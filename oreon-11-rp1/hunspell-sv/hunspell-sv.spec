%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-sv
Summary:        Swedish hunspell dictionaries
Version: 26.8.0.3
Release:        1%{?dist}
License: LGPL-3.0-only
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/sv_SE
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-sv)
# oreon:deps

# /oreon:deps
%description
Swedish hunspell dictionaries

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/sv_SE/sv_SE.aff dictionaries/sv_SE/sv_SE.dic %{buildroot}%{_datadir}/%{dict_dirname}/
install -pm 0644 dictionaries/sv_SE/sv_FI.aff dictionaries/sv_SE/sv_FI.dic %{buildroot}%{_datadir}/%{dict_dirname}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.2.3-1
- Import
