%global source0_hash f9a5ed8222b2688829b7ed530fb6b7e4fce8b051cc8f79ed36b64939bf632c29

Name: hyphen-fa
Summary: Farsi hyphenation rules
%global upstreamid 20130404
Version: 0.%{upstreamid}
Release: 27%{?dist}
Source:        https://mirror.ctan.org/language/hyphenation/fahyph.zip
URL: http://www.ctan.org/tex-archive/language/hyphenation/fahyph
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-fa)

%description
Farsi hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20130404-27
- Import
