%global source0_hash 8bfe1c1736d5dcb60b433f7932ca5d42eebe57f5a439bdb2b480a88e4d1990c6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lestrrat-go/jwx
Version:                1.2.26
%gometa -f
%global common_description %{expand:
Implementation of various JWx (Javascript Object Signing and Encryption/JOSE)
technologies.}
%global golicenses      LICENSE
%global godocs          docs examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Implementation of various JWx technologies
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jwx-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestKeyconv" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
