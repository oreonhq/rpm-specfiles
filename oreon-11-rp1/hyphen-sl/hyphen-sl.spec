%global source0_hash 306e375a4113992053c066c1a5e2574b2f1787e1ff75c2c23c2a7cd5f6ce65b5
Name: hyphen-sl
Summary:        Slovenian hyphenation rules
%global upstreamid 20070127
Version: 0.%{upstreamid}
Release:        1%{?dist}
Source0:        http://download.services.openoffice.org/contrib/dictionaries/hyph_sl_SI.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-sl)
# oreon:deps

# /oreon:deps
%description
Slovenian hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hyphen-sl
%oreon_prep
%build

chmod -x *
%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sl_SI.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070127-34
- Import
