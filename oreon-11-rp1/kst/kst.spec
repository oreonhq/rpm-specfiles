%global source0_hash cefbfd3e3710771985e08f02a397ef8ab407168fa8415d2c3c5740c031af18c6
Name:       kst
Version:    2.0.8
Release:        1%{?dist}
Summary:        A data viewing program
License:    GPL-3.0-only
URL:        http://kst-plot.kde.org/
Source0:        http://downloads.sourceforge.net/%{name}/Kst-%{version}.tar.gz
Patch0:     kst-properties.patch
Patch1:     kst-qreal.patch
Patch2:     kst-gsl21.patch
Patch3:     nest.patch
# oreon:deps
BuildRequires:  cfitsio-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  getdata-devel
BuildRequires:  gsl-devel
BuildRequires:  matio-devel
BuildRequires:  muParser-devel
BuildRequires:  netcdf-devel
BuildRequires:  pkgconf
BuildRequires:  qt4-devel
# /oreon:deps
%description
Kst is a real-time data viewing and plotting tool with basic data analysis 
functionality. Kst contains many powerful built-in features and is 
expandable with plugins and extensions. 

Main features of kst include:
  * Robust plotting of live "streaming" data.
  * Powerful keyboard and mouse plot manipulation.
  * Powerful plugins and extensions support.
  * Large selection of built-in plotting and data manipulation functions, 
    such as histograms, equations, and power spectra.
  * Color mapping and contour mapping capabilities for three-dimensional data.
  * Monitoring of events and notifications support.
  * Filtering and curve fitting capabilities.
  * Convenient command-line interface.
  * Powerful graphical user interface.
  * Support for several popular data formats.
  * Multiple tabs or windows. 

%package docs
Summary:    Documentation for kst
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch
%description docs
Documentation, tutorial, and sample data for kst.

%package devel
Summary:    Development libraries and headers for kst
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers and libraries required when building against kst.

%package netcdf
Summary:    netcdf datasource plugin for kst
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description netcdf
A plugin allowing kst to open and read data in netcdf format.

%package fits
Summary:    fits datasource plugin for kst
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   cfitsio = %(pkgconf --modversion cfitsio 2>/dev/null || echo "0")
%description fits
A plugin allowing kst to open and read data and images contained within 
fits files. 

%package getdata
Summary:    getdata datasource plugin for kst
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description getdata
A plugin allowing kst to open and read data in getdata (dirfile) format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Kst-%{version}
%patch -P0 -p1 -b .properties
%patch -P1 -p1 -b .qreal
%patch -P2 -p0 -b .gsl21
%patch -P3 -p0 -b .nest

%build

%cmake -Dkst_merge_files=0 -Dkst_rpath=0 \
  -Dkst_install_prefix=%{_prefix} -Dkst_install_libdir=%{_lib} \
  -Dkst_test=1 -Dkst_release=1 -Dkst_verbose=1 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build --target kst2
%check

%install
%cmake_install
rm -f %{buildroot}%{_bindir}/test_*
rm -frv %{buildroot}%{_datadir}/{applnk,mimelink}/
%find_lang %{name}_common --with-qt
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kst-docs -f %{oreon_filedir}/kst-docs.list
%files -n kst-devel -f %{oreon_filedir}/kst-devel.list
%files -n kst-netcdf -f %{oreon_filedir}/kst-netcdf.list
%files -n kst-fits -f %{oreon_filedir}/kst-fits.list
%files -n kst-getdata -f %{oreon_filedir}/kst-getdata.list

%changelog

%autochangelog
