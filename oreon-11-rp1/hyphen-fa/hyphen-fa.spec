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
# oreon url source checksums begin
%global source0_sha256 f9a5ed8222b2688829b7ed530fb6b7e4fce8b051cc8f79ed36b64939bf632c29
%global source0_file fahyph.zip
# oreon url source checksums end

%description
Farsi hyphenation rules.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/fahyph.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f9a5ed8222b2688829b7ed530fb6b7e4fce8b051cc8f79ed36b64939bf632c29" || { echo "oreon: Source0 SHA256 mismatch for fahyph.zip" >&2; exit 1; })
# oreon verify url source checksums end
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
