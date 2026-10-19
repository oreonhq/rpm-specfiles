%global source0_hash none
Name:           telepathy-filesystem
Version:        0.0.2
Release:        29%{?dist}
Summary:        Telepathy filesystem layout
License:        LicenseRef-Not-Copyrightable
BuildArch:      noarch
Requires:       filesystem
# oreon:deps

# /oreon:deps
%description
This package provides some directories which are required by other
packages which comprise the Telepathy release.  

%prep

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/telepathy/managers
mkdir -p $RPM_BUILD_ROOT%{_datadir}/telepathy/clients
mkdir -p $RPM_BUILD_ROOT%{_includedir}/telepathy-1.0
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
