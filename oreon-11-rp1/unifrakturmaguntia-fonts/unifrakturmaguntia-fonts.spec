%global source0_hash 5119394196ee30f00aeb4a8f22b910fa3ba70a4bb871b4ca216738ba26359152

%global fontname unifrakturmaguntia
%global fontconf 61-%{fontname}-fonts.conf
%global source_date 20140706

Name:          %{fontname}-fonts
Version:       0
Release:       0.24.%{source_date}%{?dist}
Summary:       Font that provide a Fraktur typeface that may be embedded on websites
# Automatically converted from old format: OFL - review is highly recommended.
License:       LicenseRef-Callaway-OFL
URL:           http://unifraktur.sourceforge.net/maguntia.html
Source0:       http://sourceforge.net/projects/unifraktur/files/fonts/UnifrakturMaguntia.2014-07-06.zip
Source10:      %{fontconf}
BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge
Requires:      fontpackages-filesystem

%description
UnifrakturMaguntia is based on Peter Wiegel’s font Berthold Mainzer Fraktur. The
main differences from Peter Wiegel’s font are the following:

- UnifrakturMaguntia uses OpenType for displaying the font’s ligatures.
- UnifrakturMaguntia is suitable for @font-face embedding on the internet. It
  has a permissive license, the OFL, that explicitly allows font embedding.
- G. Ansmann has carefully redrawn all glyphs and significantly expanded the
  font.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n UnifrakturMaguntia.2014-07-06
# Correct end of line encoding for OFL.txt
sed -i 's/\r$//' OFL.txt

%build
fontforge -lang=ff -script "-" *.sfdir <<_EOF
i = 1
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5)
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
_EOF

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf
%doc OFL.txt *.pdf

%changelog
%autochangelog
