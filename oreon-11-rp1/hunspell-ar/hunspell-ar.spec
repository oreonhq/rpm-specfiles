%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ar
Summary: Arabic (Egypt, Algeria, etc.) hunspell dictionaries
Version: 25.2.3
Release: 26%{?dist}
License: GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/ar
Source0: https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ar)

%description
Arabic (Egypt, Algeria, etc.) hunspell dictionaries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/ar/ar.aff %{buildroot}%{_datadir}/%{dict_dirname}/ar_TN.aff
install -pm 0644 dictionaries/ar/ar.dic %{buildroot}%{_datadir}/%{dict_dirname}/ar_TN.dic
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
ar_TN_aliases="ar_AE ar_BH ar_DJ ar_DZ ar_EG ar_ER ar_IL ar_IN ar_IQ ar_JO ar_KM ar_KW ar_LB ar_LY ar_MA ar_MR ar_OM ar_PS ar_QA ar_SA ar_SD ar_SO ar_SY ar_TD ar_YE"
for lang in $ar_TN_aliases; do
    ln -s ar_TN.aff $lang.aff
    ln -s ar_TN.dic $lang.dic
done
popd

%files
%doc dictionaries/ar/README_ar.txt
%{_datadir}/%{dict_dirname}/*



%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.2.3-1
- Import
