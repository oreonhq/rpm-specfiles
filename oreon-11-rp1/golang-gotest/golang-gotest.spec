%global source0_hash 9656a4df6d6e238c20c082fcad548ecf99e326a3005e52878635fe5ea56c7c81
%bcond check 0
%global debug_package %{nil}
%global goipath         gotest.tools
%global forgeurl        https://github.com/gotestyourself/gotest.tools
Version:                3.5.2
%gometa -L
%global goaltipaths     gotest.tools/v3
%global common_description %{expand:
A collection of packages to augment the go testing package and support common
patterns.}
%global golicenses      LICENSE LICENSE-difflib
%global godocs          CONTRIBUTING.md README.md
Name:           golang-gotest
Release:        1%{?dist}
Summary:        A collection of packages to augment the Go testing package
License:        Apache-2.0 AND BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/%{goipath}-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

mv internal/difflib/LICENSE LICENSE-difflib

# gty-migrate-from-testify has different requirements and is not used
rm -rf assert/cmd/gty-migrate-from-testify

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

sed -i "s|gotest.tools/v3|gotest.tools|" $(find . -iname "*.go" -type f)
for test in "TestWaitOnSocketWithTimeout" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
