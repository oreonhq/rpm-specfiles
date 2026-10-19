%global source0_hash 2607197f390912ab25525d129ac43c3c875049257368b3fe09b5cd03dcc526af
Name:           python-pytest-localserver
Version:        0.10.0
Release:        1%{?dist}
Summary:        pytest plugin to test server connections locally
License:        MIT
URL:            https://github.com/pytest-dev/pytest-localserver
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_localserver/pytest_localserver-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-pytest-localserver = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pytest-localserver
Summary:        pytest plugin to test server connections locally
%description -n python3-pytest-localserver

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest_localserver-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-localserver usr/lib/python3*/site-packages/pytest_localserver* usr/lib64/python3*/site-packages/pytest_localserver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_localserver* usr/lib64/python3*/site-packages/pytest_localserver* usr/bin/*

%check

%tox
%files
%files -n python3-pytest-localserver -f %{oreon_filedir}/python3-pytest-localserver.list

%changelog

%autochangelog
