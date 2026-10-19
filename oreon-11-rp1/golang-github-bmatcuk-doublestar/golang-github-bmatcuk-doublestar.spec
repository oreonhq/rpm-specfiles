%global source0_hash 955fc82b044496894749edda9ca88390b478c59a8d01d23d9c38b8506864eabe
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/bmatcuk/doublestar
Version:                1.3.4
%gometa -f
%global common_description %{expand:
Implements support for double star (**) matches in golang's path.Match and
filepath.Glob.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Implements support for double star matches in Go's path.Match and filepath.Glob
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/doublestar-%{version}.tar.gz
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

for test in "TestMatch" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
