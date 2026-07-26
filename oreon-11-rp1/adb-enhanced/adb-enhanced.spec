%global source0_hash cb8e4afdccf07b812928bef01a6df9cafcff7185919484a2c4597113f9cea9b7

%bcond_with tests

Name:           adb-enhanced
Version:        2.5.24
Release:        8%{?dist}
Summary:        Tool for Android testing and development

License:        Apache-2.0
URL:            https://github.com/ashishb/adb-enhanced
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
ADB-Enhanced is a Swiss-army knife for Android testing and development. A
command-line interface to trigger various scenarios like screen rotation,
battery saver mode, data saver mode, doze mode, permission grant/revocation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%pytest -v tests/adbe_tests.py
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/adbe
%{python3_sitelib}/adbe/
%{python3_sitelib}/adb_enhanced*.egg-info/

%changelog
%autochangelog
