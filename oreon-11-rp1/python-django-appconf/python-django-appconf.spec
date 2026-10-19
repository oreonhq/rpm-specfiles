%global source0_hash 15a88d60dd942d6059f467412fe4581db632ef03018a3c183fb415d6fc9e5cec
%global pypi_name django-appconf
Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        An app to handle configuration defaults of packaged Django apps gracefully
License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/django-appconf/
Source0:        https://files.pythonhosted.org/packages/source/d/django_appconf/django_appconf-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-appconf = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{pypi_name}
Summary:        An app to handle configuration defaults of packaged Django apps gracefully
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3dist(pytest)
%description -n python3-%{pypi_name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir django_appconf-%{version}
%oreon_prep
%build

%pyproject_wheel
sphinx-build-3 -b html docs html
rm -rf html/.{doctrees,buildinfo}
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/django_appconf* usr/lib64/python3*/site-packages/django_appconf* usr/bin/*

%check

export PYTHONPATH=.:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=tests.test_settings
%pytest -v tests/*
%files
%files -n python3-django-appconf -f %{oreon_filedir}/python3-django-appconf.list

%changelog

%autochangelog
