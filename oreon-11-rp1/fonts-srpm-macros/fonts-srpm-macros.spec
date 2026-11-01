%global source0_hash f9e4d21f4a52e0c873fc77606362c98ccc14eb1b6ef89a67e8eeb6e90cc867ae
%global debug_package %{nil}

Name: fonts-srpm-macros
Version: 5.0.0
Release: 1%{?dist}
Summary: SRPM macros for font packages
License: MIT
URL: https://pagure.io/fonts-rpm-macros
BuildArch: noarch
Source0: macros.fonts-srpm
Source1: fonts.lua
Source2: LICENSE.txt
Requires: redhat-rpm-config
Requires: forge-srpm-macros

BuildRequires: oreon-rpm-macros

%description
SRPM macros for packaging fonts.

%prep
%oreon_sha256
cp %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmluadir}/fedora/srpm
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.fonts-srpm
install -m 644 %{SOURCE1} %{buildroot}%{_rpmluadir}/fedora/srpm/fonts.lua

%files
%license LICENSE.txt
%{_rpmmacrodir}/macros.fonts-srpm
%{_rpmluadir}/fedora/srpm/fonts.lua
