%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-mos
Summary: Mossi hunspell dictionaries
%global upstreamid 20101130
Version: 0.%{upstreamid}
Release: 32%{?dist}
Source: http://www.abcburkina.net/ancien/documents/lingu/DicoMoore.zip
# oreon url source checksums begin
%global source0_sha256 d9366f7e8baa913cb88de96c056fcc814c515283dcb083f8010d2f8bff681589
%global source0_file DicoMoore.zip
# oreon url source checksums end
URL: http://www.abcburkina.net/content/view/377/48/lang,fr
License: LGPL-3.0-only
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mos)

%description
Mossi hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/DicoMoore.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d9366f7e8baa913cb88de96c056fcc814c515283dcb083f8010d2f8bff681589" || { echo "oreon: Source0 SHA256 mismatch for DicoMoore.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p mos_BF.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc lgpl-3.0.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-32
- Prepare for Oreon 11 (RP1)
