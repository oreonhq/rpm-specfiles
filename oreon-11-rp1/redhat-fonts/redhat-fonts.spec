%global fontname redhat
%global fontconf 64-%{fontname}
%global asfontname com.redhat.%{fontname}

%global projname RedHatFont

%global desc \
Red Hat Typeface is a fresh take on the geometric sans genre, \
taking inspiration from a range of American sans serifs \
including Tempo and Highway Gothic. \
 \
The Display styles, made for headlines and big statements, \
are low contrast and spaced tightly, with a large x-height and open counters. \
 \
The Text styles have a slightly smaller x-height and narrower width \
for better legibility, are spaced more generously, and have thinned joins \
for better performance at small sizes. \
 \
The Mono styles are similar to the Text styles, but are adapted \
for better performance to render code and similar text. \
 \
The three families can be used together seamlessly at a range of sizes. \
 \
The fonts were originally commissioned by Paula Scher / Pentagram \
and designed by Jeremy Mickel / MCKL for the new Red Hat identity.

Name:           %{fontname}-fonts
Version:        4.1.0
Release:        3%{?dist}
Summary:        Red Hat Typeface fonts
# Only the metainfo files are CC-BY-SA
License:        OFL-1.1-RFN AND CC-BY-SA-4.0
URL:            https://github.com/RedHatOfficial/%{projname}

Source0:        %{url}/archive/%{version}/%{projname}-%{version}.tar.gz
Source1:        %{fontconf}-display-fontconfig.conf
Source2:        %{fontconf}-text-fontconfig.conf
Source3:        %{fontconf}-mono-fontconfig.conf
Source4:        %{fontconf}-display-vf-fontconfig.conf
Source5:        %{fontconf}-text-vf-fontconfig.conf
Source6:        %{fontconf}-mono-vf-fontconfig.conf

BuildArch:      noarch
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  fontpackages-devel

%description %{desc}


%package -n %{fontname}-display-fonts
Summary:        Red Hat Display fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-display-fonts %{desc}

This package provides the Display fonts variant.

%package -n %{fontname}-text-fonts
Summary:        Red Hat Text fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-text-fonts %{desc}

This package provides the Text fonts variant.

%package -n %{fontname}-mono-fonts
Summary:        Red Hat Mono fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-mono-fonts %{desc}

This package provides the Monospace fonts variant.

%package -n %{fontname}-display-vf-fonts
Summary:        The variable font of Red Hat Display fonts
Requires:       fontpackages-filesystem
Provides:	font(redhatdisplayvf)

%description -n %{fontname}-display-vf-fonts %{desc}

This package provides the variable font version of the Display fonts variant.

%package -n %{fontname}-text-vf-fonts
Summary:        The variable font of Red Hat Text fonts
Requires:       fontpackages-filesystem
Provides:	font(redhattextvf)

%description -n %{fontname}-text-vf-fonts %{desc}

This package provides the variable font version of the Text fonts variant.

%package -n %{fontname}-mono-vf-fonts
Summary:        The Variable font of Red Hat Mono fonts
Requires:       fontpackages-filesystem
Provides:	font(redhatmonovf)

%description -n %{fontname}-mono-vf-fonts %{desc}

This package provides the variable font version of the Monospace fonts variant.

%prep
%autosetup -n %{projname}-%{version} -p1


%build
# Nothing to build

%install

# Install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontdir}-vf
## Mono
install -m 0644 -p fonts/Mono/otf/*.otf %{buildroot}%{_fontdir}
## Mono VF
install -m 0644 -p fonts/Mono/variable/*.ttf %{buildroot}%{_fontdir}-vf
## Display/Text
install -m 0644 -p fonts/Proportional/*/otf/*.otf %{buildroot}%{_fontdir}
## Display/Text VF
install -m 0644 -p fonts/Proportional/*/variable/*.ttf %{buildroot}%{_fontdir}-vf

# Drop duplicate
rm -f %{buildroot}%{_fontdir}-vf/*VF*.ttf
# workaround to address crash issue/unexpected italic rendering with variable fonts
rm -f %{buildroot}%{_fontdir}-vf/*-Italic*.ttf

# Install fontconfig data
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-display.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-text.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-display-vf.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-text-vf.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono-vf.conf

for fconf in %{fontconf}-display %{fontconf}-text %{fontconf}-mono; do
  ln -s %{_fontconfig_templatedir}/${fconf}.conf %{buildroot}%{_fontconfig_confdir}/${fconf}.conf
  ln -s %{_fontconfig_templatedir}/${fconf}-vf.conf %{buildroot}%{_fontconfig_confdir}/${fconf}-vf.conf
done

# Install AppStream metadata
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
for f in metainfo/*.metainfo.xml; do
    sed -e 's/\(com\.redhat\..*\)</\1-vf</' $f > ${f/.metainfo.xml/-vf.metainfo.xml}
    touch -r $f ${f/.metainfo.xml/-vf.metainfo.xml}
done
install -m 0644 -p metainfo/*.metainfo.xml %{buildroot}%{_datadir}/metainfo

%check
# Validate AppStream metadata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml


%_font_pkg -n display -f %{fontconf}-display.conf RedHatDisplay*.otf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-display.metainfo.xml

%_font_pkg -n text -f %{fontconf}-text.conf RedHatText*.otf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-text.metainfo.xml

%_font_pkg -n mono -f %{fontconf}-mono.conf RedHatMono*.otf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-mono.metainfo.xml

%global _fontdir %{_fontdir}-vf

%_font_pkg -n display-vf -f %{fontconf}-display-vf.conf RedHatDisplay*.ttf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-display-vf.metainfo.xml

%_font_pkg -n text-vf -f %{fontconf}-text-vf.conf RedHatText*.ttf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-text-vf.metainfo.xml

%_font_pkg -n mono-vf -f %{fontconf}-mono-vf.conf RedHatMono*.ttf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-mono-vf.metainfo.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.0-3
- Prepare for Oreon 11 (RP1)
