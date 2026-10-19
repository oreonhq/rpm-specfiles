%global source0_hash 04bc07943f24f2f804f3bfe8852cce53982318d37e6b1eaf7beea550498ac042
%global __cmake_in_source_build 1
%define _hardened_build 1
Name: ettercap
Version: 0.8.4.1
Release:        1%{?dist}
Summary:        Network traffic sniffer/analyser, NCURSES interface version
License: GPL-2.0-or-later
URL: http://ettercap.sourceforge.net
Source0:        https://github.com/Ettercap/ettercap/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: ettercap.desktop
Source2: ettercap-README.fedora
Source3: ettercap_easter_egg_license.txt
Patch1: ettercap-0.8.1-radius-stack-overflow.patch
Patch2: 2168090f5b023573ebea0f83574950401ed5d67b.patch
Requires: polkit ethtool
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  groff-base
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
