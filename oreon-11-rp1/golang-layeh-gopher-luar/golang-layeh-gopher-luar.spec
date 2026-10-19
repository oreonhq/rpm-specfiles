%global source0_hash bafcccca7db8203ae70d3b3de670ef9aa2d6c24b13c3a9402fec2f920a971d6f
%bcond check 0
%global debug_package %{nil}
%global goipath         layeh.com/gopher-luar
%global forgeurl        https://github.com/layeh/gopher-luar
Version:                1.0.8
%gometa
%global common_description %{expand:
Gopher-luar simplifies data passing to and from gopher-lua.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simplifies data passing to and from gopher-lua
License:        MPL-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/gopher-luar-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/yuin/gopher-lua)
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
