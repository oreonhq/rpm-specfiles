%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-be
Summary:        Belarusian hunspell dictionaries
Version: 26.8.0.3
Release:        1%{?dist}
License: GPL-1.0-or-later AND LGPL-2.1-or-later
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/be_BY
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-be)
# oreon:deps

# /oreon:deps
%package -n hyphen-be
Requires: hyphen
Summary: Belarusian hyphenation rules
Supplements: (hyphen and langpacks-be)
%description -n hyphen-be
Belarusian hyphenation rules.

%description
Belarusian hunspell dictionaries

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/be_BY/be-official.aff %{buildroot}%{_datadir}/%{dict_dirname}/be_BY.aff
install -pm 0644 dictionaries/be_BY/be-official.dic %{buildroot}%{_datadir}/%{dict_dirname}/be_BY.dic
mkdir -p %{buildroot}%{_datadir}/hyphen
install -pm 0644 dictionaries/be_BY/hyph_be_BY.dic %{buildroot}%{_datadir}/hyphen/hyph_be_BY.dic
%oreon_autofiles hyphen-be usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hyphen-be -f %{oreon_filedir}/hyphen-be.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.2.3-1
- Import
