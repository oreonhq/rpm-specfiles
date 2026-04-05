%global framework kdoctools

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release:	7%{?dist}
Summary: KDE Frameworks 6 Tier 2 addon for generating documentation

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Any::URI::Escape)
BuildRequires:  qt6-qtbase-devel
Requires:       docbook-dtds
Requires:       docbook-style-xsl

%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-kdoctools-static = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       perl(Any::URI::Escape)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name --with-man --with-html

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6DocTools.so.6
%{_kf6_libdir}/libKF6DocTools.so.%{version}
%{_kf6_bindir}/checkXML6
%{_kf6_bindir}/meinproc6
%{_kf6_mandir}/man1/*.1*
%{_kf6_mandir}/man7/*.7*
%{_kf6_datadir}/kf6/kdoctools/

%files devel
%{_kf6_includedir}/KDocTools/
%{_kf6_libdir}/libKF6DocTools.so
%{_kf6_libdir}/cmake/KF6DocTools/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-2
- Prepare for Oreon 11 (RP1)

