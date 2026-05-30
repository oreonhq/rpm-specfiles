%global source0_hash ff97fdfb7f561d3e6813b4f6a2145259e7c2eff43cc0e63f3fd031d0b6266032

Name:          gssdp
Version:       1.6.4
Release:       %autorelease
Summary:       Resource discovery and announcement over SSDP

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.gupnp.org/
Source0:        https://download.gnome.org/sources/%{name}/1.6/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: gi-docgen
BuildRequires: gobject-introspection-devel >= 1.36
BuildRequires: meson
BuildRequires: vala >= 0.20
BuildRequires: /usr/bin/pandoc

%description
GSSDP implements resource discovery and announcement over SSDP and is part
of gUPnP.  GUPnP is an object-oriented open source framework for creating
UPnP devices and control points, written in C using GObject and libsoup. The
GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary: Development package for gssdp
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with gssdp.

%package utils
Summary: Various GUI utuls for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
This package contains GUI utilies for %{name}.

%package docs
Summary: Documentation files for %{name}
Requires: %{name} = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends: gi-docgen-fonts
BuildArch: noarch

%description docs
This package contains developer documentation for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libgssdp-1.6.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GSSDP-1.6.typelib

%files devel
%{_includedir}/gssdp-1.6/
%{_libdir}/libgssdp-1.6.so
%{_libdir}/pkgconfig/gssdp-1.6.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GSSDP-1.6.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gssdp*

%files utils
%{_bindir}/gssdp-device-sniffer
%{_mandir}/man1/gssdp-device-sniffer.1*

%files docs
%{_docdir}/gssdp-1.6/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.4-1
- Prepare for Oreon 11 (RP1)
