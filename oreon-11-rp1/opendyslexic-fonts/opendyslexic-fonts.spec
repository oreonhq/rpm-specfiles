%global source0_hash none

%global fontname opendyslexic
%global fontconf 60-%{fontname}.conf
%global gitdate 20210904
%global gitrev e7ac50a

Name:		%{fontname}-fonts
# This is the version from the compiled fonts (thanks fontforge)
Version:	0.940
Release:	12%{?dist}
Summary:	Font designed for dyslexics and high readability
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
URL:		http://dyslexicfonts.com/
# No source tarballs that I could find, so we get it from github
# git clone https://github.com/antijingoist/opendyslexic
# tar cfj opendyslexic-20210904gite7ac50a.tar.bz2 opendyslexic
Source0:	%{fontname}-%{gitdate}git%{gitrev}.tar.bz2
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
OpenDyslexic is a new open sourced font created to increase readability for 
readers with dyslexia. The typefaces includes regular, bold, italic and 
bold-italic styles. It is being updated continually and improved based on 
input from dyslexic users. 

%prep
%setup -q -n %{fontname}

%build
# Nothing to do here.

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p compiled/OpenDyslexic*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc README.md
%license OFL.txt

%changelog
%autochangelog
