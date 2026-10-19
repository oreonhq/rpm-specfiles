%global source0_hash 9e8f002e9057ae08f01db5c2ebecfa8800a1f1ff9f07e63bae81b3fdda4821ca
%bcond check 0
%global debug_package %{nil}
%global goipath         go.mau.fi/zeroconfig
%global forgeurl        https://github.com/tulir/zeroconfig
Version:                0.1.2
%gometa -L -f
%global common_description %{expand:
A relatively simple declarative config format for zerolog.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-mau-zeroconfig
Release:        1%{?dist}
Summary:        A relatively simple declarative config format for zerolog
License:        MPL-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/zeroconfig-%{version}.tar.gz
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
