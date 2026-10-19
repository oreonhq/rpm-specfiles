%global source0_hash 26787dd3f422cfbab8f55b80a776e2edea7a11092cb74e960bef1312515708ef
Name:           python-pytest-django
Version:        4.14.0
Release:        1%{?dist}
Summary:        A Django plugin for pytest.
License:        ...
URL:            https://github.com/pytest-dev/pytest-django
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_django/pytest_django-%{version}.tar.gz
BuildArch:      noarch
Patch:          pytest_django-lower-pytest-req.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 5.0.0
Requires:       python3-pytest-django = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-django+django
Summary:        Metapackage for python3-pytest-django django extras
Requires:       python3-pytest-django = %{version}-%{release}
Requires:       python3dist(django) >= 5.2
Provides:       python3dist(pytest-django[django]) = %{version}-%{release}

%description -n python3-pytest-django+django
Metapackage for python3-pytest-django django extras.

%package -n       python3-pytest-django+docs
Summary:        Metapackage for python3-pytest-django docs extras
Requires:       python3-pytest-django = %{version}-%{release}
Provides:       python3dist(pytest-django[docs]) = %{version}-%{release}

%description -n python3-pytest-django+docs
Metapackage for python3-pytest-django docs extras.

%description

%package -n     python3-pytest-django
Summary:        A Django plugin for pytest.
# oreon:reqs
Requires:       python3dist(pytest) >= 7.0.0
# /oreon:reqs
%description -n python3-pytest-django

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_django-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-django usr/lib/python3*/site-packages/pytest_django* usr/lib64/python3*/site-packages/pytest_django* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_django* usr/lib64/python3*/site-packages/pytest_django* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-django -f %{oreon_filedir}/python3-pytest-django.list

%changelog

%autochangelog
