%global source0_hash b02a3fbeb9c9dfff9fc9e3f1def80865702a8ce83cbd528995c094a053e7f9a8
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/alecthomas/units
%global commit          9a357b53e9c9395aa5fa9031ac79dc94111814e1
%gometa -L
%global common_description %{expand:
Helpful unit multipliers and functions for Go.}
%global golicenses      COPYING
%global godocs          README.md
Name:           golang-github-alecthomas-units
Version:        0
Release:        1%{?dist}
Summary:        Helpful unit multipliers and functions for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/units-%{commit}.tar.gz
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
