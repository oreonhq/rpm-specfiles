%global dict_dirname hunspell 
Name: hunspell-en
Summary: English hunspell dictionaries
%global upstreamid 20201207
Version: 0.%{upstreamid}
Release: 13%{?dist}
Source0: https://github.com/en-wl/wordlist/archive/rel-2020.12.07.tar.gz
Source1: http://download.services.openoffice.org/contrib/dictionaries/en_GB.zip
#See http://mxr.mozilla.org/mozilla/source/extensions/spellcheck/locales/en-US/hunspell/mozilla_words.diff?raw=1
Patch0: mozilla_words.patch
Patch1: en_GB-singleletters.patch
Patch2: en_GB.two_initial_caps.patch
#See https://github.com/en-wl/wordlist/issues/15
#filter removes words with "." in them
Patch3: en_US-strippedabbrevs.patch
#See https://sourceforge.net/p/hunspell/patches/35
#to allow "didn't" instead of suggesting change to typographical apostrophe
Patch4: hunspell-en-allow-non-typographical.marks.patch
#See https://bugzilla.redhat.com/show_bug.cgi?id=619577 add SI and IEC prefixes
Patch5: hunspell-en-SI_and_IEC.patch
#See https://github.com/en-wl/wordlist/issues/46 obscure Calender hides misspelling of Calendar
Patch6: hunspell-en-calender.patch
#valid English words that are archaic or rare in en-GB but not in en-IE
Patch7: en_IE.supplemental.patch
#call git to get the release hash, but this is a tarball
Patch8: hunspell-en-dont-call-git-during-build.patch
#rhbz#1492306 for better or worse treat etc the same in US and GB
Patch9: en_GB.etc.patch
Patch10: hunspell-en-buildfix.patch
URL: http://wordlist.sourceforge.net/
# README_en_GB.txt has specified just LGPL which mean LGPLv2+
# scowl/speller/aspell/en_affix.dat is BSD
# scowl/speller/aspell/en_phonet.dat is LGPLv2
License: LGPL-2.1-or-later AND LGPL-2.1-only AND BSD-3-Clause-Modification
BuildArch: noarch
BuildRequires: aspell, zip, dos2unix, perl-Getopt-Long, gcc-c++
BuildRequires: make
Requires: hunspell-en-US = %{version}-%{release}
Requires: hunspell-en-GB = %{version}-%{release}
%if 0%{?rhel}
Requires: hunspell
%else
Supplements: (hunspell or nuspell)
%endif
Supplements: langpacks-en

%description
English (US, UK, etc.) hunspell dictionaries

%package US
Requires: hunspell-filesystem
%if 0%{?rhel}
Requires: hunspell
%else
Recommends: (hunspell or nuspell)
%endif
Summary: US English hunspell dictionaries

%description US
US English hunspell dictionaries

%package GB
Requires: hunspell-filesystem
%if 0%{?rhel}
Requires: hunspell
Supplements: hunspell
%else
Recommends: (hunspell or nuspell)
Supplements: (hunspell or nuspell)
%endif
Supplements: langpacks-en_GB
Summary: UK English hunspell dictionaries

%description GB
UK English hunspell dictionaries

%prep
%setup -q -n wordlist-rel-2020.12.07
%setup -q -T -D -a 1 -n wordlist-rel-2020.12.07
%patch -P 0 -p0 -b .mozilla
%patch -P 1 -p1 -b .singleletters
%patch -P 2 -p1 -b .two_initial_cap
%patch -P 3 -p0 -b .strippedabbrevs
%patch -P 4 -p0 -b .allow-non-typographical
%patch -P 5 -p0 -b .SI_and_IEC
%patch -P 6 -p1 -b .calender
%patch -P 7 -p1 -b .en_IE
%patch -P 8 -p1 -b .nogit
%patch -P 9 -p1 -b .etc
%patch -P 10 -p1 -b .buildfix

%build
export PERL5LIB=`pwd`/scowl/r/varcon${PERL5LIB:+:${PERL5LIB}}
make
cd scowl/speller
make hunspell
for i in README_en_CA.txt README_en_US.txt; do
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
cp -p en_??.dic en_??.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cd scowl/speller
cp -p en_??.dic en_??.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
en_GB_aliases="en_AG en_BS en_BW en_BZ en_DK en_GH en_HK en_IE en_IN en_JM en_MW en_NA en_NG en_NZ en_SG en_TT en_ZA en_ZM en_ZW"
for lang in $en_GB_aliases; do
	ln -s en_GB.aff $lang.aff
	ln -s en_GB.dic $lang.dic
done
en_US_aliases="en_PH"
for lang in $en_US_aliases; do
	ln -s en_US.aff $lang.aff
	ln -s en_US.dic $lang.dic
done
popd


%files
%doc scowl/speller/README_en_CA.txt
%{_datadir}/%{dict_dirname}/*
%exclude %{_datadir}/%{dict_dirname}/en_GB.*
%exclude %{_datadir}/%{dict_dirname}/en_US.*

%files US
%doc scowl/speller/README_en_US.txt
%{_datadir}/%{dict_dirname}/en_US.*

%files GB
%doc README_en_GB.txt
%{_datadir}/%{dict_dirname}/en_GB.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-13
- Prepare for Oreon 11 (RP1)
