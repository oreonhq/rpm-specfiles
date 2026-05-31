%global source0_hash none
%global source1_hash none

%global source_version %(echo "%version" | tr '~' '-')

%global with_pkg_config %(pkg-config --version >/dev/null 2>&1 && echo -n "1" || echo -n "0")

%global ibus_api_version 1.0
%global pkgcache /var/cache/%name

# No gtk2 in RHEL 10
%if 0%{?rhel} > 9
%bcond_with    gtk2
%bcond_with    xinit
%else
%bcond_without gtk2
%bcond_without xinit
%endif

%if (0%{?fedora} > 33 || 0%{?rhel} > 8)
%bcond_without gtk4
%else
%bcond_with    gtk4
%endif

%global ibus_xinit_condition (%pcd1 or %pcd2 or %pcd3)
# FIXME: How to write a condition with multiple lines
%global ibus_panel_condition (%pcd1 or %pcd2 or %pcd3 or %wcd1 or %wcd2)
%global pcd1 cinnamon or deepin-desktop or i3
# Currently imsettings invokes ibus-dameon directly and that way no longer work
# in Wayland.
# Comment out lxqt-x11-session until it's installed by default in LXQt Spin
# Comment out xfce4-session until it's installed by default in XFCE Spin
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
Version:        1.5.34~rc1
# https://github.com/fedora-infra/rpmautospec/issues/101
Release:        3%{?dist}
Summary:        Intelligent Input Bus for Linux OS
License:        LGPL-2.1-or-later
URL:            https://github.com/ibus/%name/wiki
Source0:        https://github.com/ibus/%name/releases/download/%{source_version}/%{name}-%{source_version}.tar.gz
Source1:        https://github.com/ibus/%name/releases/download/%{source_version}/%{name}-%{source_version}.tar.gz.sum#/%{name}.tar.gz.sum
Source2:        %{name}-xinput
Source3:        %{name}.conf.5
# Patch0:         %%{name}-HEAD.patch
# Under testing #1349148 #1385349 #1350291 #1406699 #1432252 #1601577
Patch1:         %{name}-1385349-segv-bus-proxy.patch

# autoreconf requires autopoint but not po.m4
BuildRequires:  gettext-devel
BuildRequires:  libtool
# for gtkdoc-fixxref
BuildRequires:  glib2-doc
%if %{with gtk2}
BuildRequires:  gtk2-devel
%endif
BuildRequires:  gtk3-devel
%if %{with gtk4}
BuildRequires:  gtk4-devel
%endif
BuildRequires:  dbus-python-devel >= %{dbus_python_version}
BuildRequires:  desktop-file-utils
BuildRequires:  gtk-doc
BuildRequires:  dconf-devel
BuildRequires:  dbus-x11
BuildRequires:  python3-devel
BuildRequires:  git
BuildRequires:  vala
BuildRequires:  iso-codes-devel
BuildRequires:  libnotify-devel
BuildRequires:  wayland-devel
BuildRequires:  cldr-emoji-annotation
BuildRequires:  unicode-emoji
BuildRequires:  unicode-ucd
BuildRequires:  systemd
BuildRequires:  wayland-protocols-devel

Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
%if %{with gtk2}
Requires:      (%{name}-gtk2%{?_isa}   = %{version}-%{release} if gtk2)
%endif
Requires:      (%{name}-gtk3%{?_isa}   = %{version}-%{release} if gtk3)
%if 0%{?fedora}
Requires:      (%{name}-panel%{?_isa}  = %{version}-%{release} if %ibus_panel_condition)
%endif
%if %{with xinit}
Requires:      (%{name}-xinit          = %{version}-%{release} if %ibus_xinit_condition)
%endif
Requires:       python3-ibus           = %{version}-%{release}
Recommends:     %{name}-setup          = %{version}-%{release}

Requires:       iso-codes
# rpmlint asks to delete librsvg2
#Requires:       librsvg2

Requires:               dconf%{?_isa}
Requires(postun):       dconf%{?_isa}
Requires(posttrans):    dconf%{?_isa}

Requires:               %{_sbindir}/alternatives
Requires(post):         %{_sbindir}/alternatives
Requires(postun):       %{_sbindir}/alternatives

%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/ibus.conf

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
# GObject introspection runtime ships in glib2 (libgirepository) on this distro
Requires:       glib2%{?_isa}
%if (0%{?fedora} > 28 || 0%{?rhel} > 7)
%else
Conflicts:      %{name}%{?_isa} < %{version}
%endif

%description libs
This package contains the libraries for IBus

