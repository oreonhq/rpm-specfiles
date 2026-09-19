%global source0_hash dfac4d3bb38221131824b004c50cc1d4b8059f7a78c2bc79bad73d03f0c9e266

%global	fontname	beteckna
%global common_desc \
This font is available from beteckna.se, it is a geometric sans-serif \
typeface inspired by Paul Renners popular type, Futura. It was drawn by \
Johan Mattsson in Maj 2007. The font is free, licensed under terms of the \
GNU GPL. This version supports English and a few nordic languages. \
Special character &#x2708; ( ✈ ) depicts two cats.

%global fontconf	60-%{fontname}-fonts

Name:		%{fontname}-fonts
Version:	0.3
Release:	37%{?dist}
Summary:	Beteckna sans-serif fonts

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://gnu.ethz.ch/linuks.mine.nu/beteckna/
Source0:	http://gnu.ethz.ch/linuks.mine.nu/beteckna/beteckna-0.3.tar.gz
Source1:	%{name}-fontconfig.conf
Source2:	%{name}-lower-case-fontconfig.conf
Source3:	%{name}-small-caps-fontconfig.conf
Source4:	%{fontname}.metainfo.xml
Source5:	%{fontname}-lower-case.metainfo.xml
Source6:	%{fontname}-small-caps.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontforge, fontpackages-devel
Requires:	%{name}-common = %{version}-%{release}

%description
%common_desc

%_font_pkg -f %{fontconf}.conf Beteckna.otf

%package	common
Summary:	Common files of %{name}
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

# 1 Lower Case
%package -n	%{fontname}-lower-case-fonts
Summary:	Beteckna lower case sfd fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-lower-case-fonts
%common_desc

These are lower case Beteckna Fonts.

%_font_pkg -f  %{fontconf}-lower-case.conf -n lower-case BetecknaLowerCase*.otf
%{_datadir}/appdata/%{fontname}-lower-case.metainfo.xml

# 1 Small Caps
%package -n	%{fontname}-small-caps-fonts
Summary:	Beteckna small caps sfd fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-small-caps-fonts
%common_desc

These are small caps Beteckna Fonts.

%_font_pkg -n small-caps -f  %{fontconf}-small-caps.conf BetecknaSmallCaps.otf
%{_datadir}/appdata/%{fontname}-small-caps.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n beteckna-0.3

fold -s CHANGELOG > CHANGELOG.new
sed -i 's/\r//' CHANGELOG.new
touch -r CHANGELOG CHANGELOG.new
mv CHANGELOG.new CHANGELOG

%build
fontforge -lang=ff -script "-" Beteckna*.sfd << EOF
i = 1
while ( i < \$argc )
	Open (\$argv[i], 1)
	otfile = \$fontname + ".otf"
	Generate(otfile,"otf")
	Close()
	i++
endloop
EOF

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-small-caps.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lower-case.conf

for fconf in %{fontconf}.conf %{fontconf}-lower-case.conf %{fontconf}-small-caps.conf ; 
do
	ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-lower-case.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-small-caps.metainfo.xml

%files common
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc AUTHORS LICENSE CHANGELOG readme.html

%changelog
%autochangelog
