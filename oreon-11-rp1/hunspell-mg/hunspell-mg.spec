%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-mg
Summary: Malagasy hunspell dictionaries
%global upstreamid 20050109
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/mg_MG.zip
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mg)

%description
Malagasy hunspell dictionaries.

%prep
%autosetup -c -n hunspell-mg

%build
for i in README_mg_MG.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p mg_MG.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/plt.aff
cp -p mg_MG.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/plt.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
plt_aliases="mg"
for lang in $plt_aliases; do
        ln -s plt.aff $lang.aff
        ln -s plt.dic $lang.dic
done
popd


%files
%doc README_mg_MG.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-37
- Prepare for Oreon 11 (RP1)
