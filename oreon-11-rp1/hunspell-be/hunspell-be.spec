%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-be
Summary: Belarusian hunspell dictionaries
Version: 1.1
Release: 34%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/2412/1/dict-be-official.oxt
URL: http://extensions.services.openoffice.org/project/dict-be-official
License: GPL-1.0-or-later AND LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-be)

%description
Belarusian hunspell dictionaries.

%package -n hyphen-be
Requires: hyphen
Summary: Belarusian hyphenation rules
Supplements: (hyphen and langpacks-be)

%description -n hyphen-be
Belarusian hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -n hunspell-be

%build
sed -i -e "s/microsoft-cp1251/CP1251/g" be-official.aff hyph_be_BY.dic
tail -n +3 hyph_be_BY.dic| head -n 3 > README_hyph_be_BY

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p be-official.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/be_BY.aff
cp -p be-official.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/be_BY.dic
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_be_BY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_be_BY.dic


%files
%{_datadir}/%{dict_dirname}/*

%files -n hyphen-be
%doc README_hyph_be_BY
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-34
- Prepare for Oreon 11 (RP1)
