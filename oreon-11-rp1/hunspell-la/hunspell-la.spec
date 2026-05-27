%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-la
Summary: Latin hunspell dictionaries
%global upstreamid 20130331
Version: 0.%{upstreamid}
Release: 30%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/1141/3/dict-la_2013-03-31.oxt
URL: http://extensions.services.openoffice.org/project/dict-la
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-la)

%description
Latin hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hunspell-la

%build
for i in README_extension_owner-la.txt la/README_la.txt la/COPYING*; do
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
cp -p la/la.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/la.dic
cp -p la/la.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/la.aff


%files
%doc README_extension_owner-la.txt la/README_la.txt
%license la/COPYING_*
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-30
- Prepare for Oreon 11 (RP1)
