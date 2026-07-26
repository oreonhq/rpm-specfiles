%global source0_hash ecbd04cc0494752138837cfcd302d05fcc9757ba50f121e862359ee5cde1388e

%global fontname pothana2000
%global fontconf 69-%{fontname}.conf

Name: %{fontname}-fonts
Version: 1.3.3
Release: 31%{?dist}
Summary: Unicode compliant OpenType font for Telugu

# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License: LicenseRef-Callaway-GPLv2+-with-exceptions
URL: https://fedorahosted.org/pothana_vemana/

Source0: https://fedorahosted.org/releases/p/o/pothana_vemana/%{name}-%{version}.tar.gz
Source1: %{fontname}.metainfo.xml

BuildArch: noarch
BuildRequires: make
BuildRequires: fontforge
BuildRequires: fontpackages-devel
Requires: fontpackages-filesystem

%description
A Free OpenType font for Telugu created by
Dr. Tirumala Krishna Desikacharyulu. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
make

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
 %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{fontconf} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
 %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc ChangeLog COPYRIGHT COPYING AUTHORS README
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
