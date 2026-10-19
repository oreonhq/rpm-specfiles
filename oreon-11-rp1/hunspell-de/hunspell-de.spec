%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8
Name:          hunspell-de
Summary:        German hunspell dictionaries
Version:       20240224
Release:        1%{?dist}
License:       GPL-2.0-only OR GPL-3.0-only
URL:           https://cgit.freedesktop.org/libreoffice/dictionaries/tree/de
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
BuildArch:     noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-de)
# oreon:deps

# /oreon:deps
%description
German (Germany, Switzerland, etc.) hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/hunspell
install -pm 0644 dictionaries/de/de_AT_frami.aff %{buildroot}%{_datadir}/hunspell/de_AT.aff
install -pm 0644 dictionaries/de/de_AT_frami.dic %{buildroot}%{_datadir}/hunspell/de_AT.dic
install -pm 0644 dictionaries/de/de_CH_frami.aff %{buildroot}%{_datadir}/hunspell/de_CH.aff
install -pm 0644 dictionaries/de/de_CH_frami.dic %{buildroot}%{_datadir}/hunspell/de_CH.dic
install -pm 0644 dictionaries/de/de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_LI.aff
install -pm 0644 dictionaries/de/de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_LI.dic
install -pm 0644 dictionaries/de/de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_DE.aff
install -pm 0644 dictionaries/de/de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_DE.dic
install -pm 0644 dictionaries/de/de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_BE.aff
install -pm 0644 dictionaries/de/de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_BE.dic
install -pm 0644 dictionaries/de/de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_LU.aff
install -pm 0644 dictionaries/de/de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_LU.dic
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240224-5
- Import
