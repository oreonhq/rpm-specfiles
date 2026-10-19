%global source0_hash 12a72210ce5250f8a66df562a75e034e67b2bce74c4df2983dc86d1154894943
%global source1_hash 8c22cf099c113821d6c22b7e3fc2f7033120e0e4cd7bba40d528e4ff5727cf80
%global source_version %(echo "%version" | tr '~' '-')
%global with_pkg_config %(pkg-config --version >/dev/null 2>&1 && echo -n "1" || echo -n "0")
%global ibus_api_version 1.0
%global pkgcache /var/cache/%name
%bcond_without gtk2
%bcond_without xinit
%bcond_with    gtk4
%global ibus_xinit_condition (%pcd1 or %pcd2 or %pcd3)
%global ibus_panel_condition (%pcd1 or %pcd2 or %pcd3 or %wcd1 or %wcd2)
%global pcd1 cinnamon or deepin-desktop or i3
%global pcd2 lxsession or mate-panel or phosh or awesome
%global pcd3 sugar
%global wcd1 cosmic-panel or hyprland or sway or waybar or lxqt-wayland-session
%global wcd2 budgie-desktop or plasma-workspace or xfce4-session-wayland-session
%if %with_pkg_config
%if %{with gtk2}
%{!?gtk2_binary_version: %global gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)}
%else
%{!?gtk2_binary_version: %global gtk2_binary_version ?.?.?}
%endif
%{!?gtk3_binary_version: %global gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)}
%if %{with gtk4}
%{!?gtk4_binary_version: %global gtk4_binary_version %(pkg-config  --variable=gtk_binary_version gtk4)}
%else
%{!?gtk4_binary_version: %global gtk4_binary_version ?.?.?}
%endif
%global glib_ver %([ -a /usr/%{_lib}/pkgconfig/glib-2.0.pc ] && pkg-config --modversion glib-2.0 | cut -d. -f 1,2 || echo -n "999")
%else
%{!?gtk2_binary_version: %global gtk2_binary_version ?.?.?}
%{!?gtk3_binary_version: %global gtk3_binary_version ?.?.?}
%{!?gtk4_binary_version: %global gtk4_binary_version ?.?.?}
%global glib_ver 0
%endif
%global dbus_python_version 0.83.0
Name:           ibus
Version:        1.5.34
Release:        1%{?dist}
Summary:        Intelligent Input Bus for Linux OS
License:        LGPL-2.1-or-later
URL:            https://github.com/ibus/%name/wiki
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/ibus/%name/releases/download/%{source_version}/%{name}-%{source_version}.tar.gz.sum#/%{name}.tar.gz.sum
Source2:        %{name}-xinput
Source3:        %{name}.conf.5
Patch1:         %{name}-1385349-segv-bus-proxy.patch
%if %{with gtk2}
%endif
%if %{with gtk4}
%endif
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
%if %{with gtk2}
Requires:      (%{name}-gtk2%{?_isa}   = %{version}-%{release} if gtk2)
%endif
Requires:      (%{name}-gtk3%{?_isa}   = %{version}-%{release} if gtk3)
%if %{with xinit}
Requires:      (%{name}-xinit          = %{version}-%{release} if %ibus_xinit_condition)
%endif
Requires:       python3-ibus           = %{version}-%{release}
Recommends:     %{name}-setup          = %{version}-%{release}
Requires:       iso-codes
Requires:               dconf%{?_isa}
Requires(postun):       dconf%{?_isa}
Requires(posttrans):    dconf%{?_isa}
Requires:               %{_sbindir}/alternatives
Requires(post):         %{_sbindir}/alternatives
Requires(postun):       %{_sbindir}/alternatives
%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/ibus.conf
# oreon:deps
BuildRequires:  cldr-emoji-annotation
BuildRequires:  dbus-python-devel
BuildRequires:  dbus-x11
BuildRequires:  dconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  glib2-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  iso-codes-devel
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  systemd
BuildRequires:  unicode-emoji
BuildRequires:  unicode-ucd
BuildRequires:  vala
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description
IBus means Intelligent Input Bus. It is an input framework for Linux OS.

%package -n python3-ibus
Summary:        Python 3 GObject Introspection overrides for IBus
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gobject%{?_isa}
%description -n python3-ibus
The python3-ibus package provides GObject Introspection overrides
for IBus, allowing Python applications to use the IBus library
for input method support.

