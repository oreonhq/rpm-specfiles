%global source0_hash dc98b5561061754fdae18374e7a596ea473d3bda11e27bfb1f2011b32ba37732
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zclconf/go-cty-debug
%global commit          0d6042c539401a57fc0cca85ded2861d4a5173c4
%gometa -L -f
%global common_description %{expand:
Debugging and inspection utilities for cty.}
%global golicenses      LICENSE
Name:           golang-github-zclconf-cty-debug
Version:        0
Release:        1%{?dist}
Summary:        Debugging and inspection utilities for cty
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-cty-debug-%{commit}.tar.gz
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
