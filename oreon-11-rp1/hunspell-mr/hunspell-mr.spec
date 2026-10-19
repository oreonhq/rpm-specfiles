%global source0_hash 0a49b0ea373bffafc87eb9b2e42f40b4ea8d9101f58c2449c875a7389b586e75
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon} >= 11
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-mr
Summary:        Marathi hunspell dictionaries
Version: 15.02webext
Release:        1%{?dist}
Epoch: 1
URL: https://addons.mozilla.org/en-US/firefox/addon/marathi-dictionary/
License: GPL-3.0-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mr)
Source0:        https://anishpatil.fedorapeople.org/mr_in.1.0.0.tar.gz
# oreon:deps

# /oreon:deps
%description
Marathi hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n mr_IN

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p mr_IN/mr_IN.dic mr_IN/mr_IN.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.02webext-2
- Prepare for Oreon 11 (RP1)
