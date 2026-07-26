%global source0_hash 9c193753b44e2bceea49fd9249809770af3befe99baff9aed2163778eb0028dc

%global foundryname  ctan
%global fontpkg      kerkis
%global fontname     %{foundryname}-%{fontpkg}
%global fontconf     64-%{fontname}
%global ctan_date    20090115

# Common description
%global common_desc Kerkis type 1 fonts for LaTeX.  These fonts are particularly useful \
for typesetting Greek. The Greek repertoire includes full support for \
polytonic Greek, Greek numerals, and double forms of several letters \
that occur in variant forms.

Name:           ctan-kerkis-fonts
Version:        2.0
Release:        53%{?dist}
Summary:        Kerkis Type 1 fonts
# Automatically converted from old format: LPPL - review is highly recommended.
License:        LicenseRef-Callaway-LPPL
URL:            http://www.ctan.org/pkg/kerkis
Source0:        kerkis-%{ctan_date}.zip
# upstream source - unversioned zip file
# http://tug.ctan.org/fonts/greek/kerkis.zip
Source1:        %{fontname}-fontconfig.tar.gz
# Tarball of fontconfig files for each font
BuildArch:      noarch
BuildRequires:  fontpackages-devel
%description
%{common_desc}

%package common
Summary:  Kerkis Type 1 fonts, common files (documentation…)
Requires: fontpackages-filesystem
%description common
%common_desc
This package consists of files used by other %{fontname} packages.

%global seriffonts %{fontname}-serif-fonts
%package -n %{seriffonts}
Summary:  Kerkis serif Type1 fonts
Requires:  %{name}-common = %{version}-%{release}
%description -n %{seriffonts}
%{common_desc}
This package contains the Kerkis font family. It is based on the URW Bookman
font and extends it with Greek characters and math support.

%_font_pkg -n serif -f %{fontconf}-serif.conf Kerkis.* Kerkis-*Bold.* Kerkis-*Italic.* Kerkis-*SmallCaps*

%global sansfonts %{fontname}-sans-fonts
%package -n %{sansfonts}
Summary:  KerkisSans Type1 fonts
Requires:  %{name}-common = %{version}-%{release}
%description -n %{sansfonts}
%{common_desc}
This package contains the KerkisSans font family, based on a free version
of the AvantGardURW Bookman font.

%_font_pkg -n sans -f %{fontconf}-sans.conf KerkisSans* 

%global calligraphicfonts %{fontname}-calligraphic-fonts
%package -n %{calligraphicfonts}
Summary:  Kerkis Calligraphic Type1 fonts
Requires:  %{name}-common = %{version}-%{release}
%description -n %{calligraphicfonts}
%{common_desc}
This package contains the Kerkis-Calligraphic font family, a calligraphic font 
family of Kerkis, based on URW Bookman.

%_font_pkg -n calligraphic -f %{fontconf}-calligraphic.conf Kerkis-Calligraphic* ktsy.*

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a1 -n %{fontpkg}

%build

%install
#install .pfb and .afm files in %{_fontdir} as per the fedora font guidelines
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p type1/* %{buildroot}%{_fontdir}
install -m 0644 -p afm/* %{buildroot}%{_fontdir}

# fontconfig stuff (see spectemplate-fonts-multi.spec)
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p fontconfig/%{fontname}-serif.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p fontconfig/%{fontname}-sans.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p fontconfig/%{fontname}-calligraphic.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-calligraphic.conf

for fconf in %{fontconf}-serif.conf \
             %{fontconf}-sans.conf \
             %{fontconf}-calligraphic.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%files common
%doc License.txt README.html
%dir %{_fontdir}

%changelog
%autochangelog
