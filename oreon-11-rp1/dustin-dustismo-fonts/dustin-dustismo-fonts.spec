%global source0_hash 2dce72bf24984cd02665ffb868f94648097a93fd78501d7063ad576773b28302

%global fontname dustin-dustismo
%global fontconf 63-%{fontname}

%global common_desc General purpose fonts by Dustin Norlander available in \
serif and sans-serif versions. The fonts cover all European Latin characters.

Name:          %{fontname}-fonts
Version:       20030318
Release:       36%{?dist}
Summary:       General purpose sans-serif font with bold, italic and bold-italic variations

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://www.dustismo.com
# Actual download URL
#URL:           http://ftp.de.debian.org/debian/pool/main/t/ttf-dustin/ttf-dustin_20030517.orig.tar.gz 
Source0:       Dustismo.zip
Source1:       %{name}-sans-fontconfig.conf
Source2:       %{name}-roman-fontconfig.conf
Source3:       %{fontname}.metainfo.xml
Source4:       %{fontname}-sans.metainfo.xml
Source5:       %{fontname}-roman.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc

%package common
Summary:       Common files for %{name}
Requires:      fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-sans-fonts
Summary:       General purpos sans-serif fonts
Requires:      %{name}-common = %{version}-%{release}
Provides:      %{name} = 20030318-3
Obsoletes:     %{name} < 20030318-3

%description -n %{fontname}-sans-fonts
%common_desc

General purpose sans-serif font with bold, italic and bold-italic variations

%_font_pkg -n sans -f %{fontconf}-sans.conf dustismo_bold_italic.ttf dustismo_bold.ttf dustismo_italic.ttf Dustismo.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml

%package -n %{fontname}-roman-fonts
Summary:       General purpose serif font
Requires:      %{name}-common = %{version}-%{release}
Provides:      %{name}-roman = 20030318-3
Obsoletes:     %{name}-roman < 20030318-3

%description -n %{fontname}-roman-fonts
%common_desc

General purpose serif font with bold, italic and bold-italic variations

%_font_pkg -n roman -f %{fontconf}-roman.conf Dustismo_Roman_Bold.ttf Dustismo_Roman.ttf Dustismo_Roman_Italic_Bold.ttf Dustismo_Roman_Italic.ttf      
%{_datadir}/appdata/%{fontname}-roman.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}
sed -i 's/\r//' license.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-roman.conf

for fontconf in %{fontconf}-sans.conf %{fontconf}-roman.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-roman.metainfo.xml

%files common
%doc license.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
