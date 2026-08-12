%global source0_hash 7c119bcd5ef7963aac00b7d2736bfe87393f6e5d67d201c5fe399e3ab4188f9c

%undefine __cmake_in_source_build
%global framework kimageformats

Name:           kf5-%{framework}
Version:        5.116.0
Release:        10%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with additional image plugins for QtGui

License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

# Upastream patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  jasper-devel
BuildRequires:  kf5-rpm-macros >= %{majmin}
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

Requires:       kf5-filesystem >= %{majmin}

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
