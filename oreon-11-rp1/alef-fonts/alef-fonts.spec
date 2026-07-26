%global source0_hash aae9b927858a1dbc56f371ac893af09348031e21c2ef0b94115ce5915d6ec990

%global fontname alef
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.0
Release:        27%{?dist}
Summary:        A free multi-lingual font designed for screens

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://alef.hagilda.com
Source0:        http://alef.hagilda.com/Alef.zip
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  dos2unix
Requires:       fontpackages-filesystem

%description
Alef is a free multilingual font designed specifically for screens.
Alef supports English, Hebrew, and various other European languages, and it's
readable even in extremely small sizes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build
dos2unix OFL-license.txt

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p TTF/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf

%doc readme.txt OFL-license.txt

%changelog
%autochangelog
