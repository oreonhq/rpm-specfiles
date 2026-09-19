%global source0_hash none

Name:		gimp-high-pass-filter
Version:	1.2
Release:	%autorelease
Summary:	High-pass filter script for the GIMP

License:	GPL-2.0-or-later
URL:		http://registry.gimp.org/node/7385
Source0:	http://registry.gimp.org/files/high-pass.scm
Source1:	%{name}.metainfo.xml

Requires:	gimp

BuildArch:	noarch

%description
A general purpose high-pass filter plugin. It shows up as 
Filters->Generic->High Pass Filter. You can select a blur radius that sets the 
size of detail to be passed by the filter, as well as an option to keep the 
source layer or replace it.

%prep

%build

%install
install -m 0644 -p -D %{SOURCE0} %{buildroot}%{_datarootdir}/gimp/3.0/scripts/high-pass.scm
# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%files
%{_datarootdir}/gimp/3.0/scripts/high-pass.scm
#AppStream metadata
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
%autochangelog
