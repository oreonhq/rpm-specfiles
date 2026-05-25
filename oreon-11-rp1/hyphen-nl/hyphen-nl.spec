Name: hyphen-nl
Summary: Dutch hyphenation rules
%global upstreamid 20050617
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_nl_NL.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL-2.0-only
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-nl)

%description
Dutch hyphenation rules.

%prep
%autosetup -c -n hyphen-nl

%build
for i in README_hyph_nl_NL.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_nl_NL.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s hyph_nl_NL.dic hyph_$lang.dic
done


%files
%doc README_hyph_nl_NL.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20050617-36
- Import
