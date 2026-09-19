%global source0_hash 1b9a44369ecd0f1771173eaccee697308faa2b27a74fd311a61e81efb4df3f93

%define fontname chisholm-to-be-continued
%define fontconf 61-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        20090124
Release:        35%{?dist}
Summary:        Decorative Sans Serif Font

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://www.theory.org/~matt/fonts/free/?font=2bc
Source0:        http://www.theory.org/~matt/fonts/free/download/2bc.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
To Be Continued is a decorative/graffiti sans-serif font.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
