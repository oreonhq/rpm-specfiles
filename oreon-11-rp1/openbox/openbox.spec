%global source0_hash abe75855cc5616554ffd47134ad15291fe37ebbebf1a80b69cbde9d670f0e26d

Name:		openbox
Version:	3.6.1
Release:	30%{?dist}
Summary:	A highly configurable and standards-compliant X11 window manager

License:	GPL-2.0-or-later
URL:		http://openbox.org
Source0:	http://openbox.org/dist/%{name}/%{name}-%{version}.tar.xz
Source1:	http://icculus.org/openbox/tools/setlayout.c
Source2:	xdg-menu
Source3:	menu.xml
Source4:	terminals.menu
Patch1:		openbox-python3.patch
Patch2:		openbox-kf5menu.patch
Patch3:		openbox-calc-layer.patch

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

# required by xdg-menu and xdg-autostart scripts
Requires:	python3-pyxdg
# used by xdg-menu for icon support (optional)
Suggests:	python3-gobject
# as discussed in https://bugzilla.redhat.com/860997
Requires:	redhat-menus

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	pango-devel
BuildRequires:	startup-notification-devel
BuildRequires:	libxml2-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXt-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXinerama-devel
BuildRequires:	imlib2-devel
# workaround for yum to install correct libpng-devel
BuildRequires:	libpng-devel
Provides:	firstboot(windowmanager)

# gdm-control, gnome-control-center and openbox-gnome were removed in 3.5.2-5
Obsoletes:	gdm-control < 3.5.2-5
Obsoletes:	gnome-panel-control < 3.5.2-5
Obsoletes:	%{name}-gnome < 3.5.2-5

%description
Openbox is a window manager designed explicity for standards-compliance and
speed. It is fast, lightweight, and heavily configurable (using XML for its
configuration data). It has many features that make it unique among window
managers: window resistance, chainable key bindings, customizable mouse
actions, multi-head/Xinerama support, and dynamically generated "pipe menus."

For a full list of the FreeDesktop.org standards with which it is compliant,
please see the COMPLIANCE file in the included documentation of this package. 
For a graphical configuration editor, you'll need to install the obconf
package.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
Requires:	pango-devel
Requires:	libxml2-devel
Requires:	glib2-devel

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	libs
Summary:	Shared libraries for %{name}

%description	libs
The %{name}-libs package contains shared libraries used by %{name}.

%package	kde
Summary:	KDE integration for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	plasma-workspace
BuildArch:	noarch

%description	kde
The %{name}-kde package contains the files needed for using %{name} inside a
KDE session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .python3
%patch -P2 -p1 -b .kf5menu
%patch -P3 -p1 -b .calc-layer

%build
%configure \
	--disable-static
## Fix RPATH hardcoding.
sed -ie 's|^hardcode_libdir_flag_spec=.*$|hardcode_libdir_flag_spec=""|g' libtool
sed -ie 's|^runpath_var=LD_RUN_PATH$|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -o setlayout %{SOURCE1} -lX11

%install
%make_install

install setlayout %{buildroot}%{_bindir}
install -p %{SOURCE2} %{buildroot}%{_libexecdir}/openbox-xdg-menu
sed 's|_LIBEXECDIR_|%{_libexecdir}|g' < %{SOURCE3} \
	> %{buildroot}%{_sysconfdir}/xdg/%{name}/menu.xml

install -m644 -p %{SOURCE4} %{buildroot}%{_sysconfdir}/xdg/%{name}/terminals.menu

# 'make install' misses these two, so we install them manually
install -m644 -D data/gnome-session/openbox-gnome.session \
	%{buildroot}%{_datadir}/gnome-session/sessions/openbox-gnome.session
install -m644 -D data/gnome-session/openbox-gnome-fallback.session \
	%{buildroot}%{_datadir}/gnome-session/sessions/openbox-gnome-fallback.session

# remove unpackaged files
pushd %{buildroot}
rm ./%{_bindir}/{gdm-control,gnome-panel-control,%{name}-gnome-session}
rm ./%{_datadir}/xsessions/%{name}-gnome.desktop
rm ./%{_datadir}/gnome/wm-properties/openbox.desktop
rm ./%{_datadir}/gnome-session/sessions/openbox-gnome*.session
rm ./%{_mandir}/man1/%{name}-gnome-session*.1*
popd

%find_lang %{name}
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files -f %{name}.lang
%doc AUTHORS CHANGELOG COMPLIANCE COPYING README
%doc data/*.xsd data/menu.xml doc/rc-mouse-focus.xml
%dir %{_sysconfdir}/xdg/%{name}/
%config(noreplace) %{_sysconfdir}/xdg/%{name}/*
%{_bindir}/%{name}
%{_bindir}/%{name}-session
%{_bindir}/obxprop
%{_bindir}/setlayout
%{_libexecdir}/openbox-*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/themes/*/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-session.1*
%{_mandir}/man1/obxprop.1*

%files	libs
%doc COPYING
%{_libdir}/libobrender.so.*
%{_libdir}/libobt.so.*

%files	devel
%{_includedir}/%{name}/
%{_libdir}/libobrender.so
%{_libdir}/libobt.so
%{_libdir}/pkgconfig/*.pc

%files  kde
%{_bindir}/%{name}-kde-session
%{_datadir}/xsessions/%{name}-kde.desktop
%{_mandir}/man1/%{name}-kde-session*.1*

%ldconfig_scriptlets libs

%changelog
%autochangelog
