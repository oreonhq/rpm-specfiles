%global source0_hash 6ef59a01e71c8a2a7051e4572b255cd7358a64debc22fdcd18b29f98b7cc633c
%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%global framework baloo
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Summary:        A Tier 3 KDE Frameworks 5 module that provides indexing and search functionality
Version: 5.116.0
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND LGPL-3.0-or-later
URL:     https://community.kde.org/Baloo
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Source1:        97-kde-baloo-filewatch-inotify.conf
Source2:        baloo_file_shutdown.sh
Patch100: baloo-5.67.0-baloofile_config.patch
%if 0%{?tests}
%endif
Obsoletes:      kf5-baloo-tools < 5.5.95-1
Provides:       kf5-baloo-tools = %{version}-%{release}
Conflicts:      baloo < 5
Obsoletes:      kf5-baloo < 5.21.0-4
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kfilemetadata-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-solid-devel
BuildRequires:  lmdb-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  systemd
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
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
License:        LGPLv2 or LGPLv3
Conflicts:      baloo-file < 5
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    file
%{summary}.
%endif

%package        libs
Summary:        Runtime libraries for %{name}
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
cat kio5_tags.lang kio5_baloosearch.lang kio5_timeline.lang \
    balooctl5.lang balooengine5.lang baloosearch5.lang \
    balooshow5.lang \
    > %{name}.lang
cat baloo_file5.lang baloo_file_extractor5.lang \
    > %{name}-file.lang
%if %{with kf6_compat}
cat %{name}-file.lang | xargs printf "%{buildroot}%.0s%s\n" | xargs rm
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif
%files -f %{oreon_filedir}/main.list
%files -n kf5-baloo-devel -f %{oreon_filedir}/kf5-baloo-devel.list
%files -n kf5-baloo-libs -f %{oreon_filedir}/kf5-baloo-libs.list

%changelog

%autochangelog
