%global fontname open-sans
%global fontconf 60-%{fontname}.conf

Name:       %{fontname}-fonts
Version:    1.10
Release:    25%{?dist}
Summary:    Open Sans is a humanist sans-serif typeface designed by Steve Matteson

License:    Apache-2.0
URL:        http://www.google.com/fonts/specimen/Open+Sans

# Since the font doesn't have clear upstream, the source zip package is
# downloaded from Google Fonts. It is then converted to tar.gz. All by
# getopensans.sh.
Source0:    %{name}-%{version}.tar.xz
Source1:    %{name}-fontconfig.conf
Source2:    getopensans.sh

BuildArch:  noarch
BuildRequires:  fontpackages-devel
BuildRequires:  ttembed
Requires:   fontpackages-filesystem

%description
Open Sans is a humanist sans serif typeface designed by Steve Matteson, Type
Director of Ascender Corp. This version contains the complete 897 character
set, which includes the standard ISO Latin 1, Latin CE, Greek and Cyrillic
character sets. Open Sans was designed with an upright stress, open forms and
a neutral, yet friendly appearance. It was optimized for print, web, and mobile
interfaces, and has excellent legibility characteristics in its letter forms.

%prep
%setup -q

%build
# set Embedding permission to 'Installable'
ls *.ttf | xargs ttembed

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
    %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
    %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf
%doc LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10-25
- Prepare for Oreon 11 (RP1)
