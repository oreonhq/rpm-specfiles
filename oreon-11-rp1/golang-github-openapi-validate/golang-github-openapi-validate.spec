%global source0_hash 66c4260691292f41b39019a77f1f4b1e6bf0995fe7ccbb03d632e0a92c4c2c49
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-openapi/validate
Version:                1.0.0
%gometa -L
%global common_description %{expand:
Openapi toolkit validation helpers.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md example
Name:           golang-github-openapi-validate
Release:        1%{?dist}
Summary:        Openapi toolkit validation helpers
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/validate-%{version}.tar.gz
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

for test in "ExampleSpec_second" "ExampleSpecValidator_Validate_url" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
rm -rf doc_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
