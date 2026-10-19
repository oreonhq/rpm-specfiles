%global source0_hash 10aaa364d795256d3e321e344432bb00d82f40dbaebab03884d0febad16645af
Name: mythes-sl
Summary:        Slovenian thesaurus
%global upstreamid 20130130
Version: 0.%{upstreamid}
Release:        1%{?dist}
Source0:        http://88.200.20.8:85/download/thes_sl_SI_v2.zip
URL: http://www.tezaver.si/
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-sl)
# oreon:deps

# /oreon:deps
%description
Slovenian thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
