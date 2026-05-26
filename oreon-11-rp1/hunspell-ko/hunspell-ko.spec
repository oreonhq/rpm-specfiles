%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ko
Summary: Korean hunspell dictionaries
Version: 0.7.0
Release: 23%{?dist}
Source: https://github.com/spellcheck-ko/hunspell-dict-ko/archive/%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 98ee3400994203680e464a072845da59d31f10281b1e6f092df3503ca5005a16
%global source0_file 0.7.0.tar.gz
# oreon url source checksums end
URL: https://github.com/spellcheck-ko/hunspell-dict-ko
License: MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-only
BuildArch: noarch
BuildRequires: python3
BuildRequires: hunspell
BuildRequires: make
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ko)

%description
Korean hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/0.7.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "98ee3400994203680e464a072845da59d31f10281b1e6f092df3503ca5005a16" || { echo "oreon: Source0 SHA256 mismatch for 0.7.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n hunspell-dict-ko-%{version}

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ko.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ko_KR.aff
cp -p ko.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ko_KR.dic

%check
make test

%files
%doc README.md
%license LICENSE LICENSE.GPL LICENSE.LGPL LICENSE.MPL
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-23
- Prepare for Oreon 11 (RP1)
