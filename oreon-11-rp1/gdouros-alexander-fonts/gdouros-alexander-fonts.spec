%global source0_hash b907859e9627d7d1e34c8158665c40bce42d1698b5d5ba2046229853932a16a9

%global fontname gdouros-alexander
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        8.01
Release:        19%{?dist}
Summary:        A Greek typeface inspired by Alexander Wilson
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
A text typeface using the Greek letters designed by Alexander Wilson
(1714-1786), a Scottish doctor, astronomer, and type founder, who established a
type foundry in Glasgow in 1744. The type was especially designed for an
edition of Homer’s epics, published in 1756-8 by Andrew and Robert Foulis,
printers to the University of Glasgow. A modern revival, Wilson Greek, was
designed by Matthew Carter in 1995. Peter S. Baker is also using Wilson’s Greek
type in his Junicode font for medieval scholars (2007).

Latin and Cyrillic are based on a Garamond typeface. The font covers the
Windows Glyph List, IPA Extensions, Greek Extended, Ancient Greek Numbers,
Byzantine and Ancient Greek Musical Notation, various typographic extras and
several Open Type features (Case-Sensitive Forms, Small Capitals, Subscript,
Superscript, Numerators, Denominators, Fractions, Old Style Figures, Historical
Forms, Stylistic Alternates, Ligatures).

It was created by George Douros.

%package -n gdouros-textfonts-doc
Summary:        Documentation for all Textfonts by G. Douros
%description -n gdouros-textfonts-doc
This package contains documentation regarding the Textfonts family of fonts by
G. Douros, i.e. Aroania, Anaktoria, Alexander, Avdira and Asea. The origin of
each font is presented, as well as sample texts along with a character overview
and opentype features supported by the fonts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/Alexander.ttf %{buildroot}%{_fontdir}

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

%_font_pkg -f %{fontconf} Alexander.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%files -n gdouros-textfonts-doc
%doc Textfonts.pdf Textfonts.odt

%changelog
%autochangelog
