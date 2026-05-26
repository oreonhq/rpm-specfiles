%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-et
Summary: Estonian hunspell dictionaries
%global upstreamid 20030606
Version: 0.%{upstreamid}
Release: 38%{?dist}
Source: http://www.meso.ee/~jjpp/speller/ispell-et_%{upstreamid}.tar.gz
# oreon url source checksums begin
%global source0_sha256 4aea338eef90a977134e81e075277912938ce1a97344d7a0dbf238e274a86116
%global source0_file ispell-et_20030606.tar.gz
# oreon url source checksums end
URL: http://www.meso.ee/~jjpp/speller/
License: LGPL-2.1-or-later AND LPPL-1.3a
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-et)
Provides: hunspell-ee = 0.20030606-4
Obsoletes: hunspell-ee < 0.20030606-4

%description
Estonian hunspell dictionaries.

%package -n hyphen-et
Requires: hyphen
Summary: Estonian hyphenation rules
Supplements: (hyphen and langpacks-et)

%description -n hyphen-et
Estonian hyphenation rules.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ispell-et_20030606.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4aea338eef90a977134e81e075277912938ce1a97344d7a0dbf238e274a86116" || { echo "oreon: Source0 SHA256 mismatch for ispell-et_20030606.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n ispell-et-%{upstreamid}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p latin-1/et_EE.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_et.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_et_EE.dic


%files
%doc README COPYRIGHT ChangeLog
%{_datadir}/%{dict_dirname}/*

%files -n hyphen-et
%doc README COPYRIGHT ChangeLog
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-38
- Prepare for Oreon 11 (RP1)
