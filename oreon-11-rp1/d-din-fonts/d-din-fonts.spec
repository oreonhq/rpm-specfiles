%global source0_hash bbc88b21334fd0a7912d92c6ac21249937c17e5b514ae33965b8e910198c075e
%global fontname d-din
%global fontconf 64-%{fontname}
%global asfontname com.datto.%{fontname}
%global desc \
D-DIN is a sans-serif typeface family derived from German DIN \
(Deutsches Institut fuer Normung / German Institute for Standardization) \
font style. \
 \
This font was commissioned by Datto, Inc. from Monotype and is used for \
the company's primary corporate typography.
Name:           %{fontname}-fonts
Version:        1.0
Release:        21%{?dist}
Summary:        Datto D-DIN fonts
License:        LicenseRef-Callaway-OFL AND LicenseRef-Callaway-CC-BY-SA
URL:            https://www.datto.com/fonts/d-din
Source0:        https://www.datto.com/fonts/%{fontname}/D-DIN_complete-v%{version}.zip
Source1:        %{fontconf}-fontconfig.conf
Source2:        %{fontconf}-condensed-fontconfig.conf
Source3:        %{fontconf}-exp-fontconfig.conf
BuildArch:      noarch
Requires:       fontpackages-filesystem
%global __provides_exclude ^0$
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  fontpackages-devel
# /oreon:deps
%description %{desc}

%package -n %{fontname}-condensed-fonts
Summary:        Datto D-DIN condensed fonts
Requires:       fontpackages-filesystem
%description -n %{fontname}-condensed-fonts %{desc}

This package provides the condensed fonts variant.

%package -n %{fontname}-exp-fonts
Summary:        Datto D-DIN expanded fonts
Requires:       fontpackages-filesystem
%description -n %{fontname}-exp-fonts %{desc}

This package provides the expanded fonts variant.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-exp.conf
for fconf in %{fontconf}.conf %{fontconf}-condensed.conf %{fontconf}-exp.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p *.metainfo.xml %{buildroot}%{_datadir}/metainfo
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%_font_pkg -f %{fontconf}.conf D-DIN.otf D-DIN-*.otf
%license OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}.metainfo.xml
%_font_pkg -n condensed -f %{fontconf}-condensed.conf D-DINCondensed*.otf
%license OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}-condensed.metainfo.xml
%_font_pkg -n exp -f %{fontconf}-exp.conf D-DINExp*.otf
%license OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}-exp.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n d-din-condensed-fonts -f %{oreon_filedir}/d-din-condensed-fonts.list
%files -n d-din-exp-fonts -f %{oreon_filedir}/d-din-exp-fonts.list

%changelog

%autochangelog
