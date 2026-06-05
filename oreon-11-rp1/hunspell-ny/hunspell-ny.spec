%global source0_hash 9347a974c1c35e50f47aa0543df86037a05bf6938a3c1e8bc5a4742b82185f21

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif

Name: hunspell-ny
Summary: Chichewa hunspell dictionaries
Epoch: 1
Version: 0.01
Release: 33%{?dist}
URL: http://extensions.services.openoffice.org/en/project/chicspell
License: GPL-3.0-or-later
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell
Supplements: (hunspell and langpacks-ny)

Source0:        https://downloads.sourceforge.net/project/aoo-extensions/4052/0/hunspell-chichewa-ny-dict-0.01.oxt

%description
Chichewa hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
unzip -q %{SOURCE0}

%build
for i in dictionaries/README_ny_MW.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ny_MW.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc dictionaries/README_ny_MW.txt
%license LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.01-33
- Import
