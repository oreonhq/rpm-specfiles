%global source0_hash 9166239b334d920db02d0d70603a2f5dd02cb3a1bea23b1b49bd8710a71b9155

%global fontname dustin-domestic-manners
%global fontconf 63-%{fontname}.conf

Name:          %{fontname}-fonts
Version:       20030527
Release:       35%{?dist}
Summary:       Handwriting font by Dustin Norlander

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://www.dustismo.com
# Actual download URL
# URL:         http://ftp.de.debian.org/debian/pool/main/t/ttf-dustin/ttf-dustin_20030517.orig.tar.gz 
Source0:       Domestic_Manners.zip
Source1:       %{name}-fontconfig.conf
Source2:       %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description 

This font mimics the authors handwriting. The name comes from the book 
Domestic Manners of the Americans, by Fanny Trollope.

Font contains, letters, numbers, punctuation, accented characters and 
some special characters (most European Latin characters).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}
sed -i 's/\r//' license.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%license license.txt

%changelog
%autochangelog
