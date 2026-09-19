%global source0_hash c6f9eb7a878e270b96fbb5dae7783be29710b4405c76e856de60dcfc96386e0b

%global fontname tulrich-tuffy
%global fontconf 60-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.28
Release:        26%{?dist}
Summary:        Generic sans font

# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            http://tulrich.com/fonts/
Source0:        http://tulrich.com/fonts/tuffy-20120614.tar.gz
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge
Requires:       fontpackages-filesystem

%description
Tuffy is an innocuous looking sans font.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n tuffy-20120614

%build
# be really sure that we don't package pre-generated ttf files
rm *.ttf
# We use the legacy font forge script to generate the TTF files (instead of a 
# Python one) because of bug 489109.
fontforge -lang=ff -script "-" *.sfd <<"EOF"
i = 1
while ( i < $argc )
  Open ($argv[i], 1)
  Generate ($fontname + ".ttf")
  PrintSetup (5)
  PrintFont (0, 0, "", $fontname + "-sample.pdf")
  Close()
  i++
endloop
EOF

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc LICENSE.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
