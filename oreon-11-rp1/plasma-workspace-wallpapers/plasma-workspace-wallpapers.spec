
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-workspace-wallpapers
Version: 6.6.2
Release:	2%{?dist}
Summary: Additional wallpapers for Plasma workspace
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
URL:     https://cgit.kde.org/%{name}.git

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
BuildArch: noarch

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

Requires:       kde-filesystem

# Elarun moved here
Conflicts:      kde-wallpapers < 15.08.3-10

# when we went noarch
Obsoletes:      plasma-workspace-wallpapers < 5.2.0-2


%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%files
%license COPYING.LGPL3
%{_datadir}/wallpapers/Altai/
%{_datadir}/wallpapers/Autumn/
%{_datadir}/wallpapers/BytheWater/
%{_datadir}/wallpapers/Canopee/
%{_datadir}/wallpapers/Cascade/
%{_datadir}/wallpapers/Cluster/
%{_datadir}/wallpapers/ColdRipple/
%{_datadir}/wallpapers/ColorfulCups/
%{_datadir}/wallpapers/DarkestHour/
%{_datadir}/wallpapers/Elarun/
%{_datadir}/wallpapers/EveningGlow/
%{_datadir}/wallpapers/FallenLeaf/
%{_datadir}/wallpapers/FlyingKonqui/
%{_datadir}/wallpapers/Flow/
%{_datadir}/wallpapers/Grey/
%{_datadir}/wallpapers/Honeywave/
%{_datadir}/wallpapers/IceCold/
%{_datadir}/wallpapers/Kay/
%{_datadir}/wallpapers/Kite/
%{_datadir}/wallpapers/Kokkini/
%{_datadir}/wallpapers/MilkyWay/
%{_datadir}/wallpapers/Mountain/
%{_datadir}/wallpapers/Nexus/
%{_datadir}/wallpapers/Nuvole/
%{_datadir}/wallpapers/OneStandsOut/
%{_datadir}/wallpapers/Opal/
%{_datadir}/wallpapers/PastelHills/
%{_datadir}/wallpapers/Patak/
%{_datadir}/wallpapers/Path/
%{_datadir}/wallpapers/SafeLanding/
%{_datadir}/wallpapers/ScarletTree/
%{_datadir}/wallpapers/Shell/
%{_datadir}/wallpapers/summer_1am/
%{_datadir}/wallpapers/Volna/
%{_datadir}/wallpapers/Coast/
%{_datadir}/wallpapers/Orionids/

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
