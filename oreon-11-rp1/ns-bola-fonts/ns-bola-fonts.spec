%global source0_hash bd5514d6de77cd80c46e9afe1c3340958ae94184c534dbf07f0ce4e68028af8b

%global fontname ns-bola
%global fontconf 64-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        20080203
Release:        32%{?dist}
Summary:        Chunky Geometric Fonts

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://www.nuevostudio.com/project/bola/
Source0:        http://www.nuevostudio.com/files/downloads/bola.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
A chunky geometric font like many others out there!
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
rm -fr %{buildroot}

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
%{_datadir}/appdata/%{fontname}.metainfo.xml

%doc

%changelog
%autochangelog
