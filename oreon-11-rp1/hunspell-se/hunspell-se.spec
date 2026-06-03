%global source0_hash 8363726f451d4ed02ee929ea9a4dc0f77334347f8fb518e993ba24bfea54688d

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-se
Summary: Northern Saami hunspell dictionaries
Version: 1.0
Release: 0.33.beta7%{?dist}
Source:        hunspell-se.tar.gz
URL: http://www.divvun.no/index.html
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-se)

%description
Northern Saami hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-1.0beta7.20090316

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p se.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/se_NO.aff
cp -p se.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/se_NO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
se_NO_aliases="se_SE se_FI"
for lang in $se_NO_aliases; do
        ln -s se_NO.aff $lang.aff
        ln -s se_NO.dic $lang.dic
done


%files
%doc Copyright README GPL-3
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.33.beta7
- Import
