%global source0_hash 746d1366289550dce84428987105ea9ef07ebe8934d73da0b982f40164be8a13

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-zu
Summary: Zulu hunspell dictionaries
%global upstreamid 20100126
Version: 0.%{upstreamid}
Release: 35%{?dist}
URL: https://extensions.openoffice.org/en/project/zulu-spell-checker
# There is no License information in this new sourceforge Source: archive
# Based on old gone upstream archive, Let's keep GPLv3+ license
# old and new archive .dic and .aff contents are same
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-zu)

Source0:        https://downloads.sourceforge.net/project/aoo-extensions/3132/3/dict-zu_za-2010.01.26.oxt

%description
Zulu hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
unzip -q %{SOURCE0}

%build
for i in README-zu_ZA.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p zu_ZA.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/zu.aff
cp -p zu_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/zu.dic

%files
%doc README-zu_ZA.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-35
- Prepare for Oreon 11 (RP1)
