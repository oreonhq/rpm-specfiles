%global source0_hash none

Name: mythes-da
Summary: Danish thesaurus
%global upstreamid 20100629.15.16
Version: 0.%{upstreamid}
Release: 32%{?dist}
Source: https://excellmedia.dl.sourceforge.net/project/aoo-extensions/1388/12/danskesynonymer.oxt
URL: https://extensions.openoffice.org/fr/project/danske-synonymer
License: GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-da)

%description
Danish thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c

%build
for i in README_th_da_DK.txt README_th_da_DK.txt README_th_en-US.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_da_DK.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_da_DK_v2.dat
cp -p th_da_DK.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_da_DK_v2.idx


%files
%doc README_th_da_DK.txt README_th_en-US.txt release_note.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-32
- Prepare for Oreon 11 (RP1)
