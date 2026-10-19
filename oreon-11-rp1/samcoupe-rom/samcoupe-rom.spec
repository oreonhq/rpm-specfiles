%global source0_hash none
Name:           samcoupe-rom
Version:        3.0
Release:        30%{?dist}
Summary:        SAM Coupé (Spectrum compatible homecomputer) ROM file
License:        LicenseRef-Fedora-UltraPermissive
URL:            http://www.worldofsam.org/
Source0:        SAM30.rom
Source1:        redistribution-permission.txt
BuildArch:      noarch
Requires:       simcoupe
# oreon:deps

# /oreon:deps
%description
SAM Coupé (Spectrum compatible homecomputer) ROM file, for use with the
simcoupe SAM Coupé emulator.

%prep

%setup -q -c -T
cp -a %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/simcoupe
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/simcoupe
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
