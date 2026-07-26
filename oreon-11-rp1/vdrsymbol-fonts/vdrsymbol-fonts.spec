%global source0_hash 63107e25c0e4b5ae5aadef8e4323ff58a0cbd2f965827d26dba6d4f664370bf4

%global fontname vdrsymbol
%global fontconf 69-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        20100612
Release:        31%{?dist}
Summary:        VDR symbol fonts

# Automatically converted from old format: Bitstream Vera and Public Domain - needs further work
License:        Bitstream-Vera AND LicenseRef-Callaway-Public-Domain

URL:            http://andreas.vdr-developer.org/fonts/
Source0:        http://andreas.vdr-developer.org/fonts/download/vdrsymbols-ttf-%{version}.tgz
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
VDRSymbols is a font for use with VDR plugins and patches.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n vdrsymbols
chmod -x insert_vdr_symbols.pe

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf

%license COPYRIGHT.txt
%doc HISTORY README insert_vdr_symbols.pe

%changelog
%autochangelog
