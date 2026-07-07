%global source0_hash a8a0c5103cb43dc62952aab76bb7e576e8643dbb31672e2ac2988279ab571700

%global framework kdesu

%global stable_kf6 stable
%global majmin_ver_kf6 6.27

Name:    kf6-%{framework}
Version: 6.27.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 integration with su

License: CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Pty)
#BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel
Requires:  kf6-filesystem

%if 0%{?rhel} || 0%{?fedora} >= 42
Requires:  sudo
%endif

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Pty)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6 \
%if 0%{?rhel} || 0%{?fedora} >= 42
    -DKDESU_USE_SUDO_DEFAULT:BOOL=TRUE
%endif
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang kdesu6_qt --all-name

%files -f kdesu6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*
%{_kf6_libdir}/libKF6Su.so.*
%{_kf6_libexecdir}/kdesu_stub
%{_kf6_libexecdir}/kdesud

%{_qt6_metatypesdir}/qt6kf6su_metatypes.json
%files devel
%{_kf6_includedir}/KDESu/
%{_kf6_libdir}/libKF6Su.so
%{_kf6_libdir}/cmake/KF6Su/


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

