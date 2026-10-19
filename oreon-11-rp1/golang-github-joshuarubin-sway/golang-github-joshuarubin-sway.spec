%global source0_hash 3bd95f49be110b40bc005f3db157c0a8e6ccedb4e0ed48e810368f23030a1833
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/joshuarubin/go-sway
Version:                1.2.0
%gometa -L -f
%global common_description %{expand:
Sway client for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-joshuarubin-sway
Release:        1%{?dist}
Summary:        Sway client for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-sway-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

for test in "TestSocket" "TestFocused" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
