%global source0_hash 20e90e852032bf033c2d66de732fda0280547dac17e9a851a89591faef22d2eb

%global fontname aftertheflood-sparks
%global fontconf 66-%{fontname}
%global desc After the Flood Sparks is a font that allows for the combination of text and \
visual data to show an idea and evidence in one headline. This builds on the \
principle of Sparklines defined by Edward Tufte and makes them easier to use. \
Sparklines are currently available as plugins or javascript elements. By  \
installing the Sparks font you can use them immediately without the need for \
custom code. \
\
Sparks data needs to be formatted as comma-separated values, with curly brackets \
at both ends of the set, e.g., {30,60,90}. You can also have numbers at the \
beginning and end of the set, which are useful for providing the start and \
end points, e.g., 123{30,60,90}456 – Sparks has numerals built in.

Name:       %{fontname}-fonts
Version:    2.0
Release:    20%{?dist}
Summary:    After the Flood Sparks, a font to display charts within text
# Automatically converted from old format: OFL - review is highly recommended.
License:    LicenseRef-Callaway-OFL
URL:        https://aftertheflood.co/projects/sparks/
Source0:    https://github.com/aftertheflood/sparks/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    66-%{fontname}-bar.conf
Source2:    66-%{fontname}-dot.conf
Source3:    66-%{fontname}-dot-line.conf
Source4:    %{fontname}.metainfo.xml
Source5:    %{fontname}-bar.metainfo.xml
Source6:    %{fontname}-dot.metainfo.xml
Source7:    %{fontname}-dot-line.metainfo.xml

BuildArch:      noarch

BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib

Requires:       fontpackages-filesystem

%description
%{desc}

%package common
Summary: Common files for After the Flood Sparks

%description common
%{desc}

Common files for After the Flood Sparks.

%package -n %{fontname}-bar-fonts
Summary: After the Flood Sparks Bar fonts
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-bar-fonts
%{desc}

This package provides the Bar family.

%package -n %{fontname}-dot-fonts
Summary: After the Flood Sparks Dot fonts
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-dot-fonts
%{desc}

This package provides the Dot family.

%package -n %{fontname}-dot-line-fonts
Summary: After the Flood Sparks Dot-line fonts
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-dot-line-fonts
%{desc}

This package provides the Dot-line family.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sparks-%{version}

%build
# Nothing to do

%install
# install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 output/otf/*.otf %{buildroot}%{_fontdir}

# install fontconfig files
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bar.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dot.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dot-line.conf

for fconf in %{fontconf}-bar.conf %{fontconf}-dot.conf %{fontconf}-dot-line.conf; do
    ln -s %{_fontconfig_templatedir}/$fconf \
          %{buildroot}%{_fontconfig_confdir}/$fconf
done

# install appdata
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} \
        %{buildroot}%{_datadir}/metainfo

appstream-util validate-relax --nonet \
               %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

               
%files common
%license OFL.txt
%doc AUTHORS.txt CONTRIBUTORS.txt FONTLOG.txt README.md 
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -n bar -f %{fontconf}-bar.conf Sparks-Bar-*.otf
%{_datadir}/metainfo/%{fontname}-bar.metainfo.xml

%_font_pkg -n dot -f %{fontconf}-dot.conf Sparks-Dot-*.otf
%{_datadir}/metainfo/%{fontname}-dot.metainfo.xml

%_font_pkg -n dot-line -f %{fontconf}-dot-line.conf Sparks-Dotline-*.otf
%{_datadir}/metainfo/%{fontname}-dot-line.metainfo.xml

%changelog
%autochangelog
