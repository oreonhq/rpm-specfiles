%global source0_hash 28d68fa4831705e51ad7d1e845ed6dd9e354f9b6f8a5f63b655a430646ef4e8d

%global pkgname django-tagging
Name:           python-django-tagging
Version:        0.5.0
Release:        7%{?dist}
Summary:        A generic tagging application for Django projects

License:        MIT
URL:            https://github.com/Fantomas42/django-tagging/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
A generic tagging application for Django projects, which allows association\
of a number of tags with any Model instance and makes retrieval of tags\
simple.\

%description %_description

%package -n python3-django-tagging
Summary:        A generic tagging application for Django projects
%{?python_provide:%python_provide python3-django-tagging}
Requires:       python3-django
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-django-tagging
A generic tagging application for Django projects, which allows association
of a number of tags with any Model instance and makes retrieval of tags
simple.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-django-tagging
%doc CHANGELOG.txt LICENSE.txt README.rst docs/*
%{python3_sitelib}/tagging/
%{python3_sitelib}/django_tagging-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
