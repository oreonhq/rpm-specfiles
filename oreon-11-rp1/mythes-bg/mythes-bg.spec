%global source0_hash 48489358065feee858d4f068b3c6fecbda6372df2c68383212fd947f29c74496

Name: mythes-bg
Summary: Bulgarian thesaurus
Version: 4.3
Release: 31%{?dist}
Source:        http://downloads.sourceforge.net/sourceforge/bgoffice/OOo-thes-bg-%{version}.zip
Requires: mythes
Supplements: (mythes and langpacks-bg)
URL: http://bgoffice.sourceforge.net/
BuildRequires: unzip
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

%description
Bulgarian thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n OOo-thes-bg-%{version}

%build
for i in ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
echo "UTF-8" > th_bg_BG.dat.new
tail -n +2 th_bg_BG.dat | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> th_bg_BG.dat.new
mv th_bg_BG.dat.new th_bg_BG.dat
echo "UTF-8" > th_bg_BG.idx.new
tail -n +2 th_bg_BG.idx | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> th_bg_BG.idx.new
mv th_bg_BG.idx.new th_bg_BG.idx

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_bg_BG.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_bg_BG_v2.dat
cp -p th_bg_BG.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_bg_BG_v2.idx


%files
%doc ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3-31
- Prepare for Oreon 11 (RP1)
