%global source0_hash 0f8acabe5ca7b07025fff0ae86a58105437c76f0ec0d95914360b518f385b968
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/uber-go/tally
Version:                4.1.7
%gometa
%global goaltipaths     github.com/uber-go/tally/v4
%global common_description %{expand:
A Go metrics interface with fast buffered metrics and third party reporters.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A Go metrics interface with fast buffered metrics and third party reporters
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/tally-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

rm -rf m3/example tools

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%ifarch i686
%gocheck -t m3
%else
%ifarch ppc64le s390x
for test in "TestVerifyCachedTaggedScopesAlloc" \
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