%package libs
Summary:        IBus libraries
Requires:       dbus >= 1.2.4
Requires:       glib2 >= %{glib_ver}
Requires:       glib2%{?_isa}
Conflicts:      %{name}%{?_isa} < %{version}
%description libs
This package contains the libraries for IBus

%if %{with gtk2}
%package gtk2
Summary:        IBus IM module for GTK2
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
Requires:       glib2 >= %{glib_ver}
Requires(post): glib2 >= %{glib_ver}
Provides:       ibus-gtk = %{version}-%{release}
Obsoletes:      ibus-gtk < %{version}-%{release}
%description gtk2
This package contains IBus IM module for GTK2
%endif

%package gtk3
Summary:        IBus IM module for GTK3
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
Requires:       glib2 >= %{glib_ver}
Requires(post): glib2 >= %{glib_ver}
%description gtk3
This package contains IBus IM module for GTK3

%if %{with gtk4}
%package gtk4
Summary:        IBus IM module for GTK4
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
Requires:       glib2 >= %{glib_ver}
Requires(post): glib2 >= %{glib_ver}
%description gtk4
This package contains IBus IM module for GTK4
%endif

%package setup
Summary:        IBus setup utility
Requires:       %{name} = %{version}-%{release}
Requires:       python3-gobject
BuildRequires:  gobject-introspection-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  make
BuildArch:      noarch
%description setup
This is a setup utility for IBus.

%package wayland
Summary:        IBus IM module for Wayland
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
%description wayland
This package contains IBus IM module for Wayland

%package panel
Summary:        IBus Panel icon
Requires:       %{name}%{?_isa}        = %{version}-%{release}
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
%if %{with xinit}
Requires:       setxkbmap
%endif
BuildRequires:  libdbusmenu-gtk3-devel
%description panel
This package contains IBus Panel icon using GtkStatusIcon or AppIndicator
in non-GNOME desktop sessions likes XFCE or Plasma because gnome-shell
shows the IBus Icon. This package depends on libdbusmenu-gtk3 for Wayland
desktop sessions.

%package xinit
Summary:        IBus Xinit
Requires:       %{name} = %{version}-%{release}
%if %{with xinit}
Requires:       xorg-x11-xinit
%endif
BuildArch:      noarch
%description xinit
This package includes xinit scripts to set environment variables of IBus
for Xorg desktop sessions and this is not needed by Wayland desktop sessions.

%package devel
Summary:        Development tools for ibus
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
Requires:       dbus-devel
Requires:       glib2-devel
Requires:       gettext-runtime
%description devel
The ibus-devel package contains the header files and developer
docs for ibus.

%package devel-docs
Summary:        Developer documents for IBus
BuildArch:      noarch
%description devel-docs
The ibus-devel-docs package contains developer documentation for IBus

%package desktop-testing
Summary:        Wrapper of InstalledTests Runner for IBus
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description desktop-testing
GNOME desktop testing runner implements the InstalledTests specification
and IBus also needs focus events to enable input contexts on text widgets.
The wrapper script runs gnome-session for the focus events and GNOME
desktop testing runner internally.

%package  tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa}        = %{version}-%{release}
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
SAVED_SUM=$(grep sha512sum %SOURCE1 | awk '{print $2}')
MY_SUM=$(sha512sum %SOURCE0 | awk '{print $1}')
if test x"$SAVED_SUM" != x"$MY_SUM" ; then
    abort
fi
%autosetup -S git -n %{name}-%{source_version}
# cp client/gtk2/ibusimcontext.c client/gtk3/ibusimcontext.c || :
# cp client/gtk2/ibusim.c client/gtk3/ibusim.c || :
# cp client/gtk2/ibusimcontext.c client/gtk4/ibusimcontext.c || :

# prep test
for f in ibusimcontext.c ibusim.c
do
    diff client/gtk2/$f client/gtk3/$f
    if test $? -ne 0 ; then
        echo "Have to copy $f into client/gtk3"
        abort
    fi
done
diff client/gtk2/ibusimcontext.c client/gtk4/ibusimcontext.c
if test $? -ne 0 ; then
    echo "Have to copy ibusimcontext.c into client/gtk4"
    abort