%if %{with gtk2}
%package gtk2
Summary:        IBus IM module for GTK2
Requires:       %{name}-libs%{?_isa}   = %{version}-%{release}
Requires:       glib2 >= %{glib_ver}
Requires(post): glib2 >= %{glib_ver}
# Added for upgrade el6 to el7
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
# setxkbmap can change XKB options for Xorg desktop sessions
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
# Owner of %%{_sysconfdir}/X11/xinit
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
# for %%{_datadir}/gettext/its
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
%if (0%{?fedora} || 0%{?rhel} > 9)
# Use no-overview mode in CI to get input focus
BuildRequires:  gnome-shell-extension-no-overview
Requires:       gnome-shell-extension-no-overview
%endif
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
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }SAVED_SUM=$(grep sha512sum %SOURCE1 | awk '{print $2}')
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
#autoreconf -f -i -v
#make -C bindings/vala maintainer-clean-generic
#make -C src/compose maintainer-clean-generic
#make -C tools maintainer-clean-generic
#make -C ui/gtk3 maintainer-clean-generic
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
# for 1385349-segv-bus-proxy.patch
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
# setxkbmap is not available in RHEL10
rm -f $RPM_BUILD_ROOT%{_datadir}/installed-tests/ibus/xkb-latin-layouts.test
%endif

# install man page
for S in %{SOURCE3}
do
  cp $S .
  MP=`basename $S` 
  gzip $MP
  install -pm 644 -D ${MP}.gz $RPM_BUILD_ROOT%{_datadir}/man/man5/${MP}.gz
done

# install xinput config file
install -pm 644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_xinputconf}

install -m 755 -d $RPM_BUILD_ROOT%pkgcache/bus
# `rpm -Vaq ibus` compare st_mode of struct stat with lstat(2) and
# st_mode of the RPM cache and if the file does not exist, st_mode of
# RPM cache is o0100000 while the actual st_mode is o0100644.
touch $RPM_BUILD_ROOT%pkgcache/bus/registry

# install .desktop files
echo "NoDisplay=true" >> $RPM_BUILD_ROOT%{_datadir}/applications/org.freedesktop.IBus.Setup.desktop
#echo "X-GNOME-Autostart-enabled=false" >> $RPM_BUILD_ROOT%%{_sysconfdir}/xdg/autostart/ibus.desktop

mkdir -p $RPM_BUILD_ROOT%{_libdir}/ibus
cp src/compose/sequences-* $RPM_BUILD_ROOT%{_libdir}/ibus

HAS_PREFIX=$(grep prefix $RPM_BUILD_ROOT%{_bindir}/ibus-setup | wc -l)
[ x"$HAS_PREFIX" == x1 ] && \
  sed -i -e '/prefix/d' $RPM_BUILD_ROOT%{_bindir}/ibus-setup

# Export GSK_RENDERER=cairo in CentOS only as a workaround.
# Not sure but seems mesa-vulkan-drivers is not configured correctly in
# CentOS and GTK is failed in CentOS CI:
# ibus-compose:10228: Gdk-WARNING **:
# Vulkan: ../src/imagination/vulkan/pvr_device.c:854:
# Failed to enumerate drm devices
# (errno 2: Δεν υπάρχει τέτοιο αρχείο ή κατάλογος)
# (VK_ERROR_INITIALIZATION_FAILED)
# https://www.linux.org.ru/forum/desktop/17554505
%if 0%{?rhel} > 9
if [ -f /etc/centos-release ] ; then
  sed -i.bak -e '/^TESTING_RUNNER=/a\
export GSK_RENDERER=cairo' \
    $RPM_BUILD_ROOT%{_libexecdir}/ibus-desktop-testing-autostart
  diff $RPM_BUILD_ROOT%{_libexecdir}/ibus-desktop-testing-autostart* || :
  ls -l $RPM_BUILD_ROOT%{_libexecdir}/ibus-desktop-testing-autostart*
  rm $RPM_BUILD_ROOT%{_libexecdir}/ibus-desktop-testing-autostart.bak
fi
%endif

