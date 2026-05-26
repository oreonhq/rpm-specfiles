%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hr
Summary: Croatian hunspell dictionaries
%global upstreamid 20040608
Version: 0.%{upstreamid}
Release: 36%{?dist}
Epoch: 1
Source: http://cvs.linux.hr/spell/myspell/hr_HR.zip
# oreon url source checksums begin
%global source0_sha256 0e4013ea6b41ad7c14933f5ea15302ef36378d0a4559cbbbe8a411b3e56ee12d
%global source0_file hr_HR.zip
# oreon url source checksums end
URL: http://cvs.linux.hr/spell/
License: LGPL-2.1-or-later OR SISSL
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-hr)

%description
Croatian hunspell dictionaries.

%package -n hyphen-hr
Requires: hyphen
Summary: Croatian hyphenation rules
Supplements: (hyphen and langpacks-hr)

%description -n hyphen-hr
Croatian hyphenation rules.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hr_HR.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0e4013ea6b41ad7c14933f5ea15302ef36378d0a4559cbbbe8a411b3e56ee12d" || { echo "oreon: Source0 SHA256 mismatch for hr_HR.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c -n hunspell-hr

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p hr_HR.dic hr_HR.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hr_HR.dic


%files
%doc README_hr_HR.txt
%{_datadir}/%{dict_dirname}/*

%files -n hyphen-hr
%doc README_hr_HR.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-36
- Prepare for Oreon 11 (RP1)
