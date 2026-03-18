Name: hyphen-ca
Summary: Catalan hyphenation rules
Epoch: 1
Version: 1.5
Release: 7%{?dist}
Source: https://github.com/jaumeortola/hyphen-ca/archive/refs/tags/v1.5.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/jaumeortola/hyphen-ca
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-ca)

%description
Catalan hyphenation rules.

%prep
%autosetup

%build
for i in office/release-note_en.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p office/hyph_ca_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_ca_ES.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s hyph_ca_ES.dic hyph_$lang.dic
done
popd


%files
%doc office/release-note_en.txt README.md
%license office/gpl.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5-7
- Prepare for Oreon 11 (RP1)
