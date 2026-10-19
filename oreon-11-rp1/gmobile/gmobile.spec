%global source0_hash 597373a08f21601b445319d09506b197b904c6090af0b211a78ba1c23b190bd6
%bcond docs 1
Name:     gmobile
Version:  0.7.4
Release:        1%{?dist}
Summary:        Functions useful in mobile related, glib based projects
License:  LGPL-2.1-or-later AND GPL-3.0-or-later
URL:      https://gitlab.gnome.org/World/Phosh/gmobile
Source0:        https://gitlab.gnome.org/World/Phosh/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
%if %{with docs}
%endif
Requires:  systemd-udev
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  marshalparser
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  python3dist(docutils)
BuildRequires:  systemd
# /oreon:deps
%description
gmobile carries some helpers for glib based environments on mobile devices.

%package devel
Summary:   Development headers for the gmobile library
Requires:  %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
Development headers for the gmobile library.

%if %{with docs}
%package docs
Summary:  Documentation for the gmobile library
License:  LGPL-2.1-or-later AND GPL-3.0-or-later AND (Apache-2.0 OR GPL-3.0-or-later) AND MIT
%description docs
Documentation for the gmobile library.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%meson \
%if %{with docs}
    -Dgtk_doc=true \
    -Dman=true \
%endif
    -Dexamples=false \
    -Dvapi=false
%meson_build
%install
%meson_install
rm -v %{buildroot}/%{_libdir}/libgmobile.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gmobile-devel -f %{oreon_filedir}/gmobile-devel.list
%files -n gmobile-docs -f %{oreon_filedir}/gmobile-docs.list

%changelog

%autochangelog
