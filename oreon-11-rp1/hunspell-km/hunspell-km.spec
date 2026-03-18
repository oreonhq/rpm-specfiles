%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-km
Summary: Khmer hunspell dictionaries
Version: 1.82
Release: 20%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/2250/6/sbbic-khmer-spelling-checker-1.82.oxt
URL: http://www.sbbic.org/
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-km)

%description
Khmer hunspell dictionaries.

%prep
%autosetup -c -n hunspell-km

%build
for i in CHANGELOG; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p km_KH.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc CHANGELOG
%license LICENCES-*.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.82-20
- Prepare for Oreon 11 (RP1)
