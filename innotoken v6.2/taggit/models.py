from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError, models, router, transaction
from django.utils.text import slugify
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

try:
    from unidecode import unidecode
except ImportError:

    def unidecode(tag):
        return tag


class TagBase(models.Model):
    name = models.CharField(verbose_name=_("name"), unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            slug=self.name.replace(' ', '_')   
            self.slug = slugify(f'{slug}', allow_unicode=True)
        return super().save(*args, **kwargs)


class Tag(TagBase):
    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        app_label = "taggit"


class ItemBase(models.Model):
    def __str__(self):
        return gettext("%(object)s tagged with %(tag)s") % {
            "object": self.content_object,
            "tag": self.tag,
        }

    class Meta:
        abstract = True

    @classmethod
    def tag_model(cls):
        field = cls._meta.get_field("tag")
        return field.remote_field.model

    @classmethod
    def tag_relname(cls):
        field = cls._meta.get_field("tag")
        return field.remote_field.related_name

    @classmethod
    def lookup_kwargs(cls, instance):
        return {"content_object": instance}

    @classmethod
    def tags_for(cls, model, instance=None, **extra_filters):
        kwargs = extra_filters or {}
        if instance is not None:
            kwargs.update({"%s__content_object" % cls.tag_relname(): instance})
            return cls.tag_model().objects.filter(**kwargs)
        kwargs.update({"%s__content_object__isnull" % cls.tag_relname(): False})
        return cls.tag_model().objects.filter(**kwargs).distinct()


class TaggedItemBase(ItemBase):
    tag = models.ForeignKey(
        Tag, related_name="%(app_label)s_%(class)s_items", on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class CommonGenericTaggedItemBase(ItemBase):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name=_("content type"),
        related_name="%(app_label)s_%(class)s_tagged_items",
    )
    content_object = GenericForeignKey()

    class Meta:
        abstract = True

    @classmethod
    def lookup_kwargs(cls, instance):
        return {
            "object_id": instance.pk,
            "content_type": ContentType.objects.get_for_model(instance),
        }

    @classmethod
    def tags_for(cls, model, instance=None, **extra_filters):
        tag_relname = cls.tag_relname()
        model = model._meta.concrete_model
        kwargs = {
            "%s__content_type__app_label" % tag_relname: model._meta.app_label,
            "%s__content_type__model" % tag_relname: model._meta.model_name,
        }
        if instance is not None:
            kwargs["%s__object_id" % tag_relname] = instance.pk
        if extra_filters:
            kwargs.update(extra_filters)
        return cls.tag_model().objects.filter(**kwargs).distinct()


class GenericTaggedItemBase(CommonGenericTaggedItemBase):
    object_id = models.IntegerField(verbose_name=_("object ID"), db_index=True)

    class Meta:
        abstract = True


class GenericUUIDTaggedItemBase(CommonGenericTaggedItemBase):
    object_id = models.UUIDField(verbose_name=_("object ID"), db_index=True)

    class Meta:
        abstract = True


class TaggedItem(GenericTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("tagged item")
        verbose_name_plural = _("tagged items")
        app_label = "taggit"
        index_together = [["content_type", "object_id"]]
        unique_together = [["content_type", "object_id", "tag"]]
