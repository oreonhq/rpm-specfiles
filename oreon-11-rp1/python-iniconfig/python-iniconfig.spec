%global source0_hash b485a7f6c060b2e758b6e58fd1bf7349a6f99954110ca61ceb59af25cf4ff458
Name:               python-iniconfig
Version:            2.3.0
Release:        1%{?dist}
Summary:        Brain-dead simple parsing of ini files
License:            MIT
URL:                http://github.com/pytest-dev/iniconfig
BuildArch:          noarch
%bcond_without tests
%if %{with tests}
%endif
Source0:        https://github.com/pytest-dev/iniconfig/archive/v2.3.0/iniconfig-2.3.0.tar.gz#/python-iniconfig-2.3.0.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-iniconfig = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-iniconfig
Summary:        Brain-dead simple parsing of ini files
%description -n python3-iniconfig

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir iniconfig-%{version}
%oreon_prep
%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-iniconfig usr/lib/python3*/site-packages/iniconfig* usr/lib64/python3*/site-packages/iniconfig* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/iniconfig* usr/lib64/python3*/site-packages/iniconfig* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
%pytest -v
%endif
%files
%files -n python3-iniconfig -f %{oreon_filedir}/python3-iniconfig.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.0-1
- Prepare for Oreon 11 (RP1)
