%global source0_hash 96dbb214a629e5deeb734ac68e91af11edcf46d139546d16b35c0b0c5dc182c6

%global fontname gdouros-aegean
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        9.81
Release:        18%{?dist}
Summary:        A font for ancient scripts in the greater Aegean vicinity
License:        LicenseRef-Fedora-UltraPermissive
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Aegean.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Aegean covers the following scripts and symbols: Basic Latin, Greek and Coptic,
Greek Extended, some Punctuation and other Symbols, Linear B Syllabary, Linear
B Ideograms, Aegean Numbers, Ancient Greek Numbers, Ancient Symbols, Phaistos
Disc, Lycian, Carian, Old Italic, Ugaritic, Old Persian, Cypriot Syllabary,
Phoenician, Lydian, Archaic Greek Musical Notation, Cretan Hieroglyphs,
Cypro-Minoan, Linear A, the Arkalochori Axe, Ancient Greek and Old Italic
variant alphabets. Those of the above that are not supported by the Unicode
Standard 8.0, they are allocated in the Supplementary Private Use Plane 15.

It was created by George Douros.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Aegean.ttf %{buildroot}%{_fontdir}

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
      %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} Aegean.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc Aegean.pdf Aegean.odt

%changelog
%autochangelog
