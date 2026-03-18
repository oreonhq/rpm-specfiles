Name: mythes-sl
Summary: Slovenian thesaurus
%global upstreamid 20130130
Version: 0.%{upstreamid}
Release: 29%{?dist}
Source: http://88.200.20.8:85/download/thes_sl_SI_v2.zip
URL: http://www.tezaver.si/
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-sl)

%description
Slovenian thesaurus.

%prep
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
