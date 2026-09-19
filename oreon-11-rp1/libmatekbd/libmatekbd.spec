%global source0_hash 5d2e58483c2b23d33503d24c88f8b90a28cc0189d7e4001b3e273a604f6fe80e

%global branch 1.28

Name:          libmatekbd
Version:       %{branch}.0
Release:       %autorelease
Summary:       Libraries for mate kbd
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: gtk3-devel
BuildRequires: libICE-devel
BuildRequires: libxklavier-devel
BuildRequires: mate-common
BuildRequires: gobject-introspection-devel
BuildRequires: make

%description
Libraries for matekbd

%package devel
Summary:  Development libraries for libmatekbd
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for libmatekbd

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

NOCONFIGURE=1 ./autogen.sh

%build
%configure                   \
   --disable-static          \
   --disable-schemas-compile \
   --with-x                  \
   --enable-introspection=yes
  
make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/glib-2.0/schemas/org.mate.peripherals-keyboard-xkb.gschema.xml
%{_libdir}/libmatekbd.so.6*
%{_libdir}/libmatekbdui.so.6*
%{_libdir}/girepository-1.0/Matekbd-1.0.typelib
%{_datadir}/gir-1.0/Matekbd-1.0.gir

%files devel
%{_includedir}/libmatekbd
%{_libdir}/pkgconfig/libmatekbd.pc
%{_libdir}/pkgconfig/libmatekbdui.pc
%{_libdir}/libmatekbdui.so
%{_libdir}/libmatekbd.so

%changelog
%autochangelog
