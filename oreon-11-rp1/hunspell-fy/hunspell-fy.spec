%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon}
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fy
Summary: Frisian hunspell dictionaries
Version: 3.0.0
Release: 21%{?dist}
Source:        https://addons.mozilla.org/firefox/downloads/file/499875/frysk_wurdboek-3.0.0-tb+fx+sm.xpi
URL: http://www.mozilla-nl.org/projecten/frysk
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fy)

%description
Frisian hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hunspell-fy

%build
for i in README-fy.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i | tr -d '\r' > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/fy-NL.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fy_NL.aff
cp -p dictionaries/fy-NL.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fy_NL.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
fy_NL_aliases="fy_DE"
for lang in $fy_NL_aliases; do
        ln -s fy_NL.aff $lang.aff
        ln -s fy_NL.dic $lang.dic
done
popd


%files
%doc README-fy.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-21
- Import
