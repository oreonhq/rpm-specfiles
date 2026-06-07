%global source0_hash 364b7cc153f7339461e76666d0810b8a5974bfbdee387096dc0bf130273eeab9

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ia
Summary: Interlingua hunspell dictionaries
%global upstreamid 20240316
Version: 0.%{upstreamid}
Release: 2%{?dist}
# Another URL is https://addons.mozilla.org/en-US/firefox/addon/dict-ia/
URL: https://extensions.openoffice.org/en/project/interlingua-dictionario-orthographic-e-regulas-de-division-de-parolas.html
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ia)

Source0:        https://download.savannah.gnu.org/releases/interlingua/ia_myspell.zip

%description
Interlingua hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c

%build
tr -d '\r' < README_ia.txt > README_ia.txt.new
touch -r README_ia.txt README_ia.txt.new
mv -f README_ia.txt.new README_ia.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ia.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc README_ia.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-2
- Prepare for Oreon 11 (RP1)
