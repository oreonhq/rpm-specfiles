%global source0_hash none

%global		addon luminosity-masks

Name:		gimp-%{addon}
Version:	0
Release:	%autorelease
Summary:	Luminosity mask channels plug-in for Gimp
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://registry.gimp.org/node/28644
Source0:	http://registry.gimp.org/files/sg-%{addon}.scm
Source1:	%{name}.metainfo.xml
Source2:	gpl-2.0.txt
%if 0%{?fedora}
BuildRequires:	libappstream-glib
%endif
Requires:	gimp
BuildArch:	noarch

%description
Script-Fu script generating a full set of Light, Dark, and 
Midtone masks as channels for your image.

%prep
# Copy license
cp -p %{SOURCE2} .

%build
## Nothing to build.

%install
%if 0%{?epel}
mkdir -p %{buildroot}%{_datadir}/gimp/2.0/scripts/
%endif

install -Dpm 0644 %{SOURCE0} -t %{buildroot}%{_datadir}/gimp/2.0/scripts/

%if 0%{?fedora}
# Add AppStream metadata
install -Dpm 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/metainfo/

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml
%endif

%files
%license gpl-2.0.txt
%{_datadir}/gimp/2.0/scripts/*.scm
%if 0%{?fedora}
%{_datadir}/metainfo/%{name}.metainfo.xml
%endif

%changelog
%autochangelog
