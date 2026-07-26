%global source0_hash none

%global fontname oflb-dignas-handwriting
%global fontconf 63-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        20031109
Release:        33%{?dist}
Summary:        Handwriting font

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
# Upstream is dead and there is no download link available
URL:            http://openfontlibrary.org/media/files/phranzysko/407
Source0:        http://openfontlibrary.org/people/phranzysko/phranzysko_-_Digna_s_Handwriting.ttf 
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Phranzysko's sister handwriting.

%prep
%setup -q -c -T
cp %{SOURCE0} .

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
%autochangelog
