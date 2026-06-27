%global source0_hash 5874f56e39c6e01d1145472a85a8761fb2e38cdf0ebe3daacb346a35a0ffa50e
%define fontname sj
%define fontconf 63-%{fontname}
%define common_desc Two fonts by Steve Jordi released under the GPL

Name:          %{fontname}-fonts
Version:       2.0.2
Release:       1%{?dist}
Summary:       Two fonts by Steve Jordi released under the GPL

License:       LicenseRef-Callaway-GPLv2-with-exceptions
URL:           https://github.com/deepin-community/sjfonts
Source0:       https://github.com/deepin-community/sjfonts/archive/refs/heads/master.tar.gz#/sjfonts-%{version}.tar.gz
Source1:       %{name}-delphine-fontconfig.conf
Source2:       %{name}-stevehand-fontconfig.conf
Source3:       %{fontname}-stevehand.metainfo.xml
Source4:       %{fontname}-delphine.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge

%description
%common_desc

%package common
Summary:       Common files for %{name}
Requires:      fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-delphine-fonts
Summary:       Handwriting font
Requires:      %{name}-common = %{version}-%{release}

%description -n %{fontname}-delphine-fonts
Handwriting font by Steve Jordi covering latin glyphs.

%_font_pkg -n delphine -f %{fontconf}-delphine.conf Delphine.ttf
%{_datadir}/appdata/%{fontname}-delphine.metainfo.xml

%package -n %{fontname}-stevehand-fonts
Summary:       Handwriting font
Requires:      %{name}-common = %{version}-%{release}

%description -n %{fontname}-stevehand-fonts
Handwriting font by Steve Jordi covering latin glyphs.

%_font_pkg -n stevehand -f %{fontconf}-stevehand.conf SteveHand.ttf
%{_datadir}/appdata/%{fontname}-stevehand.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n sjfonts-master

%build
fontforge -lang=ff -script "-" Delphine.sfd SteveHand.sfd <<EOF
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
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-delphine.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-stevehand.conf

for fontconf in %{fontconf}-delphine.conf %{fontconf}-stevehand.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-stevehand.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-delphine.metainfo.xml

%files common
%doc COPYING
%doc README

%dir %{_fontdir}

%changelog
%autochangelog