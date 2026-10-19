%global source0_hash 6b448b08aeaf5fd3f2b120525c8c87ddad3336f5b750a557b2022aaad0dda626
Name:             kvirc
Version:          5.2.10
Release:        2%{?dist}
Summary:        Free portable IRC client
License:          GPL-2.0-or-later WITH kvirc-openssl-exception
URL:              https://www.kvirc.net/
%global forgeurl  https://github.com/kvirc/KVIrc
Source0:        %{forgeurl}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Patch:            kvirc-5.0.0_enforce_system_crypto.patch
%ifarch %{?qt6_qtwebengine_arches}
%endif
# oreon:deps
BuildRequires:  audiofile-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  enchant2-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  graphviz
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  perl-ExtUtils-Embed
BuildRequires:  perl-devel
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
KVIrc is a free portable IRC client based on the excellent
Qt GUI toolkit. KVirc is being written by Szymon Stefanek
and the KVIrc Development Team with the contribution of
many IRC addicted developers around the world.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir KVIrc-%{version}
%oreon_prep
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
rm %{buildroot}%{_datadir}/kvirc/5.2/help/en/_db_widget.idx
rm %{buildroot}%{_bindir}/kvirc-config
rm %{buildroot}%{_libdir}/libkvilib.so
%find_lang %{name} --all-name
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
