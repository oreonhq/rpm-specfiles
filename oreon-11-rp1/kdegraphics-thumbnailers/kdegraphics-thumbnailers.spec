
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdegraphics-thumbnailers
Summary: Thumbnailers for various graphic types
Version: 25.12.3
Release:	2%{?dist}

# most sources GPLv2+, dscparse.* GPL, gscreator.* LGPLv2+,
License: GPL-2.0-or-later
URL:     https://www.kde.org/applications/graphics/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KExiv2Qt6)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(QMobipocket6)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(KDcrawQt6)

%description
%{summary}.


%prep
%autosetup


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%files
%license COPYING*
%{_kf6_metainfodir}/org.kde.kdegraphics-thumbnailers.metainfo.xml
%{_kf6_qtplugindir}/kf6/thumbcreator/blenderthumbnail.so
%{_kf6_qtplugindir}/kf6/thumbcreator/gsthumbnail.so
%{_kf6_qtplugindir}/kf6/thumbcreator/mobithumbnail.so
%{_kf6_qtplugindir}/kf6/thumbcreator/rawthumbnail.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
