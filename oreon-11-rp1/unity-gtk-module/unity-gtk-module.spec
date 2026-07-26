%global source0_hash 381238e8734fdbd90cc826b7490775378e0f4725506aa3192689668ca198d9fe

# old code base is not fully compatible with GCC 14
%global build_type_safety_c 2

Name:		unity-gtk-module
Version:	0.0.0+17.04.20170403
Release:	24%{?dist}
Summary:	GTK+ module for exporting old-style menus as GMenuModels

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:	LGPL-3.0-only
URL:		https://launchpad.net/%{name}
Source0:	http://archive.ubuntu.com/ubuntu/pool/main/u/%{name}/%{name}_%{version}.orig.tar.gz

BuildRequires: make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libX11-devel
BuildRequires:	libtool
BuildRequires:	python3-devel

%description
GTK+ module for exporting old-style menus as GMenuModels.
Many applications implement menus as GtkMenuShells and GtkMenuItems
and aren't looking to migrate to the newer GMenuModel API.
This GTK+ module watches for these types of menus and exports the
appropriate GMenuModel implementation.

%package -n libunity-gtk-parser-devel
Summary:	Common development-files for libunity-gtk{2,3}-parser

BuildArch:	noarch

BuildRequires:	gtk-doc

%description -n libunity-gtk-parser-devel
This package contains common headers and documentation for
libunity-gtk{2,3}-parser.

%package -n libunity-gtk2-parser
Summary:	Gtk2MenuShell to GMenuModel parser

BuildRequires:	gtk2-devel

%description -n libunity-gtk2-parser
This library converts Gtk2MenuShells into GMenuModels.

%package -n libunity-gtk2-parser-devel
Summary:	Development-files for libunity-gtk2-parser

Requires:	gtk2-devel%{?_isa}
Requires:	libunity-gtk-parser-devel	== %{version}-%{release}
Requires:	libunity-gtk2-parser%{?_isa}	== %{version}-%{release}

%description -n libunity-gtk2-parser-devel
This package contains development-files for libunity-gtk2-parser.

%package -n libunity-gtk3-parser
Summary:	Gtk3MenuShell to GMenuModel parser

BuildRequires:	gtk3-devel

%description -n libunity-gtk3-parser
This library converts Gtk3MenuShells into GMenuModels.

%package -n libunity-gtk3-parser-devel
Summary:	Development-files for libunity-gtk3-parser

Requires:	gtk3-devel%{?_isa}
Requires:	libunity-gtk-parser-devel	== %{version}-%{release}
Requires:	libunity-gtk3-parser%{?_isa}	== %{version}-%{release}

%description -n libunity-gtk3-parser-devel
This package contains development-files for libunity-gtk3-parser.

%package -n unity-gtk-module-common
Summary:	Common files for unity-gtk{2,3}-module

BuildArch:	noarch

BuildRequires:	systemd

Requires:	/bin/sh
Requires:	dbus
Requires:	gawk
Requires:	sed
Requires:	systemd

%description -n unity-gtk-module-common
This package contains common data-files for unity-gtk{2,3}-module.

%package -n unity-gtk2-module
Summary:	Gtk2MenuShell D-Bus exporter

Requires:	libunity-gtk2-parser%{?_isa}	== %{version}-%{release}
Requires:	unity-gtk-module-common		== %{version}-%{release}

Provides:	appmenu-gtk			== %{version}-%{release}
Provides:	appmenu-gtk%{?_isa}		== %{version}-%{release}

%description -n unity-gtk2-module
This GTK+ 2 module exports Gtk2MenuShells over D-Bus.

%package -n unity-gtk3-module
Summary:	Gtk3MenuShell D-Bus exporter

Requires:	libunity-gtk3-parser%{?_isa}	== %{version}-%{release}
Requires:	unity-gtk-module-common		== %{version}-%{release}

Provides:	appmenu-gtk3			== %{version}-%{release}
Provides:	appmenu-gtk3%{?_isa}		== %{version}-%{release}

%description -n unity-gtk3-module
This GTK+ 3 module exports Gtk3MenuShells over D-Bus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
%{__mkdir} -p build/gtk2 build/gtk3 m4

# Initialize build-environment.
%{_bindir}/gtkdocize --copy
%{_bindir}/autoreconf -fiv

# Setup systemd-unit for Fedora.
f="data/%{name}.service"
%{__sed} -i.orig -e's!^Before=!After=dbus.service\n&!'		\
	-e's!ubuntu-session.target$!default.target!g'		\
	-e's!graphical-session.target$!default.target!g'	\
	-e's!dbus-update-activation-environment!%{_bindir}/&!g'	\
	-e's!awk!%{_bindir}/&!g' -e's!sed!%{_bindir}/&!' ${f}
%{_bindir}/touch -r ${f}.orig ${f} && %{__rm} ${f}.orig

%build
export PYTHON="%{__python3}"
export SRC_DIR="$(%{_bindir}/pwd)"
for i in 2 3 ; do
	pushd build/gtk${i}
	%{_bindir}/ln ../../configure configure
	%configure	\
		--disable-silent-rules				\
		--disable-static				\
		--enable-gtk-doc				\
		--with-gtk=${i}					\
		--srcdir="${SRC_DIR}"
	%make_build
	popd
done

%install
for i in 2 3 ; do
	%make_install -C build/gtk${i}
done

# Setup systemd.
%{__mkdir} -p %{buildroot}%{_userunitdir}/default.target.wants
%{_bindir}/ln -s						\
	%{_userunitdir}/%{name}.service				\
	%{buildroot}%{_userunitdir}/default.target.wants/%{name}.service

# We don't ship libtool-dumplings.
%{_bindir}/find %{buildroot}%{_libdir} -name '*.la' -delete

# Those files are not needed during runtime.
%{__rm} -rf %{buildroot}%{_datadir}/upstart/			\
	%{buildroot}%{python3_sitelib}

# Prepare demos for inclusion in %%doc.
%{__rm} -f demos/Makefile*

%ldconfig_scriptlets -n libunity-gtk2-parser

%ldconfig_scriptlets -n libunity-gtk3-parser

%files -n libunity-gtk-parser-devel
%doc demos
%doc %{_datadir}/gtk-doc
%{_includedir}/unity-gtk-parser

%files -n libunity-gtk2-parser
%license AUTHORS COPYING*
%{_libdir}/libunity-gtk2-parser.so.0*

%files -n libunity-gtk2-parser-devel
%{_libdir}/libunity-gtk2-parser.so
%{_libdir}/pkgconfig/unity-gtk2-parser.pc

%files -n libunity-gtk3-parser
%license AUTHORS COPYING*
%{_libdir}/libunity-gtk3-parser.so.0*

%files -n libunity-gtk3-parser-devel
%{_libdir}/libunity-gtk3-parser.so
%{_libdir}/pkgconfig/unity-gtk3-parser.pc

%files -n unity-gtk-module-common
%license AUTHORS COPYING*
%{_datadir}/glib-2.0
%{_userunitdir}/default.target.wants
%{_userunitdir}/%{name}.service

%files -n unity-gtk2-module
%{_libdir}/gtk-2.0/modules/lib%{name}.so

%files -n unity-gtk3-module
%{_libdir}/gtk-3.0/modules/lib%{name}.so

%changelog
%autochangelog
