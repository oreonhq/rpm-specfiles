%global source1_hash 3d318f2c3cc35acea589bf09fa26b40e6e53885359a062cace71d27f8ef61291
%global source0_hash a59d33a919bfa1d164c8f3a6f992c609edaf2131ac5f52ea4ecb77f6fbc53be1
%global framework baloo
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Summary:        A Tier 3 KDE Frameworks 6 module that provides indexing and search functionality
Version: 6.30.0
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND bzip2-1.0.6
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Patch100: baloo-5.67.0-baloofile_config.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  lmdb-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  systemd
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6FileMetaData)
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        file
Summary:        File indexing and search for Baloo
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kf5-baloo-file < 6
%description    file
%{summary}.

%package        libs
Summary:        Runtime libraries for %{name}
%description    libs
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6 \
    -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir}
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang baloodb6
%find_lang baloo_file6
%find_lang baloo_file_extractor6
%find_lang balooctl6
%find_lang balooengine6
%find_lang baloosearch6
%find_lang balooshow6
%find_lang kio6_baloosearch
%find_lang kio6_tags
%find_lang kio6_timeline
cat kio6_tags.lang kio6_baloosearch.lang kio6_timeline.lang \
    balooctl6.lang balooengine6.lang baloosearch6.lang \
    balooshow6.lang baloodb6.lang \
    > %{name}.lang
cat baloo_file6.lang baloo_file_extractor6.lang \
    > %{name}-file.lang
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-baloo-devel -f %{oreon_filedir}/kf6-baloo-devel.list
%files -n kf6-baloo-file -f %{oreon_filedir}/kf6-baloo-file.list
%files -n kf6-baloo-libs -f %{oreon_filedir}/kf6-baloo-libs.list

%changelog

%autochangelog
