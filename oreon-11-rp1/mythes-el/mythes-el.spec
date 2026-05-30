%global source0_hash e24d4f382d09ad38a6fa0631d084f77d9ddfc2c2836ec8b7193894db90372dd3

Name: mythes-el
Summary: Greek thesaurus
%global upstreamid 20070412
Version: 0.%{upstreamid}
Release: 37%{?dist}
# below links are dead and can't find any mirror for it
# please don't report any FTBFS bugs
#Source: http://www.ellak.gr/pub/oo_extras/th_el.zip
Source:        http://www.ellak.gr/pub/oo_extras/th_el.zip
URL: wiki.services.openoffice.org/wiki/Dictionaries
License: GPL-2.0-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-el)

%description
Greek thesaurus.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build
for i in README_th_el_GR_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-7 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_el_GR_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s th_el_GR_v2.dat "th_"$lang"_v2.dat"
        ln -s th_el_GR_v2.idx "th_"$lang"_v2.idx"
done


%files
%doc README_th_el_GR_v2.txt
%{_datadir}/mythes/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070412-37
- Import
