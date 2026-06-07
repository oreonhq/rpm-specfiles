%global source0_hash c166ad07d50e9e13ac9f87d5a8938b3f675a0f8a01017bd8969c2053e7f52298

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-csb
Summary: Kashubian hunspell dictionaries
# We are using here upstreamid date as upstream published source archive date
%global upstreamid 20190319
Version: 0.%{upstreamid}
Release: 8%{?dist}
URL: https://addons.thunderbird.net/en-us/firefox/addon/kashubian-spell-checker-poland/
License: GPL-2.0-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-csb)

Source0:        https://mirrors.kernel.org/gnu/aspell/dict/csb/aspell6-csb-0.02-0.tar.bz2

%description
Kashubian hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n aspell6-csb-0.02-0

%build
export LANG=csb_PL.utf8
preunzip csb.cwl
wordlist2hunspell csb.wl csb_PL
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
