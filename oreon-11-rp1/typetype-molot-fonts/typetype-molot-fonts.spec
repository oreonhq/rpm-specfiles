%global source0_hash 4ef8a147488e47b984fc4afd1d6a5ebf03dad790d6040f3552457d21e4beab3e

%global fontname typetype-molot
%global fontconf 61-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	1.000
Release:	24%{?dist}
Summary:	A display sans-serif font 

# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
URL:		http://typetype.ru/
Source0:	http://www.typetype.ru/files/fonts/molot.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
%if 0%{?fedora} >= 21
BuildRequires:	libappstream-glib
%endif
Requires:	fontpackages-filesystem

%description
A display sans-serif font created by Roman Ershov and Jovanny Lemonad

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%if 0%{?fedora} >= 21
install -Dm 0644 -p %{SOURCE2} \
		%{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{fontname}.metainfo.xml
%endif

%_font_pkg -f %{fontconf} *.otf

%license "FREE FONT LICENSE.txt"
%if 0%{?fedora} >= 21
%{_datadir}/appdata/%{fontname}.metainfo.xml
%endif

%changelog
%autochangelog
