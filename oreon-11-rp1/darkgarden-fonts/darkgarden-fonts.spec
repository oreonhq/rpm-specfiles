%global source0_hash 3c4c6161eb4668f5fc0c9ff0bab693d7a88c2371e0978c0e5d4da25dcce2fea5

# Due to changes in the Fedora legal environment, rpm spec files are now specifically listed as a "contribution" 
# in/to Fedora (refer to FPCA FAQ here: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement ).
# Quote: 
# "Q. Are RPM spec files covered by the FPCA?
# A. Sure. They're a contribution, aren't they? :) Nevertheless, they are explicitly named as an example of a contribution, to clear up a past confusion."
# 
# As a result of this change, I have decided to specifically license all of my rpm spec files as GPLv2.
# See program source for a copy of this license.
# 

%global fontname darkgarden
%global fontconf 69-darkgarden.conf

Name:           %{fontname}-fonts
Version:	1.1
Release:        42%{?dist}
Summary:	Dark Garden is a decorative outline font of unusual shape

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://darkgarden.sourceforge.net/

Source0:        http://darkgarden.sourceforge.net/darkgarden-1.1.src.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge >= 20061025-1
Requires:      fontpackages-filesystem

%description
Dark Garden is a decorative outline font of unusual shape.
The typeface is based on author's original hand drawings.
The letterform is complex, with all characters decorated
with spikes resembling thorns or flames, character spacing
is very dense. Such a theme makes it a great font for titles,
banners, logos etc. Due to the font's complicated form,
long text passages are not very legible, but short paragraphs
such as titles or lyrics / poetry look very well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n darkgarden-1.1 %{SOURCE0}

%build
fontforge -lang=ff -c 'Open($1); Generate($2)' DarkGarden.sfd DarkGarden.ttf

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
%doc COPYING.txt
%doc README.txt
%doc COPYING-GPL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
