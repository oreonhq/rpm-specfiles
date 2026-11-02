%global source0_hash 01b4a91cec5167ed48c11e8ab78f2048cead78ce94b0cafcad0ae8c5a3044d3d
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: tzdata
Version: 2026f
Release: 2%{?dist}
Summary: Time zone database
License: LicenseRef-Public-Domain AND BSD-3-Clause
URL: https://www.iana.org/time-zones
Source0: https://data.iana.org/time-zones/releases/tzdata%{version}.tar.gz
Source1: tzdata%{version}.tar.gz.asc
Source2: tzdata-key.asc
Source3: https://data.iana.org/time-zones/releases/tzcode%{version}.tar.gz
Source4: tzcode%{version}.tar.gz.asc
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gawk

%description
The IANA time zone database, compiled for use under /usr/share/zoneinfo.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
echo '5a18da01393679ef2559214dc687563f7f3d05691f6f58b7fbc0166f3e796cd6  %{SOURCE3}' | sha256sum -c -
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE4} --data %{SOURCE3}
%autosetup -c -n tzdata-%{version} -p1
tar xzf %{SOURCE3}

%build
make -s VERSION=%{version} CFLAGS="%{_oreon_cflags}" LDFLAGS="%{_oreon_ldflags}" zic tzdata.zi

%install
zd=%{buildroot}%{_datadir}/zoneinfo
mkdir -p $zd
./zic -b fat -d $zd -L /dev/null africa antarctica asia australasia europe northamerica southamerica etcetera backward factory
install -pm0644 zone.tab zone1970.tab zonenow.tab iso3166.tab leapseconds tzdata.zi $zd/
echo %{version} > $zd/VERSION
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE
%dir %{_datadir}/zoneinfo
