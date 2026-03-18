Name: mythes-ca
Summary: Catalan thesaurus
Version: 2.3.1
Release: 7%{?dist}
Source: https://github.com/Softcatala/sinonims-cat/releases/latest/download/thesaurus-ca.oxt
URL: http://www.softcatala.org/wiki/Projectes/Openthesaurus-ca
License: CC-BY-4.0
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-ca)

%description
Catalan thesaurus.

%prep
%setup -q -c

%build
for i in release_note-ca.txt dictionaries/README_th_ca.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_ca_ES.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ca_ES_v2.dat
cp -p dictionaries/th_ca_ES.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ca_ES_v2.idx
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s th_ca_ES_v2.dat "th_"$lang"_v2.dat"
        ln -s th_ca_ES_v2.idx "th_"$lang"_v2.idx"
done
popd


%files
%doc dictionaries/README_th_ca.txt LICENCES-fr.txt LICENSES-en.txt LICENCIAS-es.txt LLICENCIES-ca.txt release_note-ca.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.1-7
- Prepare for Oreon 11 (RP1)
