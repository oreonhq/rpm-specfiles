%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ber
Summary: Amazigh hunspell dictionaries
%global upstreamid 20080210
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: http://ayaspell.sourceforge.net/data/hunspell-am_test.tar.gz
# oreon url source checksums begin
%global source0_sha256 fc55dd5fad595312eed80a0418d5a0210fc08bc2e281fa262edaee41700ddb89
%global source0_file hunspell-am_test.tar.gz
# oreon url source checksums end
URL: http://ayaspell.sourceforge.net/am.html
License: GPL-1.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ber)

%description
Amazigh hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hunspell-am_test.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fc55dd5fad595312eed80a0418d5a0210fc08bc2e281fa262edaee41700ddb89" || { echo "oreon: Source0 SHA256 mismatch for hunspell-am_test.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n spelling_tifinagh

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p tifinagh.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ber_MA.dic
cp -p tifinagh.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ber_MA.aff


%files
%doc README
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-34
- Prepare for Oreon 11 (RP1)
