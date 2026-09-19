%global source0_hash de21f20f9e7eb941529d75078b18192506a9f6d4ae80f86fbe2f3bcac8e09d71

%global pypi_name django-pytest

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        46%{?dist}
Summary:        Allows you to use py.test as a django test runner

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/buchuki/django-pytest
Source0:        http://pypi.python.org/packages/source/d/django-pytest/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
This project allows you to use py.test as a django test runner,\
instead of the default test runner.

%description %_description

%package -n     python3-%{pypi_name}
Summary:        Allows you to use py.test as a django test runner

Requires:       python3-django
Requires:       python3-pytest

Obsoletes:      python-%{pypi_name} < 0.2.0-16
Obsoletes:      python2-%{pypi_name} < 0.2.0-16

%description -n python3-%{pypi_name}
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
# remove the bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc LICENSE.txt README.md
%{python3_sitelib}/django_pytest/
%{python3_sitelib}/django_pytest-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
