%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ln
Summary: Lingala hunspell dictionaries
Version: 0.02
Release: 33%{?dist}
Source: http://downloads.sourceforge.net/lingala/hunspell-ln-0.02.zip
# oreon url source checksums begin
%global source0_sha256 0b6d81e21fc135be71e0af1a89523e6ce910841cfe7db2a9917fbcbb6f0625fa
%global source0_file hunspell-ln-0.02.zip
# oreon url source checksums end
URL: http://lingala.sourceforge.net/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ln)

%description
Lingala hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hunspell-ln-0.02.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0b6d81e21fc135be71e0af1a89523e6ce910841cfe7db2a9917fbcbb6f0625fa" || { echo "oreon: Source0 SHA256 mismatch for hunspell-ln-0.02.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ln_CD.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_ln_CD.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.02-33
- Prepare for Oreon 11 (RP1)
