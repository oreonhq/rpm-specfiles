%global source0_hash none

%global fontname oflb-smonohand
%global fontconf 64-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        20090423
Release:        32%{?dist}
Summary:        A handwritten monospace font

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://openfontlibrary.org/media/files/dalles/403
Source0:        http://openfontlibrary.org/people/dalles/dalles_-_SMonohand.ttf
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
SMonohand is a handwritten monospace Latin font with German
characters.

%prep

%build

%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}/SMonohand.ttf

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
   %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

#doc

%changelog
%autochangelog
