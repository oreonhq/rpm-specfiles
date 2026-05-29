%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hil
Summary: Hiligaynon hunspell dictionaries
Epoch: 1
Version: 0.14
Release: 33%{?dist}
Source:        https://addons.mozilla.org/firefox/downloads/file/108895/litreoir_hiligaynon-%{version}-tb+fx+sm.xpi
URL: http://extensions.services.openoffice.org/project/hunspell-hil
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-hil)

%description
Hiligaynon hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build
for i in dictionaries/README_hil_PH.txt; do
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
cp -p dictionaries/hil.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/hil_PH.dic
cp -p dictionaries/hil.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/hil_PH.aff


%files
%doc dictionaries/README_hil_PH.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.14-33
- Import
