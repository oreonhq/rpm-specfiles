%global source0_hash d32b35fdfb39cc58f33f31d2168cbfc63925033e88d515e0161ad0b28db09d87

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-se
Summary: Northern Saami hunspell dictionaries
Version: 1.0
Release: 0.33.beta7%{?dist}
Source0:        https://archive.debian.org/debian/pool/main/h/hunspell-se/hunspell-se_1.0~beta6.20081222.orig.tar.gz
URL: http://www.divvun.no/index.html
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-se)

%description
Northern Saami hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n hunspell-se-1.0beta6.20081222

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 se.aff %{buildroot}%{_datadir}/%{dict_dirname}/se_NO.aff
install -pm 0644 se.dic %{buildroot}%{_datadir}/%{dict_dirname}/se_NO.dic
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
for lang in se_SE se_FI; do
    ln -s se_NO.aff $lang.aff
    ln -s se_NO.dic $lang.dic
done
popd

%files
%doc Copyright README GPL-2 GPL-3
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.33.beta7
- Import
