%global source0_hash 734d973c14b6b8fae9a0e3f00e5c049bf6c879f335d3ae851bc9496e8c8bc8b9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/wI2L/jettison
Version:                0.7.4
%gometa -f
%global common_description %{expand:
Highly configurable, fast JSON encoder for Go.}
%global golicenses      LICENSE LICENSE.golang
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Highly configurable, fast JSON encoder for Go
License:        BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jettison-%{version}.tar.gz
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
