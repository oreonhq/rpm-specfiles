Name: hyphen-fa
Summary: Farsi hyphenation rules
%global upstreamid 20130404
Version: 0.%{upstreamid}
Release: 27%{?dist}
Source: http://mirrors.ctan.org/language/hyphenation/fahyph.zip
URL: http://www.ctan.org/tex-archive/language/hyphenation/fahyph
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-fa)
Patch0: hyphen-fa-cleantex.patch

%description
Farsi hyphenation rules.

%prep
%setup -q -n fahyph
%patch -P0 -p1 -b .clean

%build
substrings.pl fahyph.tex hyph_fa_IR.dic UTF-8
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_fa_IR.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-27
- Prepare for Oreon 11 (RP1)
