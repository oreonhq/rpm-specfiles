%global source0_hash fab5f2ac6c842d949861c07cb520afe5bee3dce55805151ce9cd01be0ec46fcd

%define libxml2_version 2.5
%define orbit2_version 2.5.1
%define libbonobo_version 2.13.0
%define libgnomecanvas_version 2.0.1
%define libgnome_version 2.13.7
%define libart_lgpl_version 2.3.8
%define gtk2_version 2.6.0
%define libglade2_version 2.0.0
%define glib2_version 2.6.0

%define po_package libbonoboui-2.0

Summary: Bonobo user interface components
Name: libbonoboui
Version: 2.24.5
Release: 33%{?dist}
URL: http://www.gnome.org
#VCS: git:git://git.gnome.org/libbonoboui
Source0: http://download.gnome.org/sources/libbonoboui/2.24/%{name}-%{version}.tar.bz2
# Fix FTBFS with gcc14 -Werror=incompatible-pointer-types
Patch0:  libbonoboui-2.24.5-c99-pointer-cast.patch
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+

Requires: ORBit2 >= %{orbit2_version}

BuildRequires: libxml2-devel >= %{libxml2_version}
BuildRequires: ORBit2-devel >= %{orbit2_version}
BuildRequires: libbonobo-devel >= %{libbonobo_version}
BuildRequires: libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildRequires: libgnome-devel >= %{libgnome_version}
BuildRequires: libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libglade2-devel >= %{libglade2_version}
BuildRequires: intltool >= 0.14-1
BuildRequires: libtool >= 1.4.2-12
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gettext
BuildRequires: make

%description

Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains the user interface related components
that come with Bonobo.

%package devel
Summary: Libraries and headers for libbonoboui
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
# bonobo-browser is GPL, libbonoboui is LGPL
Requires: %name = %{version}-%{release}
Requires: libxml2-devel >= %{libxml2_version}
Requires: ORBit2-devel >= %{orbit2_version}
Requires: libbonobo-devel >= %{libbonobo_version}
Requires: libgnomecanvas-devel >= %{libgnomecanvas_version}
Requires: libgnome-devel >= %{libgnome_version}
Requires: libart_lgpl-devel >= %{libart_lgpl_version}
Requires: gtk2-devel >= %{gtk2_version}
Requires: libglade2-devel >= %{libglade2_version}
Requires: glib2-devel >= %{glib2_version}
Requires: pkgconfig
Conflicts: bonobo-devel < 1.0.8

%description devel

Bonobo is a component system based on CORBA, used by the GNOME desktop.
libbonoboui contains GUI components that come with Bonobo.

This package contains header files used to compile programs that
use libbonoboui.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P0 -p1

%build

%configure --disable-gtk-doc --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.la
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/bonobo-browser.desktop

for serverfile in $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done

%find_lang %{po_package}

%ldconfig_scriptlets

%files -f %{po_package}.lang
%doc COPYING.LIB NEWS README
%{_libdir}/lib*.so.*
%{_libdir}/libglade/2.0/*.so
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0

%files devel
%doc COPYING COPYING.LIB
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_bindir}/*
%{_libdir}/bonobo-2.0
%{_datadir}/gtk-doc/html/libbonoboui

%changelog
%autochangelog
