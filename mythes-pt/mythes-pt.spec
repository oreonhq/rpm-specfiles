Name: mythes-pt
Summary: Portuguese thesaurus
%global upstreamid 20060817
Version: 0.%{upstreamid}
Release: 39%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/thes_pt_PT_v2.zip
URL: http://download.services.openoffice.org/contrib/dictionaries
BuildRequires: unzip
License: GPL-2.0-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-pt)

%description
Portuguese thesaurus.

%prep
%autosetup -c

%build
for i in README_th_pt_PT_v2.txt; do
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
cp -p th_pt_PT_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
pt_PT_aliases="pt_AO pt_BR"
for lang in $pt_PT_aliases; do
        ln -s th_pt_PT_v2.dat "th_"$lang"_v2.dat"
        ln -s th_pt_PT_v2.idx "th_"$lang"_v2.idx"
done


%files
%doc README_th_pt_PT_v2.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-39
- Prepare for Oreon 11 (RP1)
