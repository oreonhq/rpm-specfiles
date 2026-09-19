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
# for /usr/share/simcoupe dir ownership
Requires:       simcoupe

%description
SAM Coupé (Spectrum compatible homecomputer) ROM file, for use with the
simcoupe SAM Coupé emulator.

%prep
%setup -q -c -T
cp -a %{SOURCE1} .

%build
# nothing to build data only

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/simcoupe
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/simcoupe

%files
%doc redistribution-permission.txt
%{_datadir}/simcoupe/SAM30.rom

%changelog
%autochangelog
