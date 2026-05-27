%global source0_hash none

Name: hyphen-ku
Summary: Kurdish hyphenation rules
Version: 1.71.2
Release: 33%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/2445/12/kitandin.oxt
URL: http://extensions.services.openoffice.org/project/kitandin
License: GPL-2.0-or-later OR LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-ku)

%description
Kurdish hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hyphen-ku

%build
chmod -x *.dic *.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ku.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_ku_TR.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen
ku_TR_aliases="ku_SY"
for lang in $ku_TR_aliases; do
        ln -s hyph_ku_TR.dic hyph_$lang.dic
done
popd


%files
%doc README_ku.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.71.2-33
- Prepare for Oreon 11 (RP1)
