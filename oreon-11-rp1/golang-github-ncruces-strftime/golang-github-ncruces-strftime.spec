%global source0_hash 67e1785acddfe20586da40628b74773b467e052dd4e133df0acefd1d6f259bd3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ncruces/go-strftime
Version:                0.1.9
%gometa -L -f
%global common_description %{expand:
Strftime/strptime for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-ncruces-strftime
Release:        1%{?dist}
Summary:        Strftime/strptime for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-strftime-%{version}.tar.gz
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
