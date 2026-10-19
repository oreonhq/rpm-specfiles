%global source0_hash 9315d3729825b777c3b96cbae29ac0fc6ee15df84c066b601ebdd4e9e74bc23e
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/linuxdeepin/go-x11-client
Version:                1.0.2
%global tag             %{version}
%gometa -L
%global common_description %{expand:
A X11 client Go bindings for Deepin Desktop Environment.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README
Name:           golang-github-linuxdeepin-go-x11-client
Release:        1%{?dist}
Summary:        X11 client Go bindings for Deepin Desktop Environment
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/go-x11-client-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1
rm -rf tools/gen

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
