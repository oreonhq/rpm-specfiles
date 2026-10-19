%global source0_hash none
%global commit 3c59953e7ee5792efecdb232cb4c7211e7785f52
%global commitdatestring 2026-02-13 12:35:27 -0700
%global cosmic_minver 1.8.0
Name:           cosmic-wallpapers
Version: 1.9.0
Release:        1%{?dist}
Summary:        Default wallpapers for the COSMIC Desktop Environment
License:        CC-BY-SA-4.0
URL:            https://github.com/pop-os/cosmic-wallpapers
Source0:        cosmic-wallpapers-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description

%prep

tar -xzf %{SOURCE0} -C .

%build

%install
cd cosmic-wallpapers
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
