%global source0_hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
%global fontname fontsquirrel-crete-round
%global fontconf 63-%{fontname}.conf
Name:          %{fontname}-fonts
Version:       0
Release:        1%{?dist}
Summary:        General purpose warm slab serif font
License:       LicenseRef-Callaway-OFL
URL:           https://www.fontsquirrel.com/fonts/crete-round
Source0:        https://www.fontsquirrel.com/fonts/download/crete-round#/crete-round.zip
Source1:       %{name}.conf
BuildArch:     noarch
Requires:      fontpackages-filesystem
# oreon:deps
BuildRequires:  fontpackages-devel
# /oreon:deps
%description
Crete Round is a warm slab serif providing a hint of softness to texts. It
started as a tailored version of the original Crete fonts -
www.type-together.com/Crete - created specially to serve as corporate typeface
for the type design competition Letter2 - www.letter2.org. Crete Round is more
independent from the original with modified terminals and serifs to create two
new fonts that deliver a more contemporary and functional appearance. The tall
x-height, low contrast and sturdy slabs prove to be surprisingly efficient for
web use. This font supports 128 languages and has 416 glyphs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p CreteRound-{Italic,Regular}.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
%_font_pkg -f %{fontconf} CreteRound-{Italic,Regular}.otf
%license *.txt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
