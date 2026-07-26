%global source0_hash 40381a191233a359a5d348ddb5c548a8096cf008292225ec2212ffdbb3569db8

%define foundryname  ctan
%define fontpkg      cm-lgc
%define fontname     %{foundryname}-%{fontpkg}
%define fontconf     64-%{fontname}
%define ctan_date    20051007
%define texfontpath  public/%{fontpkg}

# Common description
%define common_desc The CM-LGC PostScript Type 1 fonts are converted from the METAFONT \
sources of the Computer Modern font families. CM-LGC supports the T1, T2A, \
LGR, and TS1 encodings, i.e. Latin, Cyrillic, and Greek.

Name:           ctan-cm-lgc-fonts
Version:        0.5
Release:        47%{?dist}
Summary:        CM-LGC Type1 fonts
# Font exception
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            http://www.ctan.org/tex-archive/fonts/ps-type1/cm-lgc
Source0:        cm-lgc-%{ctan_date}.zip
# upstream source - unversioned zip file
# http://tug.ctan.org/fonts/ps-type1/cm-lgc.zip
Source1:        %{fontname}-fontconfig.tar.gz
# Tarball of fontconfig files for each font
BuildArch:      noarch
BuildRequires:  fontpackages-devel
%description
%{common_desc}

%package common
Summary:  CM-LGC Type 1 fonts, common files (documentation…)
Requires: fontpackages-filesystem
%description common
%common_desc
This package consists of files used by other ctan-cm-lgc-fonts packages.

%define romanfonts %{fontname}-roman-fonts
%package -n %{romanfonts}
Summary:   CM-LGC Type 1 fonts, serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{romanfonts}
%common_desc
This package contains the CM-LGC serif typeface based on Computer Modern.

%_font_pkg -n roman -f %{fontconf}-roman.conf fcm*

%define sansfonts %{fontname}-sans-fonts
%package -n %{sansfonts}
Summary:   CM-LGC Type 1 fonts, sans-serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{sansfonts}
%common_desc
This package contains the CM-LGC sans-serif typeface based on Computer Modern.

%_font_pkg -n sans -f %{fontconf}-sans.conf fcs*

%define typewriterfonts %{fontname}-typewriter-fonts
%package -n %{typewriterfonts}
Summary:   CM-LGC Type 1 fonts, typewriter font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{typewriterfonts}
%common_desc
This package contains the CM-LGC serif typeface based on Computer Modern.

%_font_pkg -n typewriter -f %{fontconf}-typewriter.conf fct*

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a1 -n %{fontpkg}

%build

%install
#install .pfb and .afm files in %{_fontdir} as per the fedora font guidelines
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/type1/%{texfontpath}/* %{buildroot}%{_fontdir}
install -m 0644 -p fonts/afm/%{texfontpath}/* %{buildroot}%{_fontdir}

# fontconfig stuff (see spectemplate-fonts-multi.spec)
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p fontconfig/%{fontname}-roman.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-roman.conf
install -m 0644 -p fontconfig/%{fontname}-sans.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p fontconfig/%{fontname}-typewriter.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-typewriter.conf

for fconf in %{fontconf}-roman.conf \
             %{fontconf}-sans.conf \
             %{fontconf}-typewriter.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%files common
%doc COPYING HISTORY README
%dir %{_fontdir}

%changelog
%autochangelog
