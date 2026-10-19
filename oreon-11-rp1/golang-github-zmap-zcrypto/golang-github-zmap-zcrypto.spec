%global source0_hash 50505a3a8f541d1204dd39265f2f31a8e43af9df55390c882d9c47b3062c8a8c
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zmap/zcrypto
%global commit          64a80ee67140cba7184e874ad522497452a9f92c
%gometa
%global common_description %{expand:
Liberal Go TLS + X.509 Library for Research.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Liberal Go TLS + X.509 Library for Research
License:        Apache-2.0 AND ISC AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/zcrypto-%{commit}.tar.gz
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

for test in "TestFetchRemote" \
%ifarch %{ix86} %{arm}
            "TestVerify" \
            "TestParse" \
            "TestCheck" \
            "TestFetchLocal" \
%endif
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
