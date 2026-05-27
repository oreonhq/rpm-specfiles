%global source0_hash none

Name: mythes-hu
Summary: Hungarian thesaurus
%global upstreamid 20101019
Version: 0.%{upstreamid}
Release: 33%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/1283/9/dict-hu.oxt
URL: http://extensions.services.openoffice.org/project/hu_dicts
#bundled but unused spell-checking stuff is under GPLv2+ or LGPLv2+ or MPLv1.1
#base for bundled but unused hyphenation stuff is under GPLv2
#additional patch to unused hyphenation stuff is MPL/GPL/LGPL
License: GPL-2.0-or-later AND ( GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 ) AND GPL-2.0-only AND ( GPL-1.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 )
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-hu)

%description
Hungarian thesaurus.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_hu_HU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc README_th_hu_HU_v2.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-33
- Prepare for Oreon 11 (RP1)
