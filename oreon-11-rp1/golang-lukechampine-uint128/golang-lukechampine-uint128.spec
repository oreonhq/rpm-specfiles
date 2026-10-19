%global source0_hash 4056b6be2d0f8346191ddec2da02fe6467edbd2ed0fb02ced9b8004017a307ca
%bcond check 0
%global debug_package %{nil}
%global goipath         lukechampine.com/uint128
%global forgeurl        https://github.com/lukechampine/uint128
Version:                1.3.0
%gometa -f
%global common_description %{expand:
Uint128 for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Uint128 for Go
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/uint128-%{version}.tar.gz
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
