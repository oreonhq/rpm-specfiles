%global source0_hash 513051dff8417da1819d6ae89d6c21a03654c9a60891df60df6aba13df19d21b

%global framework kirigami-addons
%global orig_name kirigami-addons

%ifarch aarch64
%global _lto_cflags %{nil}
%global _smp_mflags -j2
%endif

Name:           kf6-%{framework}
Version:        1.12.0
Release:	6%{?dist}
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND LicenseRef-KFQF-Accepted-GPL
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/%{framework}
Source:        https://download.kde.org/stable/%{framework}/%{framework}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)

# Doesn't need qtbase-private-devel, but private stuff from qtdeclarative
# so we still need to rebuild it
#BuildRequires: qt6-qtbase-private-devel

Requires: kf6-filesystem

### Renamed from kf6-kirigami2-addons (which was at epoch 1)
Obsoletes: kf6-kirigami2-addons < 1:0.11.76-5
Provides:  kf6-kirigami2-addons = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons%{?_isa} = 1:%{version}-%{release}

### Merged subpackages back into main package
# The old name
Obsoletes: kf6-kirigami2-addons-dateandtime < 1:0.11.76-5
Provides:  kf6-kirigami2-addons-dateandtime = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-dateandtime%{?_isa} = 1:%{version}-%{release}

Obsoletes: kf6-kirigami2-addons-treeview < 1:0.11.76-5
Provides:  kf6-kirigami2-addons-treeview = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-treeview%{?_isa} = 1:%{version}-%{release}

# The new name
Obsoletes: kf6-kirigami-addons-dateandtime < 0.11.76-5
Provides:  kf6-kirigami-addons-dateandtime = %{version}-%{release}
Provides:  kf6-kirigami-addons-dateandtime%{?_isa} = %{version}-%{release}

Obsoletes: kf6-kirigami-addons-treeview < 0.11.76-5
Provides:  kf6-kirigami-addons-treeview = %{version}-%{release}
Provides:  kf6-kirigami-addons-treeview%{?_isa} = %{version}-%{release}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package   devel
Summary:   Development files for %{name}
Requires:  %{name} = %{version}-%{release}
Conflicts: kf6-kirigami-addons < 1.4.0
%description devel
The %{name}-devel package contains CMake definitions, libraries
and header files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version}

%build
%cmake_kf6 \
    -DBUILD_WITH_QT6=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose

%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{orig_name}6 --all-name

%files -f %{orig_name}6.lang
%doc README.md
%license LICENSES/
%dir %{_kf6_qmldir}/org/kde
%{_kf6_qmldir}/org/kde/kirigamiaddons
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so.{6,%{version}}
%{_kf6_libdir}/libKirigamiApp.so.%{version}
%{_kf6_libdir}/libKirigamiApp.so.6
%{_kf6_libdir}/libKirigamiAddonsComponents.so.%{version}
%{_kf6_libdir}/libKirigamiAddonsComponents.so.6

%files devel
%{_kf6_libdir}/libKirigamiAddonsComponents.so
%{_kf6_libdir}/libKirigamiApp.so
%{_includedir}/KirigamiAddons/
%{_kf6_libdir}/cmake/KF6KirigamiAddons
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so
%{_includedir}/KirigamiAddonsStatefulApp/
%{_kf6_datadir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2
%{_kf6_datadir}/kdevappwizard/templates/librarymanager6.tar.bz2

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12.0-6
- bump release (retry failed build)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12.0-5
- define %%orig_name for %%find_lang (broken %%install when empty)
- aarch64: no LTO, -j2 to reduce OOM risk

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Use kf6 cmake build/install macros (avoid qt6 prepare_docs / install_html_docs)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12.0-1
- Prepare for Oreon 11 (RP1)
