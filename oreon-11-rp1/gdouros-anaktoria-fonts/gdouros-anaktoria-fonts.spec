%global source0_hash b907859e9627d7d1e34c8158665c40bce42d1698b5d5ba2046229853932a16a9

%global fontname gdouros-anaktoria
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        8.01
Release:        19%{?dist}
Summary:        A font based on "Grecs du roi" and the "First Folio Edition of Shakespeare"
License:        LicenseRef-Fedora-UltraPermissive
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Textfonts.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem
Recommends:     gdouros-textfonts-doc

%description
Greek letters are based on "Grecs du roi" designed by Claude Garamond (1480-
1561) between 1541 and 1544, commissioned by king Francis I of France, for the
exclusive use by the Imprimerie Nationale in Paris. Mindaugas Strockis prepared
a modern version of "Grecs du roi" in 2001.

Latin letters have been digitized directly out of the titles and front pages of
the 1623 "First Folio Edition of Shakespeare". Scott Mann and Peter Guither
prepared a modern version of the font for "The Illinois Shakespeare Festival"
in 1995.

The font covers the Windows Glyph List, IPA Extensions, Greek Extended, Ancient
Greek Numbers, Byzantine and Ancient Greek Musical Notation, various
typographic extras and several Open Type features (Case-Sensitive Forms, Small
Capitals, Subscript, Superscript, Numerators, Denominators, Fractions, Old
Style Figures, Historical Forms, Stylistic Alternates, Ligatures).

It was created by George Douros.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/Anaktoria.ttf %{buildroot}%{_fontdir}

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

%_font_pkg -f %{fontconf} Anaktoria.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
%autochangelog
