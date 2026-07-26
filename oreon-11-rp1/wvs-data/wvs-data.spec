%global source0_hash none

# Well, for now we use the timestamp of unpacked data
# for version

# Other information can be obtained on
# http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/BOUNDARY/WVS/
# http://www.ngdc.noaa.gov/mgg/fliers/93mgg01.html

%define		WVS_date	20020219

Name:		wvs-data
Version:	0.0.%{WVS_date}
Release:	33%{?dist}
Summary:	World Vector Shoreline data

# Automatically converted from old format: Public Domain - needs further work
License:	LicenseRef-Callaway-Public-Domain
URL:		http://www.flaterco.com/xtide/files.html
Source0:	ftp://ftp.flaterco.com/xtide/wvs.tar.bz2

BuildArch:	noarch

%description
This package contains World Vector Shoreline data, which can
be used for XTide related applications.

%prep
%setup -q -c %{name}-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__install} -c -p -m644 *.dat \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}/

%changelog
%autochangelog
