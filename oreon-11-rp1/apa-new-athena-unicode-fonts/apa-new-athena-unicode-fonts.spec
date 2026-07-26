%global source0_hash d0e775ff86ff772ce842b50a385f71acf0f2b66a2a430ff00460e58d3e7f4af0

%global fontname apa-new-athena-unicode
%global fontconf 64-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	3.4
Release:	36%{?dist}
Summary:	New Athena Unicode is a libre/open multilingual font

License:	OFL-1.1
URL:		http://apagreekkeys.org/NAUdownload.html
Source0:	http://apagreekkeys.org/fonts/NAU3_4ttf.zip
Source1:	%{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
New Athena Unicode is an libre/open multilingual font distributed by
the American Philological Association. It follows the latest version
of the Unicode standard and includes characters for English and
Western European languages, polytonic Greek, Coptic, Old Italic, 
and Demotic Egyptian transliteration, as well as metrical symbols
and other characters used by classical scholars.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n NAU3_4ttf

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
%doc *.pdf *.rtf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
