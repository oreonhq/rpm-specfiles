%global source0_hash 9a04ade7f6e7532edebb2582001719c82886884553f15dcba9baf409b9c49420

Name: mythes-pl
Summary: Polish thesaurus
Version: 1.5
Release: 38%{?dist}
Source:        http://downloads.sourceforge.net/synonimy/OOo2-Thesaurus-1.5.zip
# URL is dead now, please don't file bugs to fix it
URL: http://synonimy.ux.pl/
License: LGPL-2.1-only
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-pl)

%description
Polish thesaurus.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build
for i in README_th_pl_PL_v2.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_pl_PL_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc README_th_pl_PL_v2.txt
%{_datadir}/mythes/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5-38
- Import
