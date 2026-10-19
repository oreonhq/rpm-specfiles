%global source0_hash 82124846d8318befc1518b6567b6f54bc5d23df600514af7d9db52ad7ec02109
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hebcal/greg
Version:                1.0.0
%gometa -f
%global common_description %{expand:
Converts between Gregorian dates and R.D. (Rata Die) day numbers.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Converts between Gregorian dates and R.D. (Rata Die) day numbers
License:        GPL-2.0-only
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/greg-%{version}.tar.gz
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
