%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ku
Summary: Kurdish hunspell dictionaries
Version: 0.21
Release: 37%{?dist}
#http://hunspell-ku.googlecode.com/files/ku_TR-021_source.zip ?
Source0: http://downloads.sourceforge.net/myspellkurdish/ku_TR-021.zip
#http://code.google.com/p/hunspell-ku/ ?
URL: https://sourceforge.net/projects/myspellkurdish/
License: GPL-3.0-only OR LGPL-3.0-only OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ku)

%description
Kurdish hunspell dictionaries.

%prep
%setup -q -n ku_TR

%build
for i in README_ku_TR.txt; do
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
cp -p ku_TR.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ku_TR_aliases="ku_SY"
for lang in $ku_TR_aliases; do
        ln -s ku_TR.aff $lang.aff
        ln -s ku_TR.dic $lang.dic
done
popd


%files
%doc README_ku_TR.txt gpl-3.0.txt lgpl-3.0.txt MPL-1.1.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.21-37
- Prepare for Oreon 11 (RP1)
