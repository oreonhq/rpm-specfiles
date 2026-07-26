%global source0_hash 76373f9f5da854532627acb396dc0519505f4937d50b21ddee5e821816422ee4

%global	fontname	chisholm-letterslaughing
%global	fontconf	65-%{fontname}.conf
%global archivename	lleqcdd.zip

Name:		%{fontname}-fonts
Version:	20030323
Release:	34%{?dist}
Summary:	Letters Laughing is a decorative/LED sans-serif font

# https://bugzilla.redhat.com/show_bug.cgi?id=491530#c3
# grep -a -B 6 -A 84 'SIL OPEN FONT LICENSE' *.ttf
License:	OFL-1.1
URL:		http://glyphobet.net/fonts/free/?font=lleqcdd
Source0:	%{archivename}
Source1:	%{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Letters Laughing is a decorative/LED sans-serif font

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n letters

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
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
