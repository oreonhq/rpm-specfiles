%global source0_hash c18513cb859995576896fed5462925194d79b9731ea52c60fe2622ee135a46a5

%global fontname horai-ume
%global fontconf 65-%{fontname}
%global archivename umefont_%{version}
%global _docdir_fmt %{name}

%global common_desc \
This package contains fonts published by Wataru Horai. It contains Gothic and\
Mincho styles in 20 variants total:\
\
 * Ume Gothic Original, O5, C4, C5, S4, S5\
 * Ume Hy Gothic, O5\
 * Ume P Gothic Original, O5, C4, C5, S4, S5\
 * Ume UI Gothic Original, O5\
 * Ume Mincho Original, S3\
 * Ume P Mincho Original, S3\
\
In addition to Latin, Greek and Cyrilics scripts it provides Hiragana, Katakana\
and CJK. These fonts are suitable for easy on-screen legibility.

Name:           %{fontname}-fonts
Version:        670
Release:        20%{?dist}
Summary:        Gothic and Mincho fonts designed for easy on-screen legibility

License:        mplus
URL:            https://osdn.jp/projects/ume-font/
Source0:        https://osdn.jp/projects/ume-font/downloads/22212/%{archivename}.tar.xz
Source1:        %{fontname}-gothic-fontconfig.conf
Source2:        %{fontname}-hgothic-fontconfig.conf
Source3:        %{fontname}-pgothic-fontconfig.conf
Source4:        %{fontname}-uigothic-fontconfig.conf
Source5:        %{fontname}-mincho-fontconfig.conf
Source6:        %{fontname}-pmincho-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
%common_desc

%package -n %{fontname}-gothic-fonts
# tgc4    Ume Gothic C4 / Regular
# tgc5    Ume Gothic C5 / Medium
# tgo4    Ume Gothic / Regular
# tgo5    Ume Gothic O5 / Medium
# tgs4    Ume Gothic S4 / Regular
# tgs5    Ume Gothic S5 / Medium
Summary:        Free Japanese fonts family Ume Gothic
Requires:       fontpackages-filesystem

%description -n %{fontname}-gothic-fonts
%common_desc

The Ume Gothic family features sans-serif fonts.

%package -n %{fontname}-hgothic-fonts
# hgo4    Ume Hy Gothic / Regular
# hgo5    Ume Hy Gothic O5 / Regular?
Summary:        Free Japanese fonts family Ume Hy Gothic
Requires:       fontpackages-filesystem

%description -n %{fontname}-hgothic-fonts
%common_desc

The Ume Hy Gothic family features sans-serif fonts.

%package -n %{fontname}-pgothic-fonts
# pgc4    Ume P Gothic C4 / Regular
# pgc5    Ume P Gothic C5 / Medium
# pgo4    Ume P Gothic / Regular
# pgo5    Ume P Gothic O5 / Medium
# pgs4    Ume P Gothic S4 / Regular
# pgs5    Ume P Gothic S5 / Medium
Summary:        Free Japanese fonts family Ume P Gothic
Requires:       fontpackages-filesystem

%description -n %{fontname}-pgothic-fonts
%common_desc

The Ume P Gothic family features sans-serif fonts.

%package -n %{fontname}-uigothic-fonts
# ugo4    Ume UI Gothic / Regular
# ugo5    Ume UI Gothic O5 / Medium
Summary:        Free Japanese fonts family Ume UI Gothic
Requires:       fontpackages-filesystem

%description -n %{fontname}-uigothic-fonts
%common_desc

The Ume Gothic family features sans-serif fonts.

%package -n %{fontname}-pmincho-fonts
# pmo3    Ume P Mincho / Regular
# pms3    Ume P Mincho S3 / Regular
Summary:        Free Japanese fonts family Ume P Mincho
Requires:       fontpackages-filesystem

%description -n %{fontname}-pmincho-fonts
%common_desc

The Ume P Mincho family features serif fonts.

%package -n %{fontname}-mincho-fonts
# tmo3    Ume Mincho / Regular
# tms3    Ume Mincho S3 / Regular
Summary:        Free Japanese fonts family Ume Mincho
Requires:       fontpackages-filesystem

%description -n %{fontname}-mincho-fonts
%common_desc

The Ume Mincho family features serif fonts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}

%build
chmod -x *

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-hgothic.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pgothic.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-uigothic.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mincho.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pmincho.conf

for fconf in %{fontconf}-gothic.conf \
             %{fontconf}-hgothic.conf \
             %{fontconf}-pgothic.conf \
             %{fontconf}-uigothic.conf \
             %{fontconf}-mincho.conf \
             %{fontconf}-pmincho.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%_font_pkg -n gothic   -f %{fontconf}-gothic.conf   ume-tg??.ttf
%license license.html

%_font_pkg -n hgothic  -f %{fontconf}-hgothic.conf  ume-hg??.ttf
%license license.html

%_font_pkg -n pgothic  -f %{fontconf}-pgothic.conf  ume-pg??.ttf
%license license.html

%_font_pkg -n uigothic -f %{fontconf}-uigothic.conf ume-ug??.ttf
%license license.html

%_font_pkg -n mincho   -f %{fontconf}-mincho.conf   ume-tm??.ttf
%license license.html

%_font_pkg -n pmincho  -f %{fontconf}-pmincho.conf  ume-pm??.ttf
%license license.html

%changelog
%autochangelog
