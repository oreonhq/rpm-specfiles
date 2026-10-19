%global source0_hash 145c6fe8bb4c1a037b9037d2fedaf5e49651675382d7d84a92060382b2718001
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/alecthomas/kong
Version:                1.16.1
%gometa -f
%global common_description %{expand:
Kong is a command-line parser for Go.}
%global golicenses      COPYING
%global godocs          _examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Command-line parser for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/kong-%{version}.tar.gz
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
