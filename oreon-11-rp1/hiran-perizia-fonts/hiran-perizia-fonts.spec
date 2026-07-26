%global source0_hash none

%global    fontname    hiran-perizia
%global    fontconf    60-%{fontname}.conf

Name:        %{fontname}-fonts
Version:    0.1.0
Release:    32%{?dist}
Summary:    English asymmetric font

License:    GPL-3.0-or-later WITH Font-exception-2.0
# alas! returns a 404 : http://hiran.in/fontprojects
# have contacted Hiran over e-mail
URL:        http://hiran.in/blog/thanks-perizia-is-now-a-font
Source0:    http://hiran.in/content/fonts/perizia/src/perizia010.sfd
Source1:    %{name}-fontconfig.conf
Source2:    GPL-3.0.txt
Source3:    %{fontname}.metainfo.xml

BuildArch:    noarch
BuildRequires:    fontforge,fontpackages-devel
Requires:    fontpackages-filesystem

%description
perizia is an asymmetric English font.

%prep
%setup -c -T
install -m 644 -p %{SOURCE2} .

%build
fontforge -lang=ff -script "-" %{SOURCE0} <<EOF
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
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc *.pdf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
