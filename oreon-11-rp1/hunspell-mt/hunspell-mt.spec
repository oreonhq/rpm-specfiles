%global source0_hash 509d3b4708636d85c3900af66e2da74b729ccc28361e54913ca2ff42f2ec1c4c
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon} >= 11
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-mt
Summary:        Maltese hunspell dictionaries
%global upstreamid 20110414
Version: 0.%{upstreamid}
Release:        1%{?dist}
URL: https://extensions.openoffice.org/en/project/maltese-spell-check-dictionary
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mt)
Source0:        https://downloads.sourceforge.net/project/aoo-extensions/5039/0/dict-mt-2011-04-14.oxt
# oreon:deps
BuildRequires:  hunspell-devel
# /oreon:deps
%description
Maltese hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
unzip -q %{SOURCE0}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p mt.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/mt_MT.dic
cp -p mt.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/mt_MT.aff
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-20
- Prepare for Oreon 11 (RP1)
