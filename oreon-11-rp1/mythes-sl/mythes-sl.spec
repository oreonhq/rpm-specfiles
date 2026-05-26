Name: mythes-sl
Summary: Slovenian thesaurus
%global upstreamid 20130130
Version: 0.%{upstreamid}
Release: 29%{?dist}
Source: http://88.200.20.8:85/download/thes_sl_SI_v2.zip
# oreon url source checksums begin
%global source0_sha256 fdf44de7c1c3f0f062cd7bdd7c0ffa7360bd0d865cdc22d16caf791481b89e03
%global source0_file thes_sl_SI_v2.zip
# oreon url source checksums end
URL: http://www.tezaver.si/
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-sl)

%description
Slovenian thesaurus.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/thes_sl_SI_v2.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fdf44de7c1c3f0f062cd7bdd7c0ffa7360bd0d865cdc22d16caf791481b89e03" || { echo "oreon: Source0 SHA256 mismatch for thes_sl_SI_v2.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -c

%build
chmod -x *
for i in README_th_sl_SI_v2.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_sl_SI_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc README_th_sl_SI_v2.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-29
- Prepare for Oreon 11 (RP1)
