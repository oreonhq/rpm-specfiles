%global source0_hash 81b35c81c6bbaf066854261442a685a41ee27731e8c3aec388ba26632f70dba6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/chromedp/sysutil
Version:                1.1.0
%gometa
%global common_description %{expand:
Package Sysutil provides cross platform system utilities.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Cross platform system utilities
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/sysutil-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
