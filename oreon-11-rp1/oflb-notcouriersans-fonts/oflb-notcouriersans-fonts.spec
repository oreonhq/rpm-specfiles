%global source0_hash 63787414388493b4018966e8cd1de9f02126730d01e8df72627b86986d24b013

%global	fontname	oflb-notcouriersans
%global fontconf	62-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	1.1
Release:	33%{?dist}
Summary:	NotCourier Sans is a re-interpretation of Nimbus Mono

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://openfontlibrary.org/media/files/OSP/411
Source0:	http://openfontlibrary.org/people/OSP/OSP_-_NotCourierSans_2.zip
Source1:	%{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontforge,fontpackages-devel
Requires:	fontpackages-filesystem

%description
This is a new release of the NotCourier-sans, with its bold.

NotCourier-sans is a re-interpretation of Nimbus Mono and was designed
in Wroclaw at the occasion of Linux Graphics Meeting (LGM 2008).For more
detailed information: ospublish.constantvzw.org

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n NotCourierSans

for txt in *.txt GPL-2 ; do
	sed 's/\r//' $txt > $txt.new
	touch -r $txt $txt.new
	mv $txt.new $txt
done

%build
fontforge -lang=ff -script "-" *.sfd <<EOF
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
install -m 755 -d %{buildroot}%{_fontdir}
install -m 644 -p *.ttf %{buildroot}%{_fontdir}

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
%doc *.txt GPL-2
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
