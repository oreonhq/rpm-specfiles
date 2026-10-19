%global source0_hash 76c5ca146e7b300d175d1d6f05a13a69bd8ca4d0017a588ea5e92b464e586629
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/dlasky/gotk3-layershell
%global commit          5c5115f0d77479c452ef686e3d7f327f2a341b3c
%gometa -L -f
%global godevelheader %{expand:
Requires:  pkgconfig(gtk-layer-shell-0)
}
%global common_description %{expand:
Gotk3 addon module that provides gtk_layer_shell compatibility.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-dlasky-gotk3-layershell
Version:        0
Release:        1%{?dist}
Summary:        Gotk3 addon module that provides gtk_layer_shell compatibility
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gotk3-layershell-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(gtk-layer-shell-0)
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

# Don't build example binary
rm -rf example*

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
