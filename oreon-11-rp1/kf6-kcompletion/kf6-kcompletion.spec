%global framework kcompletion

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:           kf6-%{framework}
Version:        6.24.0
Release:	5%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon with auto completion widgets and classes
# BSD-3-Clause is in the LICENSES folder but goes unused.
License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Codecs)

%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kcompletion6_qt

%files -f kcompletion6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Completion.so.*
%{_kf6_datadir}/qlogging-categories6/%{framework}.*

%files devel
%{_kf6_includedir}/KCompletion/
%{_kf6_libdir}/libKF6Completion.so
%{_kf6_libdir}/cmake/KF6Completion/
%{_kf6_qtplugindir}/designer/kcompletion6widgets.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