fi

%build

%configure \
    --disable-static \
%if %{with gtk2}
    --enable-gtk2 \
%else
    --disable-gtk2 \
%endif
    --enable-gtk3 \
%if %{with gtk4}
    --enable-gtk4 \
%endif
    --enable-xim \
    --enable-gtk-doc \
    --enable-surrounding-text \
    --with-python=python3 \
    --disable-python2 \
    --with-python-overrides-dir=%{python3_sitearch}/gi/overrides \
    --enable-wayland \
    --enable-introspection \
    --enable-install-tests \
    %{nil}
make -C ui/gtk3 maintainer-clean-generic
%make_build
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm -f $RPM_BUILD_ROOT%{_libdir}/libibus-*%{ibus_api_version}.la
%if %{with gtk2}
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{gtk2_binary_version}/immodules/im-ibus.la
%endif
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{gtk3_binary_version}/immodules/im-ibus.la
%if %{with gtk4}
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-4.0/%{gtk4_binary_version}/immodules/libim-ibus.la
%endif
%if %{without xinit}
rm -f $RPM_BUILD_ROOT%{_datadir}/installed-tests/ibus/xkb-latin-layouts.test
%endif
for S in %{SOURCE3}
do
  cp $S .
  MP=`basename $S` 
  gzip $MP
  install -pm 644 -D ${MP}.gz $RPM_BUILD_ROOT%{_datadir}/man/man5/${MP}.gz
done
install -pm 644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_xinputconf}
install -m 755 -d $RPM_BUILD_ROOT%pkgcache/bus
touch $RPM_BUILD_ROOT%pkgcache/bus/registry
echo "NoDisplay=true" >> $RPM_BUILD_ROOT%{_datadir}/applications/org.freedesktop.IBus.Setup.desktop
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ibus
cp src/compose/sequences-* $RPM_BUILD_ROOT%{_libdir}/ibus
HAS_PREFIX=$(grep prefix $RPM_BUILD_ROOT%{_bindir}/ibus-setup | wc -l)
[ x"$HAS_PREFIX" == x1 ] && \
  sed -i -e '/prefix/d' $RPM_BUILD_ROOT%{_bindir}/ibus-setup
desktop-file-install --delete-original          \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/*
%find_lang %{name}10
%oreon_autofiles python3-ibus usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check \
    DISABLE_GUI_TESTS="ibus-compose ibus-keypress test-stress xkb-latin-layouts" \
    VERBOSE=1 \
    %{nil}
%post xinit

%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 83 || :
%postun

if [ "$1" -eq 0 ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
  dconf update || :
  [ -f %{_sysconfdir}/dconf/db/ibus ] && \
      rm %{_sysconfdir}/dconf/db/ibus || :
fi
%postun xinit

if [ "$1" -eq 0 ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi
%posttrans

dconf update || :
%transfiletriggerin -- %{_datadir}/ibus/component
[ -x %{_bindir}/ibus ] && \
  env -i %{_bindir}/ibus write-cache --system &>/dev/null || :
%transfiletriggerpostun -- %{_datadir}/ibus/component
[ -x %{_bindir}/ibus ] && \
  env -i %{_bindir}/ibus write-cache --system &>/dev/null || :
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n python3-ibus -f %{oreon_filedir}/python3-ibus.list
%files -n ibus-libs -f %{oreon_filedir}/ibus-libs.list
%files -n ibus-gtk2 -f %{oreon_filedir}/ibus-gtk2.list
%files -n ibus-gtk3 -f %{oreon_filedir}/ibus-gtk3.list
%files -n ibus-setup -f %{oreon_filedir}/ibus-setup.list
%files -n ibus-wayland -f %{oreon_filedir}/ibus-wayland.list
%files -n ibus-panel -f %{oreon_filedir}/ibus-panel.list
%files -n ibus-xinit -f %{oreon_filedir}/ibus-xinit.list
%files -n ibus-devel -f %{oreon_filedir}/ibus-devel.list
%files -n ibus-devel-docs -f %{oreon_filedir}/ibus-devel-docs.list
%files -n ibus-desktop-testing -f %{oreon_filedir}/ibus-desktop-testing.list
%files -n ibus-tests -f %{oreon_filedir}/ibus-tests.list

%changelog

%autochangelog
