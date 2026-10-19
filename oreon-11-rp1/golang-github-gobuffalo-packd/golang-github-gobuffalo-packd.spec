%global source0_hash e767bfe445d486b3522df32ace1c4034fa3533d793e5a2837bd3a887a8cfe871
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gobuffalo/packd
Version:                1.0.2
%gometa -L
%global common_description %{expand:
This is a collection of interfaces designed to make using
github.com/gobuffalo/packr easier, and to make the transition between v1 and v2
as seamless as possible.}
%global golicenses      LICENSE
%global godocs          README.md SHOULDERS.md
Name:           golang-github-gobuffalo-packd
Release:        1%{?dist}
Summary:        Gobuffalo/packr interfaces
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/packd-%{version}.tar.gz
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
