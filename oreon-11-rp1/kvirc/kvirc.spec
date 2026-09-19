%global source0_hash 6b448b08aeaf5fd3f2b120525c8c87ddad3336f5b750a557b2022aaad0dda626

Name:             kvirc
Version:          5.2.10
Release:          2%{?dist}
Summary:          Free portable IRC client
License:          GPL-2.0-or-later WITH kvirc-openssl-exception
URL:              https://www.kvirc.net/
%global forgeurl  https://github.com/kvirc/KVIrc
Source:           %{forgeurl}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
Patch:            kvirc-5.0.0_enforce_system_crypto.patch

BuildRequires:    enchant2-devel
BuildRequires:    audiofile-devel
BuildRequires:    glib2-devel
BuildRequires:    perl-devel
BuildRequires:    perl-ExtUtils-Embed
BuildRequires:    python3-devel
BuildRequires:    cmake3
BuildRequires:    ninja-build
BuildRequires:    extra-cmake-modules
BuildRequires:    desktop-file-utils
BuildRequires:    gettext
BuildRequires:    doxygen
BuildRequires:    graphviz
BuildRequires:    libtheora-devel
BuildRequires:    libvorbis-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    cmake(KF6CoreAddons)
BuildRequires:    cmake(KF6I18n)
BuildRequires:    cmake(KF6KIO)
BuildRequires:    cmake(KF6Notifications)
BuildRequires:    cmake(KF6Parts)
BuildRequires:    cmake(KF6Service)
BuildRequires:    cmake(KF6StatusNotifierItem)
BuildRequires:    cmake(KF6WindowSystem)
BuildRequires:    cmake(KF6XmlGui)
BuildRequires:    cmake(Phonon4Qt6)
BuildRequires:    cmake(Qt6Concurrent)
BuildRequires:    cmake(Qt6Core)
BuildRequires:    cmake(Qt6Core5Compat)
BuildRequires:    cmake(Qt6DBus)
BuildRequires:    cmake(Qt6Multimedia)
BuildRequires:    cmake(Qt6Network)
BuildRequires:    cmake(Qt6PrintSupport)
BuildRequires:    cmake(Qt6Sql)
BuildRequires:    cmake(Qt6Svg)
BuildRequires:    cmake(Qt6Widgets)
BuildRequires:    cmake(Qt6Xml)
%ifarch %{?qt6_qtwebengine_arches}
BuildRequires:    cmake(Qt6WebEngineWidgets)
%endif

%description
KVIrc is a free portable IRC client based on the excellent
Qt GUI toolkit. KVirc is being written by Szymon Stefanek
and the KVIrc Development Team with the contribution of
many IRC addicted developers around the world.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n KVIrc-%{version}

%build
%{cmake3}  \
-GNinja \
-DCMAKE_SKIP_RPATH=ON \
-DQT_VERSION_MAJOR=6 \
-DWANT_ENV_FLAGS=ON \
-DWANT_DCC_VIDEO=OFF \
-DWANT_OGG_THEORA=ON \
-DWANT_GTKSTYLE=ON \
-DADDITIONAL_LINK_FLAGS='-Wl,--as-needed' \
%if "%{?_lib}" == "lib64"
%{?_cmake_lib_suffix64} \
%endif
%{nil}

%cmake_build

%install
%cmake_install

desktop-file-validate \
    %{buildroot}%{_datadir}/applications/net.kvirc.KVIrc5.desktop

ln -sf ../../%{name}/5.2/license/COPYING COPYING

# Delete zero length file
rm %{buildroot}%{_datadir}/kvirc/5.2/help/en/_db_widget.idx

rm %{buildroot}%{_bindir}/kvirc-config
rm %{buildroot}%{_libdir}/libkvilib.so

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc RELEASES
%{_bindir}/%{name}
%{_libdir}/libkvilib.so.5*
%{_datadir}/applications/net.kvirc.KVIrc5.desktop
%{_libdir}/%{name}/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/5.2
%dir %{_datadir}/%{name}/5.2/locale
%{_datadir}/%{name}/5.2/audio/
%{_datadir}/%{name}/5.2/config/
%{_datadir}/%{name}/5.2/defscript/
%{_datadir}/%{name}/5.2/help/
%{_datadir}/%{name}/5.2/modules/
%{_datadir}/%{name}/5.2/msgcolors/
%{_datadir}/%{name}/5.2/pics/
%{_datadir}/%{name}/5.2/themes/
%{_datadir}/%{name}/5.2/license/
%{_datadir}/icons/hicolor/*/apps/kvirc.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-kva.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-kvt.*
%{_datadir}/icons/hicolor/*/mimetypes/text-x-kvc.*
%{_datadir}/icons/hicolor/*/mimetypes/text-x-kvs.*
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.gz

# Translation files
%lang(de) %{_mandir}/de/man1/%{name}.1.gz
%lang(fr) %{_mandir}/fr/man1/%{name}.1.gz
%lang(it) %{_mandir}/it/man1/%{name}.1.gz
%lang(pt) %{_mandir}/pt/man1/%{name}.1.gz
%lang(uk) %{_mandir}/uk/man1/%{name}.1.gz

%changelog
%autochangelog
