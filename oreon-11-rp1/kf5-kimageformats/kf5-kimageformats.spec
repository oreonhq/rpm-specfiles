%undefine __cmake_in_source_build
%global framework kimageformats

Name:           kf5-%{framework}
Version:        5.116.0
Release:        7%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with additional image plugins for QtGui

License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0:        http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

# Upastream patches

BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  jasper-devel
BuildRequires:  kf5-rpm-macros >= %{kf5_dl_majmin}
BuildRequires:  LibRaw-devel

%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libavif)
%endif

# Update to work with OpenEXR/Imath 3.
# Fails to build for f33 and EPEL due to lack of kf5-rpm-macros and
# extra-cmake-modules.
%if 0%{?fedora} > 34
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(Imath)
%else
BuildRequires:  pkgconfig(OpenEXR)
%endif
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(libheif)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem >= %{kf5_dl_majmin}

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%{cmake_kf5} -DKIMAGEFORMATS_HEIF=ON
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_qtplugindir}/imageformats/*.so
%dir %{_kf5_datadir}/kservices5/qimageioplugins/
%{_kf5_datadir}/kservices5/qimageioplugins/*.desktop


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-7
- Prepare for Oreon 11 (RP1)
