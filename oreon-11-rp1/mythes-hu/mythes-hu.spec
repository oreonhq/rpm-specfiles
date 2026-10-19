%global source0_hash f5094e76f5cd77876f5766d302853845774b97c47aef51d815f37668b94d07bb
Name: mythes-hu
Summary:        Hungarian thesaurus
%global upstreamid 20101019
Version: 0.%{upstreamid}
Release:        1%{?dist}
Source0:        https://downloads.sourceforge.net/project/aoo-extensions/1283/9/dict-hu.oxt
URL: http://extensions.services.openoffice.org/project/hu_dicts
License: GPL-2.0-or-later AND ( GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 ) AND GPL-2.0-only AND ( GPL-1.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 )
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-hu)
# oreon:deps

# /oreon:deps
%description
Hungarian thesaurus.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_hu_HU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-33
- Prepare for Oreon 11 (RP1)
