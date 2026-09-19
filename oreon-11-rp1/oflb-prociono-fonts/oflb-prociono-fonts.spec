%global source0_hash none

%global fontname oflb-prociono
%global fontconf 62-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 20141125
Release: 26%{?dist}
Summary: A text roman with standard and discretionary ligatures, class-based kerning

License: OFL-1.1
URL:     http://www.google.com/fonts/specimen/Prociono
Source0: https://googlefontdirectory.googlecode.com/hg/ofl/prociono/Prociono-Regular.ttf
Source1: https://googlefontdirectory.googlecode.com/hg/ofl/prociono/OFL.txt
Source2: %{name}-fontconfig.conf
Source3: %{fontname}.metainfo.xml

BuildArch: noarch
BuildRequires: fontforge,fontpackages-devel
Requires: fontpackages-filesystem

%description
A serif font created by Barry Schwartz

The name is pronounced "pro-tsee-O-no" and is Esperanto for 
either "raccoon" or the star Procyon. The author prefers to 
think of this font as a raccoon.

%prep
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} .

%build
#nothing to build

%install
install -m 755 -d %{buildroot}%{_fontdir}
install -m 644 -p *.ttf %{buildroot}%{_fontdir}

install -m 755 -d %{buildroot}%{_fontconfig_templatedir} \
  %{buildroot}%{_fontconfig_confdir}

install -m 644 -p %{SOURCE2} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
 %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
