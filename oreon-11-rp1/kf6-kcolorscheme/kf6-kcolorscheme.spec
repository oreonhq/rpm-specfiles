%global framework kcolorscheme

%global stable_kf6 stable
%global majmin_ver_kf6 6.24


Name:    kf6-%{framework}
Version: 6.24.0
Release:	6%{?dist}
Summary: Classes to read and interact with KColorScheme
License: BSD-2-Clause and CC0-1.0 and LGPL-2.0-or-later and LGPL-2.1-only and LGPL-3.0-only and (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
# oreon url source checksums begin
%global source0_sha256 e9c9e0155e9b8049ad8588049645c998494b91145648467ddcbef178e31e84c5
%global source0_file kcolorscheme-6.24.0.tar.xz
# oreon url source checksums end

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(xkbcommon)

Requires:       kf6-filesystem

%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/kcolorscheme-6.24.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e9c9e0155e9b8049ad8588049645c998494b91145648467ddcbef178e31e84c5" || { echo "oreon: Source0 SHA256 mismatch for kcolorscheme-6.24.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang kcolorscheme6 --all-name

%files -f kcolorscheme6.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/kcolorscheme.categories
%{_kf6_libdir}/libKF6ColorScheme.so.6
%{_kf6_libdir}/libKF6ColorScheme.so.%{version}

%files devel
%{_kf6_includedir}/KColorScheme
%{_kf6_libdir}/cmake/KF6ColorScheme
%{_kf6_libdir}/libKF6ColorScheme.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

