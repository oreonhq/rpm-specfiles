%global source0_hash 446c4b479f832e0a61106c73e7c9732f1fa82b4c359c5d6130e698afcf0e6cbe

%undefine __cmake_in_source_build

# https://github.com/vacuum-im/vacuum-im/commit/0abd5e11dd3e2538b8c47f5a06febedf73ae99ee
%global         commit 0abd5e11dd3e2538b8c47f5a06febedf73ae99ee
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
%global         commitdate 20211209
%global         sname vacuum

Name:           %{sname}-im
Summary:        XMPP/Jabber client
Version:        1.3.0
Release:        0.35.%{commitdate}git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
Url:            http://www.vacuum-im.org/
Source0:        https://github.com/Vacuum-IM/vacuum-im/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-fix-building-with-qt5.5.patch
Patch1:         %{name}-fix-type-mismatch.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(qxtglobalshortcut)
BuildRequires:  qtlockedfile-qt5-devel
BuildRequires:  chrpath
BuildRequires:  openssl-devel
BuildRequires:  hunspell-devel
BuildRequires:  libidn-devel
BuildRequires:  jdns-devel
BuildRequires:  zlib-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:      %{name}-data = %{version}
Requires:       fedora-logos
Requires:       hicolor-icon-theme

%description
Full-featured cross platform Jabber/XMPP client.
The core program is just a plugin loader - all functionality is made
available via plugins. This enforces modularity and ensures well defined
component interaction via interfaces.

%package data
Summary:       Images, themes and translatons for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description data
This package contains images, themes and translations.

%package devel
Summary:  Development Files for Vacuum-IM
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes files needed to develop Vacuum-IM modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{commit}
#%%patch0 -p0

# Fix W: wrong-file-end-of-line-encoding /usr/share/doc/vacuum-im/AUTHORS
sed -i 's/\r$//' AUTHORS CHANGELOG README TRANSLATORS

# Fix W: spurious-executable-perm
chmod a-x src/plugins/spellchecker/{spellchecker,spellbackend}.cpp

# delete bundled qxtglobalshortcut sources
rm -rf src/thirdparty/qxtglobalshortcut

# delete bundled zlib sources
rm -rf src/thirdparty/zlib

%build
%cmake \
          -DINSTALL_LIB_DIR=%{_lib} \
          -DINSTALL_APP_DIR=%{name} \
          -DLFLAGS="${RPM_LD_FLAGS} -Wl,--as-needed" \
          -DCFLAGS="%{optflags}"    \
          -DCXXFLAGS="%{optflags}"

%cmake_build

%install
%cmake_install
install -D -m644 resources/menuicons/shared/mainwindowlogo128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo96.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
sed -i "s/Exec=%{sname}/Exec=%{name}/;s/Icon=%{sname}/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{sname}.desktop
mv %{buildroot}%{_datadir}/applications/%{sname}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_datadir}/pixmaps/%{sname}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mv %{buildroot}%{_bindir}/%{sname} %{buildroot}%{_bindir}/%{name}

find %{buildroot}%{_datadir}/%{name}/translations -name "*.qm" | sed 's:'%{buildroot}'::
s:.*/\([a-zA-Z]\{2\}\).qm:%lang(\1) \0:' > %{name}.lang

rm -f %{buildroot}%{_defaultdocdir}/%{name}/COPYING
rm -f %{buildroot}%{_datadir}/%{name}/resources/adiummessagestyles/renkoo/Contents/Resources/*LICENSE.txt

# Remove rpath E: binary-or-shlib-defines-rpath /usr/bin/vacuum-im ['$ORIGIN', '$ORIGIN/../lib64/']
chrpath --delete %{buildroot}%{_bindir}/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml

%files -f %{name}.lang
%doc CHANGELOG AUTHORS README TRANSLATORS
%license COPYING
%license resources/adiummessagestyles/renkoo/Contents/Resources/*LICENSE.txt
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/plugins
%{_libdir}/libvacuumutils.so.*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/pixmaps/%{name}.png

%files data
%{_datadir}/%{name}

%files devel
%{_libdir}/libvacuumutils.so
%{_includedir}/%{name}

%changelog
%autochangelog
