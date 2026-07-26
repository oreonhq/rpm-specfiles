%global source0_hash 5f012e77601c299d51388d0fce3a824ec9fa77c71f10bb741158e0c8a34c9e29

%global fontname 	mgopen
%global fontconf        61-%{fontname}
%global archivename     MgOpen
%global upstream_date   20050515

# Common description
%global common_desc The MgOpen fonts are a font family that includes Latin and Greek glyphs.\
The fonts have been released under a liberal license, similar to the\
license covering the Bitstream Vera fonts.

# Compat description
%global compat_desc \
This package only exists to help transition pre Fedora 11 MgOpen font users to\
the new package split. It will be removed after one distribution release cycle,\
please do not reference it or depend on it in any way.\
\
It can be safely uninstalled.

Name:      %{fontname}-fonts
Version:   0.%{upstream_date}
Release:   47%{?dist}
Summary:   Truetype greek fonts

# Automatically converted from old format: MgOpen - review is highly recommended.
License:   LicenseRef-MgOpen
URL:       http://www.ellak.gr/fonts/mgopen/
Source0:   %{archivename}-%{upstream_date}.tar.gz
# Upstream tarball is not versioned http://www.ellak.gr/fonts/mgopen/files/%{archivename}.tar.gz
Source1:   %{archivename}-%{upstream_date}-doc.tar.gz
# Tarball of the documentation on the site http://www.ellak.gr/fonts/mgopen/
# The LICENCE file is an excerpt from the html page
Source2:   %{fontname}-fontconfig.tar.gz
# Tarball of fontconfig files for each font
Source3:   %{fontname}.metainfo.xml
Source4:   %{fontname}-canonica.metainfo.xml
Source5:   %{fontname}-cosmetica.metainfo.xml
Source6:   %{fontname}-modata.metainfo.xml
Source7:   %{fontname}-moderna.metainfo.xml

BuildArch: noarch
BuildRequires: fontpackages-devel
%description
%common_desc

%package common
Summary:  Truetype greek fonts, common files (documentation…)
Requires: fontpackages-filesystem
%description common
%common_desc
This package consists of files used by other MgOpen packages.

%package compat
Summary:   Truetype greek fonts, compatibility package
Obsoletes: mgopen-fonts < 0.20050515-8
Requires:  %{fontname}-canonica-fonts, %{fontname}-cosmetica-fonts,
Requires:  %{fontname}-modata-fonts, %{fontname}-moderna-fonts
%description compat
%common_desc
%compat_desc

%package -n %{fontname}-canonica-fonts
Summary:   Truetype variable-stroke-width serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-canonica-fonts
%common_desc
This package contains the MgOpen Canonica serif variable-stroke-width typeface,
which is based on the design of Times Roman.

%_font_pkg -n canonica -f %{fontconf}-canonica.conf MgOpenCanonica*.ttf
%{_datadir}/appdata/%{fontname}-canonica.metainfo.xml

%package -n %{fontname}-cosmetica-fonts
Summary:   Truetype variable-stroke-width sans serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-cosmetica-fonts
%common_desc
This package contains the MgOpen Cosmetica sans serif variable-stroke-width
typeface, which is  based on the design of Optima.

%_font_pkg -n cosmetica -f %{fontconf}-cosmetica.conf MgOpenCosmetica*.ttf
%{_datadir}/appdata/%{fontname}-cosmetica.metainfo.xml

%package -n %{fontname}-modata-fonts
Summary:   Truetype fixed-stroke-width sans serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-modata-fonts
%common_desc
This package contains the MgOpen Modata sans serif fixed-stroke-width
which is based on the design of VAG rounded.

%_font_pkg -n modata -f %{fontconf}-modata.conf MgOpenModata*.ttf
%{_datadir}/appdata/%{fontname}-modata.metainfo.xml

%package -n %{fontname}-moderna-fonts
Summary:   Truetype fixed-stroke-width sans serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-moderna-fonts
%common_desc
This package contains the MgOpen Moderna sans serif fixed-stroke-width
typeface which is based on the design of Helvetica.

%_font_pkg -n moderna -f %{fontconf}-moderna.conf MgOpenModerna*.ttf
%{_datadir}/appdata/%{fontname}-moderna.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -a1 -a2 -n %{archivename}-%{version}
iconv -f ISO-8859-1 -t UTF-8 LICENCE > LICENCE.tmp; mv LICENCE.tmp LICENCE

%build

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf  %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p fontconfig/%{fontname}-canonica.conf \
	 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-canonica.conf
install -m 0644 -p fontconfig/%{fontname}-cosmetica.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-cosmetica.conf
install -m 0644 -p fontconfig/%{fontname}-modata.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-modata.conf
install -m 0644 -p fontconfig/%{fontname}-moderna.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-moderna.conf

for fconf in %{fontconf}-canonica.conf \
                %{fontconf}-cosmetica.conf \
                %{fontconf}-modata.conf \
                %{fontconf}-moderna.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-canonica.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-cosmetica.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-modata.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-moderna.metainfo.xml

%files common
%doc LICENCE mgopen.html _files/
%{_datadir}/appdata/%{fontname}.metainfo.xml

%files compat

%changelog
%autochangelog
