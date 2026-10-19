%global source0_hash 04f550b066d798ffa490a9c8025e7d1b4cb5c2564d60a98b22e6d719baad004e
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/gotk3/gotk3
Version:                0.6.4.1
%gometa -L -f
%global godevelheader %{expand:
Requires:  pkgconfig(cairo)
Requires:  pkgconfig(cairo-gobject)
Requires:  pkgconfig(gdk-3.0)
Requires:  pkgconfig(gio-2.0)
Requires:  pkgconfig(glib-2.0)
Requires:  pkgconfig(gobject-2.0)
Requires:  pkgconfig(gtk+-3.0)
Requires:  pkgconfig(pango)
}
%global common_description %{expand:
Go bindings for GTK3.}
%global golicenses      LICENSE
%global godocs          CHANGES.md CONTRIBUTIONS.md README.md
Name:           golang-github-gotk3
Release:        1%{?dist}
Summary:        Go bindings for GTK3
License:        ISC
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gotk3-%{version}.tar.gz
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  xwayland-run
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1
dos2unix README.md

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck -d gtk
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
