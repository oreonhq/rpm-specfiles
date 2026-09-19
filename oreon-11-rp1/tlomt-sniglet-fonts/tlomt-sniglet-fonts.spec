%global source0_hash c0ad8d2a843f8aff3b6483894f1e0917b6cdc2418260379dba69207682cfd729

%global fontname tlomt-sniglet
%global fontconf 60-%{fontname}

Name:		%{fontname}-fonts
Summary:	A rounded, sans-serif font useful for headlines
Version:	1.000
Release:	32%{?dist}
# License attribution confirmed by author
# See: sniglet-license-confirmation-email.txt
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
Source0:	https://s3.amazonaws.com/theleague-production/fonts/sniglet.zip
Source1:	%{name}-fontconfig.conf
Source2:	sniglet-license-confirmation-email.txt
Source3:        %{fontname}.metainfo.xml

URL:		https://www.theleagueofmoveabletype.com/sniglet
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Sniglet is a fun rounded, sans-serif font useful for headlines and other
creative treaments. The font was created by Haley Fiege, and it supports a
full Latin character set including diacritics (accent marks). Notably, it
has full coverage for Icelandic and French characters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}
cp %{SOURCE2} .

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf}.conf Sniglet.ttf
%doc sniglet-license-confirmation-email.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
