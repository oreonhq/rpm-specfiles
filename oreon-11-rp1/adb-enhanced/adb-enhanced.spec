%global source0_hash d894fb9620adef72a4cc99b7f2fd4564adcaf285613a7c477ce16e775a4bea0a
%bcond_with tests
Name:           adb-enhanced
Version:        2.11.0
Release:        1%{?dist}
Summary:        Tool for Android testing and development
License:        Apache-2.0
URL:            https://github.com/ashishb/adb-enhanced
Source0:        https://github.com/ashishb/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
ADB-Enhanced is a Swiss-army knife for Android testing and development. A
command-line interface to trigger various scenarios like screen rotation,
battery saver mode, data saver mode, doze mode, permission grant/revocation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles main
%if %{with tests}
%check

%pytest -v tests/adbe_tests.py
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
