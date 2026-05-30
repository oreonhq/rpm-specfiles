%global source0_hash b5f4b671c2d002b69e6cf766a429237cfe872ef64ca315ca0863422e7e0f2393

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sl
Summary: Slovenian hunspell dictionaries
%global upstreamid 20070127
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source:        http://download.services.openoffice.org/contrib/dictionaries/sl_SI.zip
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
License: GPL-1.0-or-later OR LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-sl)

%description
Slovenian hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hunspell-sl

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_sl_SI.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070127-37
- Import
