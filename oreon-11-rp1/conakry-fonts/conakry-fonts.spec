%global source0_hash e23dcd1f9bf51d447b5b0f476d876a6b7c1159d7ee031de35ec65ca5405071ea

%global fontname conakry
%global fontconf 65-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	20070829
Release:	35%{?dist}
Summary:	N'Ko font by Michael Everson

License:	OFL-1.1
URL:		http://www.evertype.com/fonts/nko/
Source0:	http://www.evertype.com/fonts/nko/ConakryFont.zip
Source1:	%{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
N'Ko font by well-known Unicode.org expert & font designer Michael 
Everson

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ConakryFont
for txt in OFL* ; do
	sed 's/\r//' $txt > $txt.new
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
