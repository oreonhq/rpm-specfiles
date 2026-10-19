%global source0_hash none
%global fontname opendyslexic
%global fontconf 60-%{fontname}.conf
%global gitdate 20210904
%global gitrev e7ac50a
Name:		%{fontname}-fonts
Version:	0.940
Release:        1%{?dist}
Summary:        Font designed for dyslexics and high readability
License:	LicenseRef-Callaway-OFL
URL:		http://dyslexicfonts.com/
Source0:        %{fontname}-%{gitdate}git%{gitrev}.tar.bz2
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
Requires:	fontpackages-filesystem
# oreon:deps
BuildRequires:  fontpackages-devel
# /oreon:deps
%description
OpenDyslexic is a new open sourced font created to increase readability for 
readers with dyslexia. The typefaces includes regular, bold, italic and 
bold-italic styles. It is being updated continually and improved based on 
input from dyslexic users. 

%prep

%setup -q -n %{fontname}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p compiled/OpenDyslexic*.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}
%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc README.md
%license OFL.txt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
