%global source0_hash none

%global release_date 20170201
%global theme_name Mistral-Thin-Dark

Name:           openbox-theme-mistral-thin-dark
Version:        0
Release:        20.%{release_date}%{?dist}
Summary:        Mistral Dark theme for Openbox

# No license file included, CC-BY-SA mentioned on URL
# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://www.box-look.org/p/1169703/
Source0:        https://dl.opendesktop.org/api/files/download/id/1485941697/%{theme_name}.obt

Requires:       openbox

BuildArch:      noarch

%description
Mistral Thin theme for the Openbox window manager, dark variant.

%prep
%setup -qc

%build
# nothing to build here

%install
%{__mkdir_p} %{buildroot}/%{_datadir}/themes
%{__cp} -av %{theme_name} %{buildroot}/%{_datadir}/themes

%files
%{_datadir}/themes/%{theme_name}

%changelog
%autochangelog
