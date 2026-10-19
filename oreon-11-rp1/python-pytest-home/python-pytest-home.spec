%global source0_hash 602151ce28186322507c7bbf1688acd567ecc00ccde37ead8946ed4ff70fd55b
Name:           python-pytest-home
Version:        0.6.0
Release:        1%{?dist}
Summary:        A temporary home directory fixture
License:        MIT
URL:            https://github.com/jaraco/pytest-home
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_home/pytest_home-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-pytest-home = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-home+test
Summary:        Metapackage for python3-pytest-home test extras
Requires:       python3-pytest-home = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-enabler) >= 2.2
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(pytest-home[test]) = %{version}-%{release}

%description -n python3-pytest-home+test
Metapackage for python3-pytest-home test extras.

%package -n       python3-pytest-home+doc
Summary:        Metapackage for python3-pytest-home doc extras
Requires:       python3-pytest-home = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Provides:       python3dist(pytest-home[doc]) = %{version}-%{release}

%description -n python3-pytest-home+doc
Metapackage for python3-pytest-home doc extras.

%description

%package -n python3-pytest-home
Summary:        A temporary home directory fixture
%description -n python3-pytest-home

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest_home-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-home usr/lib/python3*/site-packages/pytest_home* usr/lib64/python3*/site-packages/pytest_home* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_home* usr/lib64/python3*/site-packages/pytest_home* usr/bin/*

%check

mv pytest_home _pytest_home
%pytest
%files
%files -n python3-pytest-home -f %{oreon_filedir}/python3-pytest-home.list

%changelog

%autochangelog
