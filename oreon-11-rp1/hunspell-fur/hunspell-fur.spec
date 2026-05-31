%global source0_hash aa3edd8dc51611fb732923817bec962c50bbe9556d988050f69952e08cb63218

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fur
Summary: Friulian hunspell dictionaries
%global upstreamid 20050912
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source: http://digilander.libero.it/paganf/coretors/myspell-fur-12092005.zip
URL: http://digilander.libero.it/paganf/coretors/dizionaris.html
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fur)

%description
Friulian hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n myspell-fur-12092005

%build
chmod -x *
for i in COPYING.txt LICENCE.txt LEIMI.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-15 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p fur_IT.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc COPYING.txt LEIMI.txt LICENCE.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-35
- Prepare for Oreon 11 (RP1)
