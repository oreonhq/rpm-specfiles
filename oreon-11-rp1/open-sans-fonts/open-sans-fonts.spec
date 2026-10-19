%global source0_hash 329e6957238f8352d65c99c6286f18476ced5dc4aeb861d23550c78cd9565331
%global fontname open-sans
%global fontconf 60-%{fontname}.conf
Name:       %{fontname}-fonts
Version:    1.10
Release:        1%{?dist}
Summary:        Open Sans is a humanist sans-serif typeface designed by Steve Matteson
License:    Apache-2.0
URL:        http://www.google.com/fonts/specimen/Open+Sans
Source0:        %{name}-%{version}.tar.xz
Source1:    %{name}-fontconfig.conf
Source2:        getopensans.sh
BuildArch:  noarch
Requires:   fontpackages-filesystem
# oreon:deps
BuildRequires:  fontpackages-devel
BuildRequires:  ttembed
# /oreon:deps
%description
Open Sans is a humanist sans serif typeface designed by Steve Matteson, Type
Director of Ascender Corp. This version contains the complete 897 character
set, which includes the standard ISO Latin 1, Latin CE, Greek and Cyrillic
character sets. Open Sans was designed with an upright stress, open forms and
a neutral, yet friendly appearance. It was optimized for print, web, and mobile
interfaces, and has excellent legibility characteristics in its letter forms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

ls *.ttf | xargs ttembed
%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
    %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
    %{buildroot}%{_fontconfig_confdir}/%{fontconf}
%_font_pkg -f %{fontconf} *.ttf
%doc LICENSE.txt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10-25
- Import
