%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-wa
Summary: Walloon hunspell dictionaries
Version: 0.4.17
Release: 28%{?dist}
Source0: http://chanae.walon.org/walon/aspell-wa-%{version}.tar.bz2
URL: http://chanae.walon.org/walon/aspell.php
License: LGPL-2.1-or-later
BuildArch: noarch
Patch0: hunspell-wa-0.4.15-buildfix.patch

BuildRequires: make

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-wa)

%description
Walloon hunspell dictionaries.

%prep
%setup -q -n aspell-wa-%{version}
%patch -P0 -p1 -b .buildfix

%build
make myspell
for i in TODO README; do
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
cp -p wa.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/wa_BE.dic
cp -p wa.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/wa_BE.aff


%files
%doc README LGPL ChangeLog TODO
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.17-28
- Prepare for Oreon 11 (RP1)
