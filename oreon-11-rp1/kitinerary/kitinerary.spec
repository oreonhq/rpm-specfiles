%global source0_hash none

Name:    kitinerary
Version: 26.04.1
Release: 1%{?dist}
Summary: A library containing itinerary data model and itinerary extraction code

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND ODbL-1.0
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# 
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
%if 0%{?fedora} || 0%{?oreon}
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
