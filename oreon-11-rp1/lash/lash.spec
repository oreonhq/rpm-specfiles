%global source0_hash 105a7da84415c4725c6bcad28e70f23aeb4534f94fc80ca262b6a2cef2226c16
Summary:        LASH Audio Session Handler
Name:         lash
Version:      0.5.4
Release:        58%{?dist}
License:      GPL-2.0-or-later
URL:          http://www.nongnu.org/lash/
Source0:        http://download.savannah.gnu.org/releases/lash/lash-%{version}.tar.gz
Source1:      %{name}-panel.desktop
Patch0:       lash-0.5.3-no-static-lib.patch
Patch1:       lash-linking.patch
Patch2:       lash-gcc47.patch
Patch3:       lash-Modernize-texi2html-arguments.patch
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  texi2html
# /oreon:deps
%description
LASH is a session management system for JACK and ALSA audio applications on
GNU/Linux. It allows you to save and restore audio sessions consisting of
multiple interconneced applications, restoring program state (i.e. loaded
patches) and the connections between them.

%package devel
Summary:      Development files for LASH
Requires:     %{name}-libs%{?_isa} = %{version}-%{release}
Requires:     alsa-lib-devel
Requires:     jack-audio-connection-kit-devel
Requires:     libuuid-devel
%description devel
Development files for the LASH library.

%package        libs
Summary:        Shared libraries for using %{name}
%description    libs
The %{name}-libs package contains lash shared libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p1 -b .linking
%patch -P2 -p1 -b .gcc47
%patch -P3 -p1 -b .texi2html

# Hack to build against newer swig
sed -i 's|1.3.31|4.0.0|g' configure*

%build

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -std=gnu17" %configure --disable-static --disable-serv-inst
%make_build
%install
mkdir -p %{buildroot}%{_sysconfdir}
%make_install
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/liblash.la
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/96x96/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/lash/icons/lash_16px.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_24px.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_48px.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_96px.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/lash.svg
chrpath --delete %{buildroot}%{_bindir}/lash_control
chrpath --delete %{buildroot}%{_bindir}/lash_simple_client
chrpath --delete %{buildroot}%{_bindir}/lashd
chrpath --delete %{buildroot}%{_bindir}/lash_synth
chrpath --delete %{buildroot}%{_bindir}/lash_panel
chrpath --delete %{buildroot}%{_bindir}/lash_save_button
mkdir -p %{buildroot}%{_datadir}/xml/lash/dtds
mv %{buildroot}%{_datadir}/lash/dtds/lash-project-1.0.dtd %{buildroot}%{_datadir}/xml/lash/dtds
rm -rf %{buildroot}%{_datadir}/lash
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                         \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
if [ ! -d docs/lash-manual-html-split/lash-manual/ ]; then
  mkdir -p docs/lash-manual-html-split/lash-manual/
  cp -p docs/lash-manual-html-split/*.html docs/lash-manual-html-split/lash-manual/
fi
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lash-devel -f %{oreon_filedir}/lash-devel.list
%files -n lash-libs -f %{oreon_filedir}/lash-libs.list

%changelog

%autochangelog
