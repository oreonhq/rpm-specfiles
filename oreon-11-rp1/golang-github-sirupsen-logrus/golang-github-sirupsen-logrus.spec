%global source0_hash cfa48a647a28c1f12fb6a9b672bc4d88b6407ff05aedcf23ce939d342646acce
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/sirupsen/logrus
Version:                1.9.3
%gometa -L
%global common_description %{expand:
Logrus is a structured logger for Go, completely API compatible with the
standard library logger.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           golang-github-sirupsen-logrus
Release:        1%{?dist}
Summary:        Structured, pluggable logging for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/logrus-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestCallerReportingOverhead" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
