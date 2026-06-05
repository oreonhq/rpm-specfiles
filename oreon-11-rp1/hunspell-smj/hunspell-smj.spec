%global source0_hash 3626613a2b7ff446dcce1e499012516fa61ebdadb4546bdbc7df420b45470858

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-smj
Summary: Lule Saami hunspell dictionaries
Version: 1.0
Release: 0.33.beta7%{?dist}
URL: http://www.divvun.no/index.html
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-smj)

Source0:        hunspell-smj.tar.gz

%description
Lule Saami hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-1.0beta7.20090316 -a %{SOURCE0}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p smj.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/smj_NO.aff
cp -p smj.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/smj_NO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
smj_NO_aliases="smj_SE"
for lang in $smj_NO_aliases; do
        ln -s smj_NO.aff $lang.aff
        ln -s smj_NO.dic $lang.dic
done
popd

%files
%doc Copyright README GPL-3
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.33.beta7
- Import
