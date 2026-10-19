%global source0_hash 20488ef3f15dd4f04d6225a44b5deb5525e39ba433142246aecfa4d9ec27ba81
%bcond_without check
Name:           python-pytest-datadir
Version:        1.8.0
Release:        1%{?dist}
Summary:        Pytest plugin for test data directories and files
License:        MIT
URL:            https://github.com/gabrielcnr/pytest-datadir
Source0:        https://github.com/gabrielcnr/pytest-datadir/archive/v%{version}/pytest-datadir-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-pytest-datadir = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-datadir+testing
Summary:        Metapackage for python3-pytest-datadir testing extras
Requires:       python3-pytest-datadir = %{version}-%{release}
Provides:       python3dist(pytest-datadir[testing]) = %{version}-%{release}

%description -n python3-pytest-datadir+testing
Metapackage for python3-pytest-datadir testing extras.

%package -n       python3-pytest-datadir+dev
Summary:        Metapackage for python3-pytest-datadir dev extras
Requires:       python3-pytest-datadir = %{version}-%{release}
Provides:       python3dist(pytest-datadir[dev]) = %{version}-%{release}

%description -n python3-pytest-datadir+dev
Metapackage for python3-pytest-datadir dev extras.

%description

%package -n     python3-pytest-datadir
Summary:        Pytest plugin for test data directories and files
# oreon:reqs
Requires:       python3dist(pytest) >= 7.0
# /oreon:reqs
%description -n python3-pytest-datadir

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-datadir-%{version}
%oreon_prep
%build

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-datadir usr/lib/python3*/site-packages/pytest_datadir* usr/lib64/python3*/site-packages/pytest_datadir* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_datadir* usr/lib64/python3*/site-packages/pytest_datadir* usr/bin/*
%if %{with check}
%check

%pyproject_check_import
%pytest
%endif
%files
%files -n python3-pytest-datadir -f %{oreon_filedir}/python3-pytest-datadir.list

%changelog

%autochangelog
