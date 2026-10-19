%global source0_hash 532d6e152bc1c031a9e8d7bf3236ca59891ef1a0d0ad61b84103b36c89241304
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/bep/clocks
Version:                0.5.0
%gometa -L -f
%global godevelheader %{expand:
Obsoletes:      golang-github-bep-clock-devel < 0.3.0-4
}
%global common_description %{expand:
A Golang clock that allows you to set the start time.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-bep-clocks
Release:        1%{?dist}
Summary:        A Golang clock that allows you to set the start time
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/clocks-%{version}.tar.gz
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
