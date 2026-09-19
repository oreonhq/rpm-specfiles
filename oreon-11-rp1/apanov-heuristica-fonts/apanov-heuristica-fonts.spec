%global source0_hash 08bf21e44941d195dceab637c3d8e22f4b5ce8490c83993cebd85d721b92553d

%global fontname apanov-heuristica
%global fontconf 61-%{fontname}.conf

%global archivename heuristica-ttf-%{version}
%global googlename  evristika

Name:    %{fontname}-fonts
Version: 1.0.2
Release: 28%{?dist}
Epoch:   1
Summary: A serif latin & cyrillic font

# Automatically converted from old format: OFL - review is highly recommended.
License:   LicenseRef-Callaway-OFL
URL:       http://sourceforge.net/projects/heuristica/

#we are using binary ttf archive as source archive
#is currently missing required fontforge scripts
#to compile and generate ttf files
Source0:   http://downloads.sourceforge.net/project/heuristica/%{archivename}.tar.xz
Source1:   %{name}-fontconfig.conf
Source2:   %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: dos2unix
Requires:      fontpackages-filesystem

%description
Heuristica is a serif latin & cyrillic font, derived from the “Adobe Utopia”
font that was released to the TeX Users Group under a liberal license.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
dos2unix OFL-FAQ.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *\.ttf %{buildroot}%{_fontdir}

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
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
