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
Summary:        Bonobo user interface components
Name: libbonoboui
Version: 2.24.5
Release:        1%{?dist}
URL: http://www.gnome.org
Source0:        http://download.gnome.org/sources/libbonoboui/2.24/%{name}-%{version}.tar.bz2
Patch0:  libbonoboui-2.24.5-c99-pointer-cast.patch
License: LicenseRef-Callaway-LGPLv2+
Requires: ORBit2 >= %{orbit2_version}
# oreon:deps
BuildRequires:  ORBit2-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libart_lgpl-devel
BuildRequires:  libbonobo-devel
BuildRequires:  libglade2-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description

Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains the user interface related components
that come with Bonobo.

%package devel
Summary: Libraries and headers for libbonoboui
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libbonoboui-devel -f %{oreon_filedir}/libbonoboui-devel.list

%changelog

%autochangelog
