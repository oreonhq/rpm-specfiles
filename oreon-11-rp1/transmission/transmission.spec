%global source0_hash e743283ee03a42c4d0b08fed2bd52b554aa6c9f65b4d4d45b795c32d98762a79

Name:           transmission
Version:        4.1.1
Release:        2%{?dist}
Summary:        A lightweight GTK+ BitTorrent client
# See COPYING. This licensing situation is... special.
License:        MIT and GPL-2.0-only
URL:            http://www.transmissionbt.com

Source0:        https://github.com/transmission/transmission/releases/download/%{version}/transmission-%{version}.tar.xz
# https://bugzilla.redhat.com/show_bug.cgi?id=1221292
Source1:        https://raw.githubusercontent.com/gnome-design-team/gnome-icons/master/apps-symbolic/Adwaita/scalable/apps/transmission-symbolic.svg
# Fix the DBus name to match the app name for flatpak builds
# https://github.com/transmission/transmission/pull/847
Patch0:         0001-gtk-use-com.transmissionbt.Transmission.-D-Bus-names.patch
# Proposed upstream: https://github.com/transmission/transmission/issues/7567
Patch1:         0002-Make-compatible-with-CMake-4.0.patch
Patch2:         7669.patch
Patch3:         144871ed5ec62d9b45f28774923ac83532eb1a2d.patch

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  gtk4-devel
BuildRequires:  gtkmm4.0-devel
BuildRequires:  libcurl-devel >= 7.16.3
BuildRequires:  libevent-devel >= 2.0.10
BuildRequires:  desktop-file-utils
BuildRequires:  gettext intltool
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  systemd-devel
BuildRequires:  libnatpmp-devel >= 20150609-1
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(libpsl)
# unbundled dependencies
BuildRequires:  fast_float-static
#BuildRequires:  fmt-static
BuildRequires:  libb64-static
BuildRequires:  utf8cpp-static
# Default
Requires: transmission-gtk%{?_isa}

%description
Transmission is a free, lightweight BitTorrent client. It features a
simple, intuitive interface on top on an efficient, cross-platform
back-end.

%package common
Summary:       Transmission common files
Provides:      bundled(dht) = 0.27
# remove, unbundle, and BR: fmt-static once ported to fmt-10
Provides:      bundled(fmt) = 9.0.0
Provides:      bundled(libutp) = 3.4
Provides:      bundled(wide-integer)
Provides:      bundled(wildmat)
%description common
Common files for Transmission BitTorrent client sub-packages. It includes
the web user interface, icons and transmission-remote, transmission-create,
transmission-edit, transmission-show utilities.

%package cli
Summary:       Transmission command line implementation
Requires:      transmission-common%{?_isa}
%description cli
Command line version of Transmission BitTorrent client.

%package daemon
Summary:       Transmission daemon
Requires:      transmission-common%{?_isa}
BuildRequires: systemd
%description daemon
Transmission BitTorrent client daemon.

%package gtk
Summary:       Transmission GTK interface
Requires:      transmission-common%{?_isa}
# for canberra-gtk-play
Recommends:    libcanberra-gtk3%{?_isa}

%description gtk
GTK graphical interface of Transmission BitTorrent client.

%package qt
Summary:       Transmission Qt interface
Requires:      transmission-common%{?_isa}
# for canberra-gtk-play
Recommends:    libcanberra-gtk3%{?_isa}

%description qt
Qt graphical interface of Transmission BitTorrent client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# unbundle
pushd third-party
find fast_float/ libb64/ libdeflate/ libevent/ libnatpmp/ libpsl/ \
     utfcpp/ -type f -delete
popd

# fix icon location for Transmission Qt
sed -i 's|Icon=%{name}-qt|Icon=%{name}|g' qt/%{name}-qt.desktop

# convert to UTF encoding
iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new
mv AUTHORS.new AUTHORS

# Create a sysusers.d config file
cat >transmission.sysusers.conf <<EOF
u transmission - 'transmission daemon account' %{_sharedstatedir}/transmission -
EOF

%build

CXXFLAGS="%{optflags} -fPIC"
CFLAGS="%{optflags} -fPIC"

%cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_CLI=ON -DENABLE_QT=ON -DUSE_QT_VERSION=6 -DENABLE_GTK=ON -DUSE_GTK_VERSION=4
%cmake_build

# Re-enable if DhtTest.usesBootstrapFile passes
#%%check
#%%ctest

%install
mkdir -p %{buildroot}%{_unitdir}
install -m0644 redhat-linux-build/daemon/transmission-daemon.service  %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sharedstatedir}/transmission
%cmake_install

mv -f %{buildroot}%{_docdir}/transmission %{buildroot}%{_docdir}/transmission-common

# Install the symbolic icon
mkdir -p  %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps
cp %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/transmission-symbolic.svg

%find_lang %{name} --with-qt
%find_lang %{name}-gtk

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop
desktop-file-install \
                --dir=%{buildroot}%{_datadir}/applications/  \
                  qt/%{name}-qt.desktop

install -m0644 -D transmission.sysusers.conf %{buildroot}%{_sysusersdir}/transmission.conf

%post daemon
%systemd_post transmission-daemon.service

%preun daemon
%systemd_preun transmission-daemon.service

%postun daemon
%systemd_postun_with_restart transmission-daemon.service

%files

%files common
%license COPYING
%doc COPYING AUTHORS README.md news/ rpc-spec.md send-email-when-torrent-done.sh
%{_bindir}/transmission-remote
%{_bindir}/transmission-create
%{_bindir}/transmission-edit
%{_bindir}/transmission-show
%{_datadir}/transmission/public_html/
%{_datadir}/icons/hicolor/*/apps/transmission*.svg
%doc %{_mandir}/man1/transmission-remote*
%doc %{_mandir}/man1/transmission-create*
%doc %{_mandir}/man1/transmission-edit*
%doc %{_mandir}/man1/transmission-show*

%files cli
%{_bindir}/transmission-cli
%doc %{_mandir}/man1/transmission-cli*

%files daemon
%{_bindir}/transmission-daemon
%{_unitdir}/transmission-daemon.service
%attr(-,transmission, transmission)%{_sharedstatedir}/transmission/
%doc %{_mandir}/man1/transmission-daemon*
%{_sysusersdir}/transmission.conf

%files gtk -f %{name}-gtk.lang
%{_bindir}/transmission-gtk
%{_datadir}/metainfo/transmission-gtk.metainfo.xml
%{_datadir}/applications/transmission-gtk.desktop
%doc %{_mandir}/man1/transmission-gtk.*

%files qt -f %{name}.lang
%{_bindir}/transmission-qt
%{_datadir}/applications/transmission-qt.desktop
%doc %{_mandir}/man1/transmission-qt.*

%changelog
%autochangelog
