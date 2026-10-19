%global source0_hash 9bb1a956fca0718c083bef842e625797535a00ce81f175df08b042c2a92cfe7f
Name:           gshhg-gmt-nc4
Version:        2.3.7
Release:        1%{?dist}
Summary:        Global Self-consistent Hierarchical High-resolution Geography (GSHHG)
License:        LGPL-3.0-or-later
URL:            https://github.com/GenericMappingTools/gshhg-gmt
Source0:        https://github.com/GenericMappingTools/gshhg-gmt/releases/download/%{version}/gshhg-gmt-%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      GMT-coastlines < 2.2.4-2
Provides:       GMT-coastlines = %{version}-%{release}
Provides:       gshhg-gmt = %{version}-%{release}
# oreon:deps

# /oreon:deps
%description
GSHHG is a high-resolution shoreline data set amalgamated from two databases:
Global Self-consistent Hierarchical High-resolution Shorelines (GSHHS) and
CIA World Data Bank II (WDBII).  GSHHG contains vector descriptions at five
different resolutions of land outlines, lakes, rivers, and political
boundaries.  This data for use by GMT, the Generic Mapping Tools.

This package contains the crude, low, and intermediate resolution data.
Install the -all, -full, or -high sub-packages to get full, high, or all of
the resolution data respectively. 

%package        full
Summary:        GSHHG - full resolution
Requires:       %{name}
Obsoletes:      GMT-coastlines-full < 2.2.4-2
Provides:       GMT-coastlines-full = %{version}-%{release}
Provides:       gshhg-gmt-full = %{version}-%{release}
%description    full
%{summary}.

%package        high
Summary:        GSHHG - high resolution
Requires:       %{name}
Obsoletes:      GMT-coastlines-high < 2.2.4-2
Provides:       GMT-coastlines-high = %{version}-%{release}
Provides:       gshhg-gmt-high = %{version}-%{release}
%description    high
%{summary}.

%package        all
Summary:        GSHHG - all resolutions
Requires:       %{name}
Requires:       %{name}-full
Requires:       %{name}-high
Obsoletes:      GMT-coastlines-all < 2.2.4-2
Provides:       GMT-coastlines-all = %{version}-%{release}
Provides:       gshhg-gmt-all = %{version}-%{release}
%description    all
%{summary}.

%prep

%setup -q -n gshhg-gmt-%{version} 

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a *.nc %{buildroot}/%{_datadir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gshhg-gmt-nc4-full -f %{oreon_filedir}/gshhg-gmt-nc4-full.list
%files -n gshhg-gmt-nc4-high -f %{oreon_filedir}/gshhg-gmt-nc4-high.list
%files -n gshhg-gmt-nc4-all -f %{oreon_filedir}/gshhg-gmt-nc4-all.list

%changelog

%autochangelog
