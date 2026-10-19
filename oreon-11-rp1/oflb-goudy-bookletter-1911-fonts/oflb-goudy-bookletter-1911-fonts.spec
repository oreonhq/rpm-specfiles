%global source0_hash 117bbb60010b95a4a8d4c2dee6a7c701c33c92808a7dc50e3762e789ec05d132
%global fontname oflb-goudy-bookletter-1911
%global fontconf 61-%{fontname}.conf
Name:		%{fontname}-fonts
Summary:        Clean serif font based on Kennerly Old Style
Version:	20080206
Release:        1%{?dist}
License:	LicenseRef-Fedora-Public-Domain
Source0:        chemoelectric_-_Goudy_Bookletter_1.zip
Source1:	%{name}-fontconfig.conf
Source2:	GoudyBookletter1911.otf
Source3:        %{fontname}.metainfo.xml
URL:		http://home.comcast.net/~crudfactory/cf3/gb1911.html
Requires:	fontpackages-filesystem
BuildArch:	noarch
# oreon:deps
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
# /oreon:deps
%description
Based on the roman of Frederic Goudy's Kennerley Old Style (designed and cut in
1911 for a limited edition of "The Door in the Wall and Other Stories" by H G
Wells, published by Mitchell Kennerley). The letters, though not condensed, may
seem to fit together like pieces of a jigsaw puzzle, giving text an unusually
solid appearance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}
sed -i 's|/home/trashman/bin/fontforge|/usr/bin/fontforge|g' make-otf.py

%build

cp %{SOURCE2} .
%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} %{buildroot}%{_fontconfig_confdir}/%{fontconf}
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
