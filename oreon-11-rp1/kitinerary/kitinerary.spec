Name:    kitinerary
Version: 25.12.3
Release:	2%{?dist}
Summary: A library containing itinerary data model and itinerary extraction code

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND ODbL-1.0
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:   %{ix86}
%endif

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kpublictransport
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  cmake(ZXing)
BuildRequires:  cmake(KF6I18n)

# kde-pim pkgs
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Archive)

# kde-pim cmake
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KPim6PkPass)

BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Qml)

BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler)
%if 0%{?fedora}
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel
%endif
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  osmctools

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Mime)
Requires:       cmake(KPim6PkPass)
Requires:       cmake(KF6CalendarCore)
Requires:       cmake(KF6Contacts)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Itinerary.so.*
%{_libexecdir}/kf6/kitinerary-extractor
%{_kf6_datadir}/mime/packages/application-vnd-kde-itinerary.xml

%files devel
%{_includedir}/KPim6/kitinerary/
%{_includedir}/KPim6/KItinerary/
%{_includedir}/KPim6/kitinerary_version.h
%{_kf6_libdir}/libKPim6Itinerary.so
%{_kf6_libdir}/cmake/KPim6Itinerary/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
