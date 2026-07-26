%global source0_hash none

%global fontname source-serif
%global fontconf 63-%{fontname}.conf

Name:           adobe-source-serif-pro-fonts
Version:        4.005
Release:        10%{?dist}
Summary:        Typeface for setting text in many sizes, weights, and languages

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            https://github.com/adobe-fonts/source-serif
Source0:        https://github.com/adobe-fonts/source-serif/archive/%{version}R.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{fontname}.fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Source Serif is an open-source typeface to complement the Source Sans family.

%prep
%setup -q -n source-serif-%{version}R
sed -i 's/\r//' LICENSE.md

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%check
appstream-util --nonet validate-relax \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%doc README.md
%license LICENSE.md

%changelog
%autochangelog
