%global source0_hash 9f225ce269b5757b31019435077ea84606ba56b7d36a0b94f51dacd370b5868d

%global fontname gust-antykwa-torunska
%global shortname antt
%global fontconf 69-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.08
%global versiontag %(echo %{version}|tr . _)
Release:        %autorelease
Summary:        Two-element typeface for typesetting of small prints
License:        LPPL-1.3a
URL:            https://jmn.pl/en/antykwa-torunska/
Source0:        https://jmn.pl/pliki/AntykwaTorunska-otf-%{versiontag}.zip
Source1:        %{name}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Antykwa Toruńska (meaning just "Antiqua of Torun") is a two-element typeface
designed by Zygfryd Gardzielewski in the 50’s.

The font is mainly used for typesetting of small prints. Its characteristic
features are the widening of vertical stems at the top and the wave-like form of
some of the horizontal and diagonal lines as well as of the serifs.

The current version contains a greatly extended character set (e.g., cyrillic,
greek, most often used mathematical symbols and currency symbols, additional
ligatures) compared to the original, as well as additional typefaces (light,
regular, medium and bold in normal and condensed widths).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{shortname}-otf

%build

%install
mkdir -p %{buildroot}%{_fontdir}
cp -p *.otf %{buildroot}%{_fontdir}

mkdir -p %{buildroot}%{_fontconfig_templatedir} \
         %{buildroot}%{_fontconfig_confdir}
cp -p %{SOURCE1} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
         %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.otf

%changelog
%autochangelog
