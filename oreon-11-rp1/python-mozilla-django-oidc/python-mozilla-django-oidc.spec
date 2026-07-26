%global source0_hash c9e6e0e33c319d1261d53cbd474df0dbacb79ddcff1ace97bbbcaf2fe6636df5

%global shortname mozilla-django-oidc
Name:          python-%{shortname}
Version:       4.0.1
Release:       5%{?dist}
Summary:       A django OpenID Connect library

License:       MPL-2.0
URL:           https://github.com/mozilla/%{shortname}/
Source0:       https://github.com/mozilla/%{shortname}/archive/%{version}.tar.gz#/%{shortname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

%description
A django OpenID Connect library.

%package -n python3-%{shortname}
Summary:       A django OpenID Connect library
%{?python_provide:%python_provide python3-%{shortname}}
Requires:      python3-django

%description -n python3-%{shortname}
A django OpenID Connect library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{shortname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mozilla_django_oidc

%files -n python3-%{shortname} -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
