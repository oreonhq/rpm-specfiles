%global source0_hash 3c47c66fbfbd268ef46269673a0516a039539b0972b8ed2ec9cfee44c4b65523

%global srcname django-pglocks

Name:           python-%{srcname}
Version:        1.0.4
Release:        20%{?dist}
Summary:        Context managers for advisory locks for PostgreSQL

# https://github.com/Xof/django-pglocks/issues/28
License:        MIT
URL:            https://github.com/Xof/django-pglocks
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
# distutils does not support dependencies
# https://github.com/Xof/django-pglocks/pull/27
sed -i -e "s/from distutils.core import setup/from setuptools import setup/" setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGES.txt
%{python3_sitelib}/django_pglocks-*.egg-info/
%{python3_sitelib}/django_pglocks/

%changelog
%autochangelog
