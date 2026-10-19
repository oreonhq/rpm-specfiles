%global source0_hash 7a25ce8f4214f69ac9c7ce87e2603887f7ae99326c316bc8d2d75375e09341c9
Name:           python-django-storages
Version:        1.14.6
Release:        1%{?dist}
Summary:        Support for many storage backends in Django
License:        BSD-3-Clause
URL:            https://github.com/jschneier/django-storages
Source0:        https://files.pythonhosted.org/packages/source/d/django_storages/django_storages-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-django-storages = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-storages+azure
Summary:        Metapackage for python3-django-storages azure extras
Requires:       python3-django-storages = %{version}-%{release}
Requires:       python3dist(azure-core) >= 1.13
Requires:       python3dist(azure-storage-blob) >= 12
Provides:       python3dist(django-storages[azure]) = %{version}-%{release}

%description -n python3-django-storages+azure
Metapackage for python3-django-storages azure extras.

%package -n       python3-django-storages+boto3
Summary:        Metapackage for python3-django-storages boto3 extras
Requires:       python3-django-storages = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.4.4
Provides:       python3dist(django-storages[boto3]) = %{version}-%{release}

%description -n python3-django-storages+boto3
Metapackage for python3-django-storages boto3 extras.

%package -n       python3-django-storages+dropbox
Summary:        Metapackage for python3-django-storages dropbox extras
Requires:       python3-django-storages = %{version}-%{release}
Requires:       python3dist(dropbox) >= 7.2.1
Provides:       python3dist(django-storages[dropbox]) = %{version}-%{release}

%description -n python3-django-storages+dropbox
Metapackage for python3-django-storages dropbox extras.

%package -n       python3-django-storages+google
Summary:        Metapackage for python3-django-storages google extras
Requires:       python3-django-storages = %{version}-%{release}
Requires:       python3dist(google-cloud-storage) >= 1.36.1
Provides:       python3dist(django-storages[google]) = %{version}-%{release}

%description -n python3-django-storages+google
Metapackage for python3-django-storages google extras.

%package -n       python3-django-storages+libcloud
Summary:        Metapackage for python3-django-storages libcloud extras
Requires:       python3-django-storages = %{version}-%{release}
Provides:       python3dist(django-storages[libcloud]) = %{version}-%{release}

%description -n python3-django-storages+libcloud
Metapackage for python3-django-storages libcloud extras.

%package -n       python3-django-storages+s3
Summary:        Metapackage for python3-django-storages s3 extras
Requires:       python3-django-storages = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.4.4
Provides:       python3dist(django-storages[s3]) = %{version}-%{release}

%description -n python3-django-storages+s3
Metapackage for python3-django-storages s3 extras.

%package -n       python3-django-storages+sftp
Summary:        Metapackage for python3-django-storages sftp extras
Requires:       python3-django-storages = %{version}-%{release}
Requires:       python3dist(paramiko) >= 1.15
Provides:       python3dist(django-storages[sftp]) = %{version}-%{release}

%description -n python3-django-storages+sftp
Metapackage for python3-django-storages sftp extras.

%description

%package -n     python3-django-storages
Summary:        Support for many storage backends in Django
# oreon:reqs
Requires:       python3dist(django) >= 3.2
# /oreon:reqs
%description -n python3-django-storages

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_storages-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-storages usr/lib/python3*/site-packages/django_storages* usr/lib64/python3*/site-packages/django_storages* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_storages* usr/lib64/python3*/site-packages/django_storages* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-storages -f %{oreon_filedir}/python3-django-storages.list

%changelog

%autochangelog