desktop-file-install --delete-original          \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/*

# FIXME: no version number
%find_lang %{name}10

%check
make check \
    DISABLE_GUI_TESTS="ibus-compose ibus-keypress test-stress xkb-latin-layouts" \
    VERBOSE=1 \
    %{nil}

%post xinit
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 83 || :

%postun
if [ "$1" -eq 0 ]; then
  # ibus 1.5.31 has no ibus-xinit and need to delete %%_xinputconf here
  # for the back compatiblity for a year.
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :

  # 'dconf update' sometimes does not update the db...
  dconf update || :
  [ -f %{_sysconfdir}/dconf/db/ibus ] && \
      rm %{_sysconfdir}/dconf/db/ibus || :
fi

%postun xinit
if [ "$1" -eq 0 ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi

%posttrans
dconf update || :

# see https://bugzilla.redhat.com/show_bug.cgi?id=2439813
# for use of `env -i`
%transfiletriggerin -- %{_datadir}/ibus/component
[ -x %{_bindir}/ibus ] && \
  env -i %{_bindir}/ibus write-cache --system &>/dev/null || :

# see https://bugzilla.redhat.com/show_bug.cgi?id=2439813
# for use of `env -i`
%transfiletriggerpostun -- %{_datadir}/ibus/component
[ -x %{_bindir}/ibus ] && \
  env -i %{_bindir}/ibus write-cache --system &>/dev/null || :


%ldconfig_scriptlets libs

%files -f %{name}10.lang
# FIXME: no version number
%doc AUTHORS COPYING README
%dir %{_datadir}/ibus/
%{_bindir}/ibus
%{_bindir}/ibus-daemon
%{_datadir}/applications/org.freedesktop.IBus.Panel.Emojier.desktop
%{_datadir}/applications/org.freedesktop.IBus.Panel.Extension.Gtk3.desktop
%{_datadir}/bash-completion/completions/ibus.bash
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/ibus/component
%{_datadir}/ibus/dicts
%dir %{_datadir}/ibus/engine
%{_datadir}/ibus/keymaps
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/man/man1/ibus.1.gz
%{_datadir}/man/man1/ibus-daemon.1.gz
%{_datadir}/man/man7/ibus-emoji.7.gz
%{_datadir}/man/man5/00-upstream-settings.5.gz
%{_datadir}/man/man5/ibus.5.gz
%{_libexecdir}/ibus-engine-simple
%{_libexecdir}/ibus-dconf
%{_libexecdir}/ibus-portal
%{_libexecdir}/ibus-extension-gtk3
%{_libexecdir}/ibus-ui-emojier
%{_libexecdir}/ibus-x11
%{_sysconfdir}/dconf/db/ibus.d
%{_sysconfdir}/dconf/profile/ibus
%dir %{_sysconfdir}/xdg/Xwayland-session.d
%{_sysconfdir}/xdg/Xwayland-session.d/10-ibus-x11
%dir %{_prefix}/lib/systemd/user/gnome-session.target.wants
%{_prefix}/lib/systemd/user/gnome-session.target.wants/*.service
%{_prefix}/lib/systemd/user/org.freedesktop.IBus.session.*.service
%verify(not mtime) %dir %pkgcache
%verify(not mtime) %dir %pkgcache/bus
# 'ibus write-cache --system' updates the system cache.
%ghost %pkgcache/bus/registry

%files -n python3-ibus
%{python3_sitearch}/gi/overrides/__pycache__/*.py*
%{python3_sitearch}/gi/overrides/IBus.py

%files libs
%{_libdir}/libibus-*%{ibus_api_version}.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/IBus*-1.0.typelib

%if %{with gtk2}
%files gtk2
%{_libdir}/gtk-2.0/%{gtk2_binary_version}/immodules/im-ibus.so
%endif

%files gtk3
%{_libdir}/gtk-3.0/%{gtk3_binary_version}/immodules/im-ibus.so

%if %{with gtk4}
%files gtk4
%dir %{_libdir}/gtk-4.0/%{gtk4_binary_version}/immodules
%{_libdir}/gtk-4.0/%{gtk4_binary_version}/immodules/libim-ibus.so
%endif

# The setup package won't include icon files so that
# gtk-update-icon-cache is executed in the main package only one time.
%files setup
%{_bindir}/ibus-setup
%{_datadir}/applications/org.freedesktop.IBus.Setup.desktop
%{_datadir}/ibus/setup
%{_datadir}/man/man1/ibus-setup.1.gz

%files wayland
%{_libexecdir}/ibus-wayland

%files panel
%{_datadir}/applications/org.freedesktop.IBus.Panel.Wayland.Gtk3.desktop
%{_libexecdir}/ibus-ui-gtk3

%files xinit
%{_datadir}/man/man5/ibus.conf.5.gz
%if %{without xinit}
# ibus owns xinit directory without xorg-x11-xinit package
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit/xinput.d
%endif
# Do not use %%config(noreplace) to always get the new keywords in _xinputconf
# For user customization, $HOME/.xinputrc can be used instead.
%config %{_xinputconf}

%files devel
%{_libdir}/ibus
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gettext/its/ibus.*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/IBus*-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/ibus-*1.0.vapi
%{_datadir}/vala/vapi/ibus-*1.0.deps

%files devel-docs
# Own html dir since gtk-doc is heavy.
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/*

%files desktop-testing
%{_bindir}/ibus-desktop-testing-runner
%{_datadir}/ibus/tests
%{_libexecdir}/ibus-desktop-testing-autostart
%{_libexecdir}/ibus-desktop-testing-module

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/ibus
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/ibus

%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.34~rc1-3
- ibus-libs depend on glib2 instead of missing gobject-introspection RPM

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.34~rc1-2
- Prepare for Oreon 11 (RP1)
