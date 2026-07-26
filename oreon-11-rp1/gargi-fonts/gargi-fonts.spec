%global source0_hash e5fffd20d32575e3dff9f875e6000a62db9f5e870be5dbc68ac8a316a9bfc711

%global fontname gargi
%global fontconf 69-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.9
Release:        34%{?dist}
Summary:        A Devanagari font

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://savannah.nongnu.org/projects/gargi
Source0:        http://mirror.vocabbuilder.net/savannah/gargi/%{fontname}-%{version}.tar.gz
Source1:        %{name}-fontconfig.conf
Source2:       %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel fontforge
Requires:       fontpackages-filesystem

%description
A Free Unicode OpenType Font

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{fontname}-%{version}

sed 's/\r//' Changelog > Changelog.new
touch -r Changelog Changelog.new
mv Changelog.new Changelog

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
rm -fr %{buildroot}

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

%doc Changelog COPYING
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
