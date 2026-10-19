%global source0_hash cb7f677a7ba287ce24c3523b4b3e121c0d64096fa72cc9adeaf813b1559ecc40
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/macaroon.v2
%global forgeurl        https://github.com/go-macaroon/macaroon
Version:                2.1.0
%gometa -L -f
%global common_description %{expand:
A native Go implementation of macaroons.}
%global golicenses      LICENSE
%global godocs          README.md TODO
Name:           golang-gopkg-macaroon2
Release:        1%{?dist}
Summary:        A native Go implementation of macaroons
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/macaroon-%{version}.tar.gz
Patch1:         0001-Fix-TestAsciiHex.patch
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
