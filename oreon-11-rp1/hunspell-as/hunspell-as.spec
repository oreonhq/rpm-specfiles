%global source0_hash 45feab20738dfd3be29d62629ef792c61a86c05a27f89f84b491adf9413f3fa2

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-as
Summary: Assamese hunspell dictionaries
Epoch: 1
Version: 1.0.1.2resigned1
Release: 3%{?dist}
URL: https://addons.mozilla.org/en-US/firefox/addon/assamese-spell-checker/
# license tag explicitly mentioned on website
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-as)

Source0:        https://downloads.sourceforge.net/project/aoo-extensions/2318/4/as_in.oxt

%description
Assamese hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n hunspell-as

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p as_IN.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

%files
%doc README_as_IN.txt
%license COPYING COPYING.MPL COPYING.GPL COPYING.LGPL
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1.2resigned1-3
- Prepare for Oreon 11 (RP1)
