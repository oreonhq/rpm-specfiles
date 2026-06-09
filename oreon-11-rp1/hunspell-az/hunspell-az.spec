%global source0_hash 063176ec459d61acd59450ae49b5076e42abb1dcd54c1f934bae5fa6658044c3

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-az
Summary: Azerbaijani hunspell dictionaries
# date is derived from upstream az.dic file timestamp
%global upstreamid 20180807
Version: 0.%{upstreamid}
Release: 9%{?dist}
URL: https://github.com/mozillaz/spellchecker/
License: MPL-2.0
BuildArch: noarch
BuildRequires: aspell hunspell hunspell-devel

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-az)

Source0:        https://mirrors.kernel.org/gnu/aspell/dict/az/aspell6-az-0.02-0.tar.bz2

%description
Azerbaijani hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n aspell6-az-0.02-0

%build
export LANG=az_AZ.utf8
preunzip az.cwl
wordlist2hunspell az.wl az_AZ
for i in Copyright doc/Crawler.txt; do
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
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc COPYING Copyright README doc/Crawler.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-8
- Prepare for Oreon 11 (RP1)
