%global source0_hash cc60b6da691eb524a956cc65a02f1749f4e497185f6a73f1394607158944510c
%bcond tests 1
%bcond minimal_tests 1
%bcond full_tests 0
Name:           python-fortranformat
Version:        2.0.3
Release:        1%{?dist}
Summary:        FORTRAN format interpreter for Python
License:        MIT
URL:            https://github.com/brendanarnold/py-fortranformat
Source0:        https://github.com/brendanarnold/py-fortranformat/archive/refs/tags/v%{version}.tar.gz#./%{name}-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%if %{with minimal_tests} || %{with full_tests}
%endif
%if %{with full_tests}
%endif
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-fortranformat = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-fortranformat
Summary:        FORTRAN format interpreter for Python
%description -n python3-fortranformat

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n py-fortranformat-%{version}
sed -r -i 's@\bpython\b@%{python3}@' Makefile

%build

%pyproject_wheel
%if %{with tests}
%if %{with minimal_tests} || %{with full_tests}
%make_build buildtests
%endif
%if %{with full_tests}
%make_build compilertests
%endif
%endif
%install
%pyproject_install
%oreon_autofiles python3-fortranformat usr/lib/python3*/site-packages/fortranformat* usr/lib64/python3*/site-packages/fortranformat* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fortranformat* usr/lib64/python3*/site-packages/fortranformat* usr/bin/*

%check

%pyproject_check_import fortranformat
%if %{with tests}
%if %{without full_tests} && %{without minimal_tests}
%pytest tests/handwritten
%endif
%if %{with minimal_tests}
%py3_test_envvars %make_build runminimaltests
%endif
%if %{with full_tests}
%py3_test_envvars %make_build runtests
%endif
%endif
%files
%files -n python3-fortranformat -f %{oreon_filedir}/python3-fortranformat.list

%changelog

%autochangelog
