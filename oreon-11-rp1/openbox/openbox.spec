%global source1_hash 3bfa0b406cd9e4c3d5425711d237e8c701a8b88a927319be0f83428c09a629b2
%global source0_hash abe75855cc5616554ffd47134ad15291fe37ebbebf1a80b69cbde9d670f0e26d
Name:		openbox
Version:	3.6.1
Release:        1%{?dist}
Summary:        A highly configurable and standards-compliant X11 window manager
License:	GPL-2.0-or-later
URL:		http://openbox.org
Source0:        http://openbox.org/dist/%{name}/%{name}-%{version}.tar.xz
Source1:	http://icculus.org/openbox/tools/setlayout.c
Source2:	xdg-menu
Source3:	menu.xml
Source4:	terminals.menu
Patch1:		openbox-python3.patch
Patch2:		openbox-kf5menu.patch
Patch3:		openbox-calc-layer.patch
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	python3-pyxdg
Suggests:	python3-gobject
Requires:	redhat-menus
Provides:	firstboot(windowmanager)
Obsoletes:	gdm-control < 3.5.2-5
Obsoletes:	gnome-panel-control < 3.5.2-5
Obsoletes:	%{name}-gnome < 3.5.2-5
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  imlib2-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
# /oreon:deps
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
install -m644 -D data/gnome-session/openbox-gnome.session \
	%{buildroot}%{_datadir}/gnome-session/sessions/openbox-gnome.session
install -m644 -D data/gnome-session/openbox-gnome-fallback.session \
	%{buildroot}%{_datadir}/gnome-session/sessions/openbox-gnome-fallback.session
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openbox-devel -f %{oreon_filedir}/openbox-devel.list
%files -n openbox-libs -f %{oreon_filedir}/openbox-libs.list
%files -n openbox-kde -f %{oreon_filedir}/openbox-kde.list

%changelog

%autochangelog
