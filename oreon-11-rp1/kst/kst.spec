%global source0_hash cefbfd3e3710771985e08f02a397ef8ab407168fa8415d2c3c5740c031af18c6

Name:       kst
Version:    2.0.8
Release:    62%{?dist}
Summary:    A data viewing program

License:    GPL-3.0-only
URL:        http://kst-plot.kde.org/
Source0:    http://downloads.sourceforge.net/%{name}/Kst-%{version}.tar.gz
# Fix calls to set_target_properties in KstMacros.cmake
# https://bugs.kde.org/show_bug.cgi?id=322286
Patch0:     kst-properties.patch
# Upstream patch to fix qreal for arm
# https://bugs.kde.org/show_bug.cgi?id=342642
# https://bugzilla.redhat.com/show_bug.cgi?id=1180348
Patch1:     kst-qreal.patch
Patch2:     kst-gsl21.patch
Patch3:     nest.patch

BuildRequires: gsl-devel cmake
BuildRequires: cfitsio-devel
BuildRequires: pkgconf
%if 0%{?fedora} >= 17
BuildRequires:  netcdf-cxx-devel
%else
BuildRequires:  netcdf-devel
%endif
BuildRequires: getdata-devel muParser-devel
BuildRequires: matio-devel
BuildRequires: desktop-file-utils
BuildRequires: qt4-devel

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
# Hack because cfitsio won't run if it's internal library version
# doesn't perfectly match between installed library and compiled
# against library.  Meh.
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
# -Dkst_merge_files=1 is failing for now
# https://bugs.kde.org/show_bug.cgi?id=322289
%cmake -Dkst_merge_files=0 -Dkst_rpath=0 \
  -Dkst_install_prefix=%{_prefix} -Dkst_install_libdir=%{_lib} \
  -Dkst_test=1 -Dkst_release=1 -Dkst_verbose=1 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build --target kst2

%check
#make test

%install
%cmake_install
rm -f %{buildroot}%{_bindir}/test_*
# omit deprecated kde3-era stuff -- rex
rm -frv %{buildroot}%{_datadir}/{applnk,mimelink}/
%find_lang %{name}_common --with-qt

%ldconfig_scriptlets

%files -f %{name}_common.lang
%doc INSTALL AUTHORS README COPYING COPYING-DOCS COPYING.LGPL 

#binaries
%{_bindir}/kst*
%{_libdir}/libkst*so.*
%dir %{_libdir}/kst2
%dir %{_libdir}/kst2/plugins
%{_libdir}/kst2/plugins/libkst2_dataobject*so
%{_libdir}/kst2/plugins/libkst2_fi*so

%{_datadir}/applications/kst2.desktop

%{_libdir}/kst2/plugins/libkst2_datasource_ascii.so

%{_libdir}/kst2/plugins/libkst2_datasource_qimagesource.so

%{_libdir}/kst2/plugins/libkst2_datasource_matlab.so

%{_libdir}/kst2/plugins/libkst2_datasource_sampledatasource.so

%{_libdir}/kst2/plugins/libkst2_datasource_sourcelist.so

%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/kst2.1.gz

%files devel
%{_libdir}/libkst*a
%{_libdir}/libkst*so

%files docs
#%{_datadir}/apps/kst/tutorial/gyrodata.dat

%files fits
%{_libdir}/kst2/plugins/libkst2_datasource_fitsimage.so

%files netcdf
%{_libdir}/kst2/plugins/libkst2_datasource_netcdf.so

%files getdata
%{_libdir}/kst2/plugins/libkst2_datasource_dirfilesource.so

%changelog
%autochangelog
