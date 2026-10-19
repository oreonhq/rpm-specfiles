%global source0_hash 2a072650508a95a99647d0ad7d23e658d092270412573f5f819372149cb49f8c
%global stable_kf6 stable
Name:    kitinerary
Version: 26.04.3
Release:        1%{?dist}
Summary:        A library containing itinerary data model and itinerary extraction code
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND ODbL-1.0
URL:     https://invent.kde.org/frameworks/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:   %{ix86}
%endif
%if 0%{?fedora} || (0%{?oreon} >= 11)
%endif
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6PkPass)
BuildRequires:  cmake(ZXing)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kpublictransport
BuildRequires:  libphonenumber-devel
BuildRequires:  osmctools
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  protobuf-devel
BuildRequires:  qt5-qtbase-private-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kitinerary-devel -f %{oreon_filedir}/kitinerary-devel.list
%files -n kitinerary-doc -f %{oreon_filedir}/kitinerary-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
