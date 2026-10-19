%global source0_hash 68c9d82dfe95fa65712e107010c9344e7d8b4afe8c975a7be0d273d939583a93
%global pypi_name pytest_timeout
Name:           python-pytest-timeout
Version:        2.5.0
Release:        1%{?dist}
Summary:        py.test plugin to abort hanging tests
License:        MIT
URL:            https://github.com/pytest-dev/pytest-timeout
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_timeout/pytest_timeout-2.5.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-timeout = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-timeout
Summary:        py.test plugin to abort hanging tests
%description -n python3-pytest-timeout

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n pytest_timeout-%{version}
# python-ipdb FTBFS currently
sed -i -e '/\s*ipdb$/d' tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-timeout usr/lib/python3*/site-packages/pytest_timeout* usr/lib64/python3*/site-packages/pytest_timeout* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_timeout* usr/lib64/python3*/site-packages/pytest_timeout* usr/bin/*

%check

%tox
%files
%files -n python3-pytest-timeout -f %{oreon_filedir}/python3-pytest-timeout.list

%changelog

%autochangelog
