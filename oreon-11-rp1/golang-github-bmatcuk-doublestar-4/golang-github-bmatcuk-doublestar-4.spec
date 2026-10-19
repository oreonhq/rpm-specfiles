%global source0_hash bb1082ee3e27a0a25f8cab17d604e5c646cca232f16bb09587639d0b4fde8e33
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/bmatcuk/doublestar/v4
Version:                4.10.2
%gometa -f
%global common_description %{expand:
This package implements support for double star (**) matches in Golang's
path.Match and filepath.Glob.}
%global golicenses      LICENSE
%global godocs          examples README.md UPGRADING.md
Name:           golang-github-bmatcuk-doublestar-4
Release:        1%{?dist}
Summary:        Support for double star (**) matches in Go's path.Match and filepath.Glob
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/bmatcuk/doublestar/archive/v%{version}/doublestar-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
chmod 755 test/nopermission
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
