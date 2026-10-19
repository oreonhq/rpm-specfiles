%global source0_hash bc847bcb74e32e5b845fc0c177452da161f89405baa7ac1e34f38a248af5b2b8
%global fontname gdouros-musica
%global fontconf 65-%{fontname}.conf
Name:           %{fontname}-fonts
Version:        3.17
Release:        21%{?dist}
Summary:        A font for musical symbols
License:        LicenseRef-Fedora-UltraPermissive
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Musica.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml
BuildArch:      noarch
Requires:       fontpackages-filesystem
# oreon:deps
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Musica is a work-font for Ancient Greek, Byzantine and Western musical symbols.
The font also covers basic Latin, along with a few common symbols. Besides
musical notation glyphs supported by the Unicode Standard 7.0, Musica provides
extra symbols in Plane 15.

It was created by George Douros.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Musica.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
      %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml
%_font_pkg -f %{fontconf} Musica.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc Musica.pdf
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
