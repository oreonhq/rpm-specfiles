%global source0_hash ec5943b4d7efdc18c506ea0db543acdcd5313452615c66d72a1d5ff8d428296a

%global framework kirigami

%global stable_kf6 stable
%global majmin_ver_kf6 6.29


Name:           kf6-%{framework}
Version:        6.29.0
Release:        1%{?dist}
Summary:        QtQuick plugins to build user interfaces based on the KDE UX guidelines
License:        BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# -- UPSTREAM --

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6ShaderTools)

# Renamed from kf6-kirigami2
Obsoletes:      kf6-kirigami2 < 5.246.0
Provides:       kf6-kirigami2 = %{version}-%{release}
Provides:       kf6-kirigami2%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Obsoletes:      kf6-kirigami2-devel < 5.246.0
Provides:       kf6-kirigami2-devel = %{version}-%{release}
Provides:       kf6-kirigami2-devel%{?_isa} = %{version}-%{release}
%description    devel
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
%find_lang_kf6 libkirigami6_qt

%files -f libkirigami6_qt.lang
%doc README.md
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%license LICENSES/*.txt
%{_kf6_qmldir}/org/kde/kirigami
%{_datadir}/qlogging-categories6/kirigami.categories
%{_kf6_libdir}/libKirigami.so.6
%{_kf6_libdir}/libKirigami.so.%{version}
%{_kf6_libdir}/libKirigamiDelegates.so.6
%{_kf6_libdir}/libKirigamiDelegates.so.%{version}
%{_kf6_libdir}/libKirigamiDialogs.so.6
%{_kf6_libdir}/libKirigamiDialogs.so.%{version}
%{_kf6_libdir}/libKirigamiLayouts.so.6
%{_kf6_libdir}/libKirigamiLayouts.so.%{version}
%{_kf6_libdir}/libKirigamiLayoutsPrivate.so.6
%{_kf6_libdir}/libKirigamiLayoutsPrivate.so.%{version}
%{_kf6_libdir}/libKirigamiPlatform.so.6
%{_kf6_libdir}/libKirigamiPlatform.so.%{version}
%{_kf6_libdir}/libKirigamiPrimitives.so.6
%{_kf6_libdir}/libKirigamiPrimitives.so.%{version}
%{_kf6_libdir}/libKirigamiPrivate.so.6
%{_kf6_libdir}/libKirigamiPrivate.so.%{version}
%{_kf6_libdir}/libKirigamiPolyfill.so.6
%{_kf6_libdir}/libKirigamiPolyfill.so.%{version}
%{_kf6_libdir}/libKirigamiTemplates.so.6
%{_kf6_libdir}/libKirigamiTemplates.so.%{version}
%{_kf6_libdir}/libKirigamiControls.so.6
%{_kf6_libdir}/libKirigamiControls.so.%{version}
%{_kf6_libdir}/libKirigamiForms.so.6
%{_kf6_libdir}/libKirigamiForms.so.%{version}
%{_kf6_libdir}/libKirigamiFormsPrivateTemplates.so.6
%{_kf6_libdir}/libKirigamiFormsPrivateTemplates.so.%{version}
%{_kf6_libdir}/libKirigamiFormsPrivateFlat.so.6
%{_kf6_libdir}/libKirigamiFormsPrivateFlat.so.%{version}
%{_kf6_libdir}/libKirigamiFormsPrivateCards.so.6
%{_kf6_libdir}/libKirigamiFormsPrivateCards.so.%{version}

%{_qt6_metatypesdir}/qt6kirigamiplatform_metatypes.json
%files devel
%dir %{_kf6_datadir}/kdevappwizard/
%dir %{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_datadir}/kdevappwizard/templates/kirigami6.tar.bz2
%{_kf6_includedir}/Kirigami/
%{_kf6_libdir}/cmake/KF6Kirigami{,2}/
%{_kf6_libdir}/cmake/KF6KirigamiPlatform/
%{_kf6_libdir}/libKirigami.so
%{_kf6_libdir}/libKirigamiDelegates.so
%{_kf6_libdir}/libKirigamiDialogs.so
%{_kf6_libdir}/libKirigamiLayouts.so
%{_kf6_libdir}/libKirigamiLayoutsPrivate.so
%{_kf6_libdir}/libKirigamiPlatform.so
%{_kf6_libdir}/libKirigamiPrimitives.so
%{_kf6_libdir}/libKirigamiPrivate.so
%{_kf6_libdir}/libKirigamiPolyfill.so
%{_kf6_libdir}/libKirigamiTemplates.so
%{_kf6_libdir}/libKirigamiControls.so
%{_kf6_libdir}/libKirigamiForms.so
%{_kf6_libdir}/libKirigamiFormsPrivateTemplates.so
%{_kf6_libdir}/libKirigamiFormsPrivateFlat.so
%{_kf6_libdir}/libKirigamiFormsPrivateCards.so


%changelog
* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.29.0-1
- Latest upstream release

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-9
- bump release (retry failed build)

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-8
- sort changelog so newer dates are above older (Sat Apr 04 before Fri Apr 03)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-7
- inline cmake --build (no qt6 prepare_docs pass)
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)
- Qt6 qdoc: -html file list via find, tags/index in -devel
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-7
- BR cmake(Qt6LinguistTools) for ecm_install_po_files_as_qm (fixes x86_64 configure)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

