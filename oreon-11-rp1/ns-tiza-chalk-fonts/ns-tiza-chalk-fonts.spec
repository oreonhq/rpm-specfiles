%global source0_hash 35c22f9f0a5a556db28abc125698803f531b3bacd0c013796a25fed87e2dd218

%global fontname ns-tiza-chalk
%global fontconf 64-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        20080210
Release:        32%{?dist}
Summary:        Chalky slab-serif fonts

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://www.nuevostudio.com/project/tiza/
Source0:        http://www.nuevostudio.com/files/downloads/tiza.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
A bold, chalky slab-serif font inspired by the lovely slab-serif Giza.
It supports diacritics in addition to the basic latin set of characters.
The font was created by Pablo Caro.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -L -q %{SOURCE0}
chmod 0644 *.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done

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
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
