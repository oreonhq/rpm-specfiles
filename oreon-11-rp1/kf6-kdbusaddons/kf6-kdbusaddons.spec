%global source0_hash 9ea3792b2f1c43d5551437260803fdd676c903e2768f4aac4186054e5b22d4ca

%global framework	kdbusaddons

%global stable_kf6 stable
%global majmin_ver_kf6 6.27

Name:			kf6-%{framework}
Version:		6.27.0
Release:        1%{?dist}
Summary:		KDE Frameworks 6 Tier 1 addon with various classes on top of QtDBus
License:		CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:			https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:		extra-cmake-modules >= %{version}
BuildRequires:		kf6-rpm-macros
BuildRequires:		cmake
BuildRequires:		gcc-c++
BuildRequires:		qt6-qtbase-devel
BuildRequires:		qt6-qttools-devel
BuildRequires:          qt6-qtbase-private-devel
BuildRequires:		pkgconfig(xkbcommon)

Requires:		kf6-filesystem

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		qt6-qtbase-devel
%description		devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 kdbusaddons6_qt

%files -f kdbusaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_bindir}/kquitapp6
%{_kf6_libdir}/libKF6DBusAddons.so.*

%{_qt6_metatypesdir}/qt6kf6dbusaddons_metatypes.json
%files devel
%{_kf6_includedir}/KDBusAddons/
%{_kf6_libdir}/libKF6DBusAddons.so
%{_kf6_libdir}/cmake/KF6DBusAddons/


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

