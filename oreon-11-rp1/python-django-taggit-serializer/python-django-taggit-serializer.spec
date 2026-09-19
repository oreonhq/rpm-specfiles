%global source0_hash f712eb2482079be452bcd1e82b18a820e26427c3ee1cef2b4fcd4d6b8b9f14d0

%global srcname django-taggit-serializer

Name:           python-%{srcname}
Version:        0.1.7
Release:        24%{?dist}
Summary:        Django Taggit serializer for Django REST Framework

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/glemmaPaul/django-taggit-serializer
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md HISTORY.rst
%{python3_sitelib}/django_taggit_serializer-*.egg-info/
%{python3_sitelib}/taggit_serializer/

%changelog
%autochangelog
