%global source0_hash f3c470ddced8f689e9725a3d5b36ecc6540a6ba9ae94dcbf12a50385fc006878
%global realname egeoip
%global git_commit 4efda2c2b5b0084d3e77b8f0bbdec78514706b34
%global git_date 20140111
Name:		erlang-%{realname}
Version:	1.1
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang IP Geolocation module
License:	MIT
URL:		https://github.com/mochi/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/mochi/%{realname}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
Patch1:		erlang-egeoip-0001-FIXME-an-old-DB-in-Fedora.patch
Patch2:		erlang-egeoip-0002-Fix-for-Rebar3.patch
Requires:	GeoIP-GeoLite-data-extra
# oreon:deps
BuildRequires:  GeoIP-GeoLite-data-extra
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
Erlang IP Geolocation module, currently supporting the MaxMind GeoLite City
Database.

%prep

%autosetup -p1 -n %{realname}-%{git_commit}

%build

%{erlang3_compile}
%install
%{erlang3_install}
mkdir -p %{buildroot}%{erlang_appdir}/priv/
ln -s %{_datadir}/GeoIP/GeoIPCity.dat %{buildroot}%{erlang_appdir}/priv/GeoIPCity.dat
ln -s %{_datadir}/GeoIP/GeoLiteCity.dat %{buildroot}%{erlang_appdir}/priv/GeoLiteCity.dat
ln -s %{_datadir}/GeoIP/GeoLiteCountry.dat %{buildroot}%{erlang_appdir}/priv/GeoIP.dat
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
