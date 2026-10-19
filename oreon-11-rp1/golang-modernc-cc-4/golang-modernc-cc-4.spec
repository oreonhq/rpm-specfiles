%global source0_hash d962478912af4c8c5a3111b78f9a72d41ed97eddbd8daa344c63dfdd286f8976
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/cc/v4
%global forgeurl        https://gitlab.com/cznic/cc
Version:                4.24.3
%global tag             v%{version}
%global distprefix      %nil
%gometa -f
%global common_description %{expand:
Package CC is a C99 compiler front end.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS
Name:           %{goname}
Release:        1%{?dist}
Summary:        C99 compiler front end
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/cc-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
find . ! \( -name v4 -o -name AUTHORS -o -name CONTRIBUTORS -o -name LICENSE -o -name _build \) -maxdepth 1 -exec rm -rvf {} \;
mv v4/* .

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
