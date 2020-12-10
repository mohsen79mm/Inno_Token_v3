from django.contrib.auth.base_user import BaseUserManager



class MyUserManager(BaseUserManager):
    def _create_user(self, username, phone=None , password=None, **other_fields):

        if not username:
            raise ValueError("username is required...!")
        if not phone:
            raise ValueError("mobile is required...!")
       
        username = self.model.normalize_username(username)
        user = self.model(username=username,phone = phone ,**other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, phone, password, **extra_fields)

    def create_superuser(self, username,phone, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
    
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser muse have is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser muse have is_superuser=True')
        return self._create_user(username,phone, password, **other_fields)