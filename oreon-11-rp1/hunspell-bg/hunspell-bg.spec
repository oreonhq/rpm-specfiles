%global source0_hash 33c71a42faf1e247d112450c932d41ecae2fc584e17face60c5731376ee83168

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-bg
Summary: Bulgarian hunspell dictionaries
Version: 4.3
Release: 33%{?dist}
Source:        http://downloads.sourceforge.net/bgoffice/OOo-spell-bg-%{version}.zip
URL: http://bgoffice.sourceforge.net/
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-bg)

%description
Bulgarian hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n OOo-spell-bg-%{version}

%build
for i in README.bulgarian GPL-2.0.txt MPL-1.1.txt ChangeLog Copyright LGPL-2.1.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

iconv -f WINDOWS-1251 -t UTF-8 bg_BG.dic > bg_BG.dic.new
mv -f bg_BG.dic.new bg_BG.dic
echo "SET UTF-8" > bg_BG.aff.new
tail -n +2 bg_BG.aff | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> bg_BG.aff.new
mv bg_BG.aff.new bg_BG.aff

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc ChangeLog Copyright README.bulgarian
%license GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3-33
- Prepare for Oreon 11 (RP1)
