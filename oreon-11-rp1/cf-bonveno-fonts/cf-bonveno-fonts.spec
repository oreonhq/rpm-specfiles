%global source0_hash a33f64ca59f0481f1abceb32bb6f0d5df75601ee1ad620d4220bf15c9c7e38b7

%global	fontname	cf-bonveno
%global fontconf	60-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	1.1
Release:	41%{?dist}
Summary:	A fun font by Barry Schwartz

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://home.comcast.net/~crudfactory/cf3/bonveno.xhtml
Source0:	http://home.comcast.net/~crudfactory/cf3/fonts/BonvenoCF-1.1.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch: 	noarch
BuildRequires:	fontforge, fontpackages-devel
Requires:	fontpackages-filesystem

%description
A set of fun fonts from the crud factory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

for txt in COPYING README ; do
	sed 's/\r//' $txt > $txt.new
	touch -r $txt $txt.new
	mv $txt.new $txt
done

%build
fontforge -lang=ff -script "-" BonvenoCF*.sfd <<EOF
i = 1 
while ( i < \$argc )
	Open (\$argv[i], 1)
	Generate (\$fontname + ".ttf")
	PrintSetup (5) 
	PrintFont (0, 0, "", \$fontname + "-sample.pdf")
	Close()
	i++ 
endloop
EOF

%install
rm -fr %{buildroot}

install -dm 755 %{buildroot}%{_fontdir}
install -pm 644 *.ttf  %{buildroot}%{_fontdir}

install -m 755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%doc  COPYING* README*

%dir %{_fontdir}/

%changelog
%autochangelog
