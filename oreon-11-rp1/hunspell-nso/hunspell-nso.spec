%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-nso
Summary: Northern Sotho hunspell dictionaries
%global upstreamid 20091201
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/3139/1/dict-ns_za-2009.12.01.oxt
URL: https://extensions.openoffice.org/en/project/northern-sotho-spell-checker
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-nso)

%description
Northern Sotho hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hunspell-nso

%build
for i in README-ns_ZA.txt package-description.txt release-notes-ns_ZA.txt; do
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
cp -p ns_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/nso_ZA.dic
cp -p ns_ZA.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/nso_ZA.aff


%files
%doc README-ns_ZA.txt package-description.txt release-notes-ns_ZA.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-34
- Prepare for Oreon 11 (RP1)
