%global source0_hash 86665847a51cdfb58a1e1dfd8b1ba33f183485affe50b53e3304f63d3d3552ab

%global fontname msimonson-anonymouspro
%global fontconf 61-%{fontname}.conf
%global archivename AnonymousPro

Name:           %{fontname}-fonts
Version:        1.002.001
Release:        31%{?dist}
Summary:        A coding-friendly monospace font

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://www.ms-studio.com/FontSales/anonymouspro.html
Source0:        http://www.ms-studio.com/FontSales/AnonymousPro-1.002.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Anonymous Pro is a family of fixed-width fonts designed especially with coding
in mind. Characters that could be mistaken for one another (O, 0, I, l, 1,
etc.) have distinct shapes to make them easier to tell apart in the context of
source code.

It has support for most Western and European Latin-based languages, Greek, and
Cyrillic. It also includes special “box drawing” characters.

Anonymous Pro is based on an earlier font, Anonymous, which is a TrueType
version of Susan Lesch and David Lamkins’ font Anonymous 9, a freeware
Macintosh bitmap font.

It was created by Mark Simonson.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}-%{version}
for txt in "OFL.txt" "OFL-FAQ.txt"; do
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

%doc *.txt

%changelog
%autochangelog
