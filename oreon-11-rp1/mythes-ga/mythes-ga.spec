Name: mythes-ga
Summary: Irish thesaurus
%global upstreamid 20071001
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/thes_ga_IE_v2.zip
URL: https://cadhan.com/lsg/index-en.html
BuildRequires: unzip
License: GFDL-1.2-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-ga)

%description
Irish thesaurus.

%prep
%autosetup -c

%build
for i in README_th_ga_IE_v2.txt; do
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
cp -p th_ga_IE_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc README_th_ga_IE_v2.txt
%{_datadir}/mythes/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20071001-37
- Import
