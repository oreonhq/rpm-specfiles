%global source0_hash 1be3f7522a315e6db3f09e25983911f55e42b014c590a35f5511664c8a25cb47
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/xc
%global forgeurl        https://gitlab.com/cznic/xc
Version:                1.1.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Cross language compiler support/utility stuff.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Cross language compiler support/utility stuff
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/xc-%{tag}.tar.bz2
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
