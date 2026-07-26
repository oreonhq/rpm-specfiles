%global source0_hash 722f0a2c2c26194718d0342812e8814c901fb70d013f1888e185d9d55c14792d

%global fontname    oldstandard
%global fontconf    60-%{fontname}.conf

Name:       %{fontname}-sfd-fonts
Version:    2.0.2
Release:    42%{?dist}
Summary:    Old Standard True-Type Fonts

License:    OFL-1.1
# Also at https://fonts.google.com/specimen/Old+Standard+TT
URL:        https://fontlibrary.org/en/font/old-standard
Source0:    http://www.thessalonica.org.ru/downloads/oldstandard-2.0.2.src.zip
Source1:    %{name}-fontconfig.conf
Source2:    http://www.thessalonica.org.ru/downloads/oldstand-manual.pdf
Source3:        %{fontname}.metainfo.xml

# guidelines say this can be used

BuildArch:  noarch
BuildRequires:  fontforge,fontpackages-devel
Requires:   fontpackages-filesystem

%description
The Old Standard font family is an attempt to revive
a specific type of Modern (classicist) style of serif
typefaces, very commonly used in various editions
printed in the late 19th and early 20th century,
but almost completely  abandoned later.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n oldstandard-%{version}

for i in $(ls OldStandard*.sfd);do
    sed -i -e 's/OldStandardTT/OldStandardSFD/'  -e 's/Old \Standard \TT/Old \Standard \SFD/' $i;
done
for txt in OFL* ; do
    sed 's/\r//' $txt > $txt.new
    touch -r $txt $txt.new
    mv $txt.new $txt
done

install -m 644 -p %{SOURCE2} .

%build
fontforge -lang=ff -script "-" OldStandard*.sfd <<EOF
i = 1 
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".otf")
  PrintSetup (5) 
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++ 
endloop
EOF

%install
install -m 755 -d %{buildroot}%{_fontdir}
install -m 644 -p *.otf %{buildroot}%{_fontdir}

install -m 755 -d %{buildroot}%{_fontconfig_templatedir} \
        %{buildroot}%{_fontconfig_confdir}

install -m 644 -p %{SOURCE1} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
    %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%doc *.txt *.pdf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
