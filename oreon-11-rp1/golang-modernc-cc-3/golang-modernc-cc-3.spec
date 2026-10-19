%global source0_hash 5c57b00f7f5baf2f156722f45113b2848f7325e221bbc39513c295a3d978b773
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/cc/v3
%global forgeurl        https://gitlab.com/cznic/cc
Version:                3.41.0
%global tag             v%{version}
%global distprefix      %nil
%gometa -f
%global common_description %{expand:
Package CC is a C99 compiler front end.}
%global golicenses      GO-LICENSE LICENSE
%global godocs          docs README.md AUTHORS CONTRIBUTORS
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
%autopatch -p1
find . ! \( -name v3 -o -name _build \) -maxdepth 1 -exec rm -rvf {} \;
mv v3/* .

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
