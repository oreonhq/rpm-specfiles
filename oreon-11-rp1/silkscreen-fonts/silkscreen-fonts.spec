%global source0_hash 9ad38d3f7841ec2e0d55efcfcc1ed7e7d33f80463dc9831261d1fd9a06f57ff3

%global fontname silkscreen
%global fontconf 60-%{fontname}

%global common_desc \
Silkscreen is a four member type family for your Web graphics created by Jason \
Kottke. Silkscreen is best used in places where extremely small graphical \
display type is needed. The primary use is for navigational items (nav bars, \
menus, etc), but it works well wherever small type is needed. In order to \
preserve the proper spacing and letterforms, Silkscreen should be used at 8pt. \
multiples (8pt., 16pt., 24pt., etc.) with anti-aliasing turned off. \

Name:		%{fontname}-fonts
Summary: 	Silkscreen four member type family
Version:	1.0
Release:	34%{?dist}
# License attribution confirmed by author and Open Font Library
# http://openfontlibrary.org/media/files/jkottke/218
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
Source0:	http://www.kottke.org/plus/type/silkscreen/download/silkscreen.tar.gz
Source1:	%{name}-fontconfig.conf
Source2:	%{name}-expanded-fontconfig.conf
Source3:	%{fontname}.metainfo.xml
Source4:	%{fontname}-expanded.metainfo.xml
URL:		http://www.kottke.org/plus/type/silkscreen/
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	%{name}-common = %{version}-%{release}

%description
%common_desc

%package common
Summary:	Common files for Silkscreen fonts (documentation...)
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other Silkscreen packages.

%package -n %{fontname}-expanded-fonts
Summary:	Expanded Silkscreen font family
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-expanded-fonts
%common_desc

This font family has a slightly expanded spacing between the letters in 
comparison to the normal Silkscreen font family.

%_font_pkg -n expanded -f %{fontconf}-expanded.conf slkscre*.ttf
%{_datadir}/appdata/%{fontname}-expanded.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}

%build

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-expanded.conf

for fontconf in %{fontconf}.conf %{fontconf}-expanded.conf ; do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-expanded.metainfo.xml

%_font_pkg -f %{fontconf}.conf slkscr.ttf slkscrb.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%files common
%doc readme.txt
%dir %{_fontdir}

%changelog
%autochangelog
