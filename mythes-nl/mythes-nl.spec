Name: mythes-nl
Summary: Dutch thesaurus
%global upstreamid 20130131
Version: 0.%{upstreamid}
Release: 27%{?dist}
Source: http://data.opentaal.org/opentaalbank/thesaurus/download/thes_nl.oxt
URL: http://data.opentaal.org/opentaalbank/thesaurus
License: BSD-2-Clause OR CC-BY-3.0

BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-nl)

%description
Dutch thesaurus.

%prep
%setup -q -c

%build
for i in README_th_nl.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_nl_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_nl_NL_v2.dat
cp -p th_nl_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_nl_NL_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s th_nl_NL_v2.dat "th_"$lang"_v2.dat"
        ln -s th_nl_NL_v2.idx "th_"$lang"_v2.idx"
done


%files
%doc README_th_nl.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-27
- Prepare for Oreon 11 (RP1)
