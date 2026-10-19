%global source0_hash eea6c1008b00209e47013861cb93f5882be1dd730ceaa5aa2b4ef4bd834f9e33
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon} >= 11
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-xh
Summary:        Xhosa hunspell dictionaries
%global upstreamid 20091030
Version: 0.%{upstreamid}
Release:        1%{?dist}
URL: https://extensions.openoffice.org/en/project/xhosa-spell-checker
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-xh)
Source0:        https://downloads.sourceforge.net/project/aoo-extensions/3133/0/dict-xh_za-2009.10.30.oxt
# oreon:deps

# /oreon:deps
%description
Xhosa hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n hunspell-xh

%build

for i in README-xh_ZA.txt release-notes-xh_ZA.txt package-description.txt; do
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
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-33
- Prepare for Oreon 11 (RP1)
