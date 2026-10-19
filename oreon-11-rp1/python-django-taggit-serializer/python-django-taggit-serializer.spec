%global source0_hash f712eb2482079be452bcd1e82b18a820e26427c3ee1cef2b4fcd4d6b8b9f14d0
%global srcname django-taggit-serializer
Name:           python-%{srcname}
Version:        0.1.7
Release:        1%{?dist}
Summary:        Django Taggit serializer for Django REST Framework
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/glemmaPaul/django-taggit-serializer
Source0:        https://files.pythonhosted.org/packages/source/p/python-django-taggit-serializer/python-django-taggit-serializer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package     -n python3-%{srcname}
Summary:        Django Taggit serializer for Django REST Framework
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%description -n python3-%{srcname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-django-taggit-serializer -f %{oreon_filedir}/python3-django-taggit-serializer.list

%changelog

%autochangelog
