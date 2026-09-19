%global source0_hash 6011aef9a3f5ede216eeb8bca868c4a2bca335a6b836a8c9fa82aaef28a13a77

%global fontname drehatlas-widelands
%global fontconf 61-%{fontname}.conf
%global metapkgver 2010-02-06

# This is a highly-stylized titling font, so picking an ideal substitute with
# fontconfig is pointless

Name:		%{fontname}-fonts
Version:	1.0.3.1
Release:	38%{?dist}
Summary:	A Latin typeface inspired by feudal calligraphy
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
URL:		http://www.drehatlas.de/
Source0:	http://downloads.sourceforge.net/project/drehatlas-fonts/Font-Packages/COMPLETE/drehatlas-fonts-%{metapkgver}.zip
Source1:	%{fontconf}
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel fontforge
Requires:	fontpackages-filesystem

%description
This font was created by Peter Schwanemann as a logo for the Widelands project,
but has since been enhanced.  The font is decorative and not really usable for
real texts, but it looks nice for logos, banners or similar stuff.  All normal
latin glyphs and arabic numbers are included and usable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version}
cd drehatlas-fonts-%{metapkgver}/Widelands-%{version}
# Wrap the license file at 80 chars
fold -s LICENSE > LICENSE.new
touch -r LICENSE LICENSE.new
mv LICENSE.new LICENSE

%build

%install
cd drehatlas-fonts-%{metapkgver}/Widelands-%{version}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc drehatlas-fonts-%{metapkgver}/Widelands-%{version}/LICENSE drehatlas-fonts-%{metapkgver}/Widelands-%{version}/FONTLOG

%changelog
%autochangelog
