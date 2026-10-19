%global source0_hash c31cd5d4beb0645d6dcaa7a7dfc1bdaece0b809d606efac5f65e82d29f54ec0e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gobuffalo/logger
Version:                2.0.1
%gometa
%global common_description %{expand:
The logger.Logger interface is used throughout Buffalo apps, and other systems,
to log a whole manner of things.}
%global golicenses      LICENSE
%global godocs          README.md SHOULDERS.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Common logging interface for the Buffalo ecosystem
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/logger-%{version}.tar.gz
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
