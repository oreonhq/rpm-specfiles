%global source0_hash 3ce2ba1a36011995b4f1b2038904196f6f00a482abec37ec8d78dc9e11fb6772
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jmhodges/clock
Version:                1.2.0
%gometa
%global common_description %{expand:
Package clock provides an abstraction for system time that enables testing of
time-sensitive code.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Abstraction for system time that enables testing of time-sensitive code
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/clock-%{version}.tar.gz
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
