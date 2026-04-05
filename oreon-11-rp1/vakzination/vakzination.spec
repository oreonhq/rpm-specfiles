%global commit0 851a9fb0178003bb931d637356ee82c4ecfc4bc4
%global date 20241228
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           vakzination
Version:        23.01.0^git%{date}.%{shortcommit0}
Release:	5%{?dist}

License:        CC-PDDC AND Apache-2.0 AND LGPL-2.0-or-later AND CC0-1.0 AND BSD-3-Clause AND GPL-2.0-or-later AND FSFAP
Summary:        Vakzination manages your health certificates like vaccination, test, and recovery certificates.
Url:            https://invent.kde.org/plasma-mobile/vakzination
Source:         https://invent.kde.org/pim/%{name}/-/archive/%{commit0}/%{name}-%{commit0}.tar.gz

ExclusiveArch:  %{java_arches}

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KHealthCertificate)
BuildRequires: cmake(KPim6Itinerary)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_kf6_datadir}/applications/ %{buildroot}/%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang

%license LICENSES/*

%{_kf6_bindir}/%{name}

%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.01.0^git%{date}.%{shortcommit0}-4
- Prepare for Oreon 11 (RP1)
