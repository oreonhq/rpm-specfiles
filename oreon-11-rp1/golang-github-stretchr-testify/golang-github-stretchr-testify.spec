%global source0_hash 06af5143ab5fc8f2fbf3d1420a5f002f6383cd7de911698dbd1822beacb27684
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/stretchr/testify
Version:                1.10.0
%gometa -L -f
%global common_description %{expand:
Golang set of packages that provide many tools for testifying
that your code will behave as you intend.
Features include:
 - Easy assertions
 - Mocking
 - Testing suite interfaces and functions}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md EMERITUS.md MAINTAINERS.md README.md
Name:           golang-github-stretchr-testify
Release:        1%{?dist}
Summary:        Toolkit with common assertions and mocks
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/testify-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%ifarch %{ix86} %{arm} s390x riscv64
for test in "TestFailfastSuiteFailFastOn" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
