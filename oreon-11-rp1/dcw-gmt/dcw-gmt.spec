%global source0_hash none

Name:           dcw-gmt
Version:        2.2.0
Release:        7%{?dist}
Summary:        Digital Chart of the World (DCW) for GMT

License:        LGPL-3.0-or-later
URL:            https://github.com/GenericMappingTools/dcw-gmt
Source0:        https://github.com/GenericMappingTools/dcw-gmt/releases/download/%{version}/dcw-gmt-%{version}.tar.gz
BuildArch:      noarch

%description
DCW-GMT is an enhancement to the original 1:1,000,000 scale vector basemap of
the world available from the Princeton University Digital Map and Geospatial
Information Center and from GeoCommunity at
http://data.geocomm.com/readme/dcw/dcw.html.  To read and process the data you
should install GMT, the Generic Mapping Tools.

%prep
%setup -q

# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a *.nc *.txt %{buildroot}/%{_datadir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_datadir}/%{name}/

%changelog
%autochangelog
