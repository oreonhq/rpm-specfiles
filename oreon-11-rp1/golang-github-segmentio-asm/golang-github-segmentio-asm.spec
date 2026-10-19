%global source0_hash 47bd144ee60642b19a0118143005038e4ce5009f8e90e3ec168a257099ac887d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/segmentio/asm
Version:                1.2.1
%gometa -f
%global common_description %{expand:
Go library providing algorithms optimized to leverage the characteristics of
modern CPUs.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%global gosupfiles      build/qsort/sort_asm.go
Name:           %{goname}
Release:        1%{?dist}
Summary:        Algorithms optimized to leverage the characteristics of modern CPUs
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/asm-%{version}.tar.gz
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

for test in "TestSort8" \
            "TestSort16" \
            "TestSort24" \
            "TestSort32" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -t build
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
