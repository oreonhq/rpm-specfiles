%global source0_hash 13f04acdb0590c0b813071e5296686cae25e7bc02eea281222c585911b0a83d1

%global fontname labiryntowy

Name:          %{fontname}-fonts
Version:       1.53
Release:       25%{?dist}
Summary:       Artificial font consisting of vertical and horizontal bars
# Automatically converted from old format: OFL - review is highly recommended.
License:       LicenseRef-Callaway-OFL
URL:           http://alfabet-ozdobny.appspot.com/?str=labiryntowy
Source0:       https://alfabet-ozdobny.appspot.com/images/Labiryntowy_pl.tgz

BuildArch:     noarch
BuildRequires: fontpackages-devel

Requires:      fontpackages-filesystem

%description
Artificial alphabet. Conscript. Font was created by Jacek Szewczyk as a
practical realization of the idea of the alphabet the labyrinth.
This font contains over 300 ligatures and most of the characters
needed to complete the titles and monograms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_fontdir}
cp -p *.ttf %{buildroot}%{_fontdir}

%{_font_pkg} %{_fontdir}
%doc opis.txt

%changelog
%autochangelog
