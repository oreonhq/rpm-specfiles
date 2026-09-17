%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-sr
Summary: Serbian hunspell dictionaries
Version: 25.2.3
Release: 2%{?dist}
License: LGPL-3.0-only
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/sr
Source0: https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-sr)
Provides: hunspell-bs = %{version}-%{release}

%package -n hyphen-sr
Requires: hyphen
Summary: Serbian hyphenation rules
Provides: hyphen-bs = %{version}-%{release}
Supplements: (hyphen and langpacks-sr)

%description -n hyphen-sr
Serbian hyphenation rules.

%description
Serbian hunspell dictionaries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/sr/sr.aff %{buildroot}%{_datadir}/%{dict_dirname}/sr_YU.aff
install -pm 0644 dictionaries/sr/sr.dic %{buildroot}%{_datadir}/%{dict_dirname}/sr_YU.dic
install -pm 0644 dictionaries/sr/sr-Latn.aff %{buildroot}%{_datadir}/%{dict_dirname}/sh_YU.aff
install -pm 0644 dictionaries/sr/sr-Latn.dic %{buildroot}%{_datadir}/%{dict_dirname}/sh_YU.dic
mkdir -p %{buildroot}%{_datadir}/hyphen
install -pm 0644 dictionaries/sr/hyph_sr.dic %{buildroot}%{_datadir}/hyphen/hyph_sr_YU.dic
install -pm 0644 dictionaries/sr/hyph_sr-Latn.dic %{buildroot}%{_datadir}/hyphen/hyph_sh_YU.dic
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
for lang in sr_ME sr_RS; do ln -s sr_YU.aff $lang.aff; ln -s sr_YU.dic $lang.dic; done
for lang in sh_ME sh_RS bs_BA; do ln -s sh_YU.aff $lang.aff; ln -s sh_YU.dic $lang.dic; done
popd
pushd %{buildroot}%{_datadir}/hyphen/
for lang in sr_ME sr_RS; do ln -s hyph_sr_YU.dic hyph_${lang}.dic; done
for lang in sh_ME sh_RS bs_BA; do ln -s hyph_sh_YU.dic hyph_${lang}.dic; done
popd

%files
%doc dictionaries/sr/README.txt
%{_datadir}/%{dict_dirname}/*

%files -n hyphen-sr
%doc dictionaries/sr/README.txt
%{_datadir}/hyphen/*



%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.2.3-1
- Import
