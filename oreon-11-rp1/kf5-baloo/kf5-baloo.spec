%global source0_hash 6ef59a01e71c8a2a7051e4572b255cd7358a64debc22fdcd18b29f98b7cc633c

%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

%global framework baloo

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Summary: A Tier 3 KDE Frameworks 5 module that provides indexing and search functionality
Version: 5.116.0
Release: 5%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND LGPL-3.0-or-later
URL:     https://community.kde.org/Baloo
#URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

Source1:        97-kde-baloo-filewatch-inotify.conf
# shutdown script to explictly stop baloo_file on logout
# Now that baloo supports systemd user unit, this can probably be dropped -- rex
Source2:        baloo_file_shutdown.sh

## upstreamable patches
# http://bugzilla.redhat.com/1235026
Patch100: baloo-5.67.0-baloofile_config.patch

## upstream patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kcrash-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kfilemetadata-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kidletime-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  kf5-solid-devel >= %{majmin}

BuildRequires:  lmdb-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

# for systemd-related macros
BuildRequires:  systemd

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Obsoletes:      kf5-baloo-tools < 5.5.95-1
Provides:       kf5-baloo-tools = %{version}-%{release}

%if 0%{?fedora}
Obsoletes:      baloo < 5
Provides:       baloo = %{version}-%{release}
%else
Conflicts:      baloo < 5
%endif

# main pkg accidentally multilib'd prior to 5.21.0-4
Obsoletes:      kf5-baloo < 5.21.0-4

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
# KDE e.V. may determine that future LGPL versions are accepted
License:        LGPLv2 or LGPLv3
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel >= %{majmin}
Requires:       kf5-kfilemetadata-devel >= %{majmin}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{without kf6_compat}
%package        file
Summary:        File indexing and search for Baloo
# KDE e.V. may determine that future LGPL versions are accepted
License:        LGPLv2 or LGPLv3
%if 0%{?fedora}
Obsoletes:      baloo-file < 5.0.1-2
Provides:       baloo-file = %{version}-%{release}
%else
Conflicts:      baloo-file < 5
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    file
%{summary}.
%endif

%package        libs
Summary:        Runtime libraries for %{name}
# KDE e.V. may determine that future LGPL versions are accepted
License:        LGPLv2 or LGPLv3
%description    libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  %{?with_kf6_compat:-DBUILD_INDEXER_SERVICE=OFF}
%cmake_build

%install
%cmake_install

%if 0%{?flatpak:1}
find %{buildroot} -name kde-baloo.service -delete
%endif

# baloodb not installed unless BUILD_EXPERIMENTAL is enabled, so omit translations
rm -fv %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/baloodb5.*

%if %{without kf6_compat}
install -p -m644 -D %{SOURCE1} %{buildroot}%{_prefix}/lib/sysctl.d/97-kde-baloo-filewatch-inotify.conf
install -p -m755 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/shutdown/baloo_file.sh
%endif

%find_lang kio5_baloosearch
%find_lang kio5_tags
%find_lang kio5_timeline
%find_lang balooctl5
%find_lang balooengine5
%find_lang baloosearch5
%find_lang balooshow5
%find_lang baloo_file5
%find_lang baloo_file_extractor5
#find_lang baloomonitorplugin

cat kio5_tags.lang kio5_baloosearch.lang kio5_timeline.lang \
    balooctl5.lang balooengine5.lang baloosearch5.lang \
    balooshow5.lang \
    > %{name}.lang

cat baloo_file5.lang baloo_file_extractor5.lang \
    > %{name}-file.lang

%if %{with kf6_compat}
cat %{name}-file.lang | xargs printf "%{buildroot}%.0s%s\n" | xargs rm
%endif

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif

%files -f %{name}.lang
%license LICENSES/*.txt
#{_kf5_bindir}/baloodb
%{_kf5_bindir}/baloosearch
%{_kf5_bindir}/balooshow
%if %{without kf6_compat}
%{_kf5_bindir}/balooctl
%endif
%{_kf5_datadir}/qlogging-categories5/%{framework}*

%if %{without kf6_compat}
%files file -f %{name}-file.lang
%{_prefix}/lib/sysctl.d/97-kde-baloo-filewatch-inotify.conf
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/shutdown/baloo_file.sh
%{_kf5_bindir}/baloo_file
%{_kf5_bindir}/baloo_file_extractor
%config(noreplace) %{_kf5_sysconfdir}/xdg/autostart/baloo_file.desktop
%if ! 0%{?flatpak:1}
%{_userunitdir}/kde-baloo.service
%endif
%{_libexecdir}/baloo_file
%{_libexecdir}/baloo_file_extractor
%endif

%ldconfig_scriptlets libs

%files libs
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5Baloo.so.*
%{_kf5_libdir}/libKF5BalooEngine.so.*
# multilib'd plugins and friends
%{_kf5_plugindir}/kio/baloosearch.so
%{_kf5_plugindir}/kio/tags.so
%{_kf5_plugindir}/kio/timeline.so
%{_kf5_plugindir}/kded/baloosearchmodule.so
%{_kf5_qmldir}/org/kde/baloo

%files devel
%{_kf5_libdir}/libKF5Baloo.so
%{_kf5_libdir}/cmake/KF5Baloo/
%{_kf5_libdir}/pkgconfig/Baloo.pc
%{_kf5_includedir}/Baloo/

%{_kf5_archdatadir}/mkspecs/modules/qt_Baloo.pri
%if %{without kf6_compat}
%{_kf5_datadir}/dbus-1/interfaces/org.kde.baloo.*.xml
%{_kf5_datadir}/dbus-1/interfaces/org.kde.Baloo*.xml
%endif

%changelog
%autochangelog
