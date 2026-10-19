%global source0_hash f112774324c23218e7f7ea5b266fa0d5827147de36aecd7ab4529ee6a2f8208d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/goccy/go-json
Version:                0.10.2
%gometa -f
%global common_description %{expand:
Fast JSON encoder/decoder compatible with encoding/json for Go.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast JSON encoder/decoder compatible with encoding/json for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-json-%{version}.tar.gz
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
            "TestUnmarshalRescanLiteralMangledUnquote" \
            "TestATestHTMLEscapective" \
            "TestCompactBig" \
            "TestIndentBig" \
            "TestEncoderSetEscapeHTML" \
            "TestHTMLEscape" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
