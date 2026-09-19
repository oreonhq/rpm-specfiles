%global source0_hash none

%global fontname gdouros-aegyptus
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        6.17
Release:        21%{?dist}
Summary:        A font for Egyptian hieroglyphs

# https://web.archive.org/web/20150625020428/http://users.teilar.gr/~g1951d/
# "in lieu of a licence:
# Fonts and documents in this site are not pieces of property or merchandise
# items; they carry no trademark, copyright, license or other market tags;
# they are free for any use. George Douros"
License:        LicenseRef-Fedora-UltraPermissive
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Aegyptus.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Aegyptus contains an Extended List of 7062 Egyptian Hieroglyphs, in regular and
bold font weights.

There is no standard for Egyptian Hieroglyphs or Meroitic, so they are
allocated in the Supplementary Private Use Plane 15. The fonts also cover Basic
Latin and some Punctuation and other Symbols.

They were created by George Douros, mainly based on the book Hieroglyphica,
PIREI I², 2000 and the work of Alan Gardiner.

%prep
%setup -q -c

%build

%install
rm -f *_hint.ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Aegyptus*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
      %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} Aegyptus*.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc *.pdf

%changelog
%autochangelog
