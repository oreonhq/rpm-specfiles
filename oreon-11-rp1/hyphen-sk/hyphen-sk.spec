Name: hyphen-sk
Summary: Slovak hyphenation rules
%global upstreamid 20031227
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_sk_SK.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL-1.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-sk)

%description
Slovak hyphenation rules.

%prep
%autosetup -c

%build
chmod -x *
for i in README_hyph_sk_SK.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_sk_SK.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-36
- Prepare for Oreon 11 (RP1)
