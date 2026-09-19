%global source0_hash b907859e9627d7d1e34c8158665c40bce42d1698b5d5ba2046229853932a16a9

%global fontname gdouros-aroania
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        8.01
Release:        19%{?dist}
Summary:        A font based on Victor Julius Scholderer's "New Hellenic"
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
Aroania is a modern recast of Victor Scholderer's "New Hellenic" font, on the
basis of Verdana. In 1927, Victor Julius Scholderer (1880-1971), on behalf of
the "Society for the Promotion of Greek Studies", got involved in choosing and
consulting the design and production of a Greek type called "New Hellenic", cut
by the Lanston Monotype Corporation. He chose the revival of a round, and
almost monoline type which had first appeared in 1492 in the edition of
Macrobius, ascribable to the printing shop of Giovanni Rosso (Joannes Rubeus)
in Venice.

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
install -m 0644 -p fonts/Aroania.ttf %{buildroot}%{_fontdir}

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

%_font_pkg -f %{fontconf} Aroania.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
%autochangelog
