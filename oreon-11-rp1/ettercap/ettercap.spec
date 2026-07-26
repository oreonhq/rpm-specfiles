%global source0_hash 61276f292628ba081607e8ad1633702cf9c7860eba087a871b1eeec54c769fe2

%global __cmake_in_source_build 1
%define _hardened_build 1
Name: ettercap
Version: 0.8.4
Release: 1%{?dist}
Summary: Network traffic sniffer/analyser, NCURSES interface version
License: GPL-2.0-or-later
URL: http://ettercap.sourceforge.net
Source0: https://github.com/Ettercap/ettercap/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: ettercap.desktop
Source2: ettercap-README.fedora
# Permission from upstream to drop the silly modification restriction
Source3: ettercap_easter_egg_license.txt
Patch1: ettercap-0.8.1-radius-stack-overflow.patch
Patch2: 2168090f5b023573ebea0f83574950401ed5d67b.patch

BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
BuildRequires: gtk3-devel
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: libtool
BuildRequires: bison
BuildRequires: flex
BuildRequires: cmake
BuildRequires: libcurl-devel
BuildRequires: groff-base
BuildRequires: libappstream-glib
#some requirements are available in fedora but not in stock epel
#build for epel requires libnet which is only available from rpmforge
%if 0%{?rhel}
BuildRequires: libnet
#epel 5
BuildRequires: libtool-ltdl-devel
BuildRequires: libpcap-devel
%endif
%if 0%{?fedora}
BuildRequires: libpcap-devel
BuildRequires: libnet-devel
BuildRequires: libtool-ltdl-devel
%endif
BuildRequires: make
Requires: polkit ethtool

%description
Ettercap is a suite for man in the middle attacks on LAN. It features
sniffing of live connections, content filtering on the fly and many other
interesting tricks. It supports active and passive dissection of many
protocols (even ciphered ones) and includes many feature for network and host
analysis. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 1 -p1
%patch -P 2 -p1

%build
mkdir build
pushd build
%cmake ../ -DINSTALL_PREFIX=/usr -DMAN_INSTALLDIR=%{_mandir} -DINSTALL_LIBDIR=%{_libdir} -DENABLE_IPV6=yes -DENABLE_GEOIP=no -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
mkdir -p  %{buildroot}%{_bindir}
pushd build
%cmake_install
#make install DESTDIR=%{buildroot}
#make install man DESTDIR=%{buildroot}
#getting rid of libtool files potentially left behind when building plugins
rm -f %{buildroot}%{_libdir}/ettercap/*.la
mkdir -p %{buildroot}%{_docdir}
install -c -m 644 %{SOURCE2} %{buildroot}%{_docdir}
install -c -m 644 %{SOURCE3} %{buildroot}%{_docdir}
touch %{buildroot}%{_bindir}/ettercap

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 ../share/ettercap.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
rm -f ettercap*png

popd
install -c -m 644 desktop/ettercap.appdata.xml %{buildroot}%{_metainfodir}/ettercap.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS CHANGELOG THANKS TODO* README.md doc/
%{_bindir}/etter*
%config(noreplace) %{_sysconfdir}/ettercap/
%{_docdir}/ettercap-README.fedora
%{_docdir}/ettercap_easter_egg_license.txt
%{_mandir}/man5/etter*
%{_mandir}/man8/etter*
%{_datadir}/ettercap/
%{_libdir}/ettercap/
%{_libdir}/libettercap.so.0*
%{_libdir}/libettercap.so
%{_libdir}/libettercap-ui.so.0*
%{_libdir}/libettercap-ui.so
%{_datadir}/applications/ettercap.desktop
%{_datadir}/icons/hicolor/32x32/apps/ettercap.png
%{_datadir}/icons/hicolor/scalable/apps/ettercap.svg
%{_datadir}/polkit-1/actions/org.pkexec.ettercap.policy
%{_metainfodir}/ettercap.appdata.xml
%{_metainfodir}/ettercap.metainfo.xml

%changelog
%autochangelog
