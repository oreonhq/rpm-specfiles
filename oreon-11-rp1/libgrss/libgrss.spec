%global source0_hash 6709c0f630a915ea7d5f1ac88ac173ef974d8d7406f43bd4be70d3e71fd554d9

Name:          libgrss
Version:       0.7.0
Release:       24%{?dist}
Summary:       Library for easy management of RSS/Atom/Pie feeds

License:       LGPL-3.0-or-later
URL:           https://wiki.gnome.org/Projects/Libgrss
Source0:       https://download.gnome.org/sources/%{name}/0.7/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: make

%description
libgrss is a Glib abstaction to handle feeds in RSS, Atom and other formats.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-static --disable-silent-rules --enable-gtk-doc
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/%{name}.so.*
%{_libdir}/girepository-1.0/Grss-0.7.typelib

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Grss-0.7.gir
%{_datadir}/gtk-doc/html/%{name}/

%changelog
%autochangelog
