%global source0_hash c163ae80d2e0b22d8fb598047cd0dcef31f81830e127cfecae278ad574167260

%global srcname django-js-asset

Name:           python-%{srcname}
Version:        1.2.2
Release:        24%{?dist}
Summary:        Script tag with additional attributes for django.forms.Media

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/matthiask/django-js-asset
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# https://github.com/matthiask/django-js-asset/pull/5
Requires:       python%{python3_version}dist(django)

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
%doc README.rst
%{python3_sitelib}/django_js_asset-*.egg-info/
%{python3_sitelib}/js_asset/

%changelog
%autochangelog
