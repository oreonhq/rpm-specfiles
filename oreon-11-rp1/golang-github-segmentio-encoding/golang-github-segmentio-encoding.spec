%global source0_hash 879ed211c5574c16a226a34c36d20c72072850b0661463a596d208a3e39ce6e6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/segmentio/encoding
Version:                0.5.4
%gometa -f
%global common_description %{expand:
Go package containing implementations of efficient encoding, decoding, and
validation APIs.}
%global golicenses      LICENSE json/fuzz/LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Implementations of efficient encoding, decoding, and validation APIs
License:        Apache-2.0 AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/encoding-%{version}.tar.gz
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

%ifarch s390x
for test in "TestUnmarshalMarshal" \
            "TestCompactBig" \
            "TestAppendEscape" \
            "TestIndentBig" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
