%global source0_hash c04b432b088edabc8ff025049535077722869f842fb6f851864106b7f4f03527

# SPDX-License-Identifier: MIT
Version:        2.0
Release:        %autorelease
URL:            https://pcaro.es/p/hermit

%global foundry		pcaro	
%global	fontlicense	OFL-1.1-RFN

%global	fontfamily	Hermit
%global	fontsummary	Hermit monospace fonts
%global	fonts		*.otf
%global	fontconfngs	%{SOURCE10}
%global fontdescription	%{expand:
Hermit is a monospace font designed to be clear, pragmatic and very readable.
Its creation has been focused on programming. Every glyph was carefully planned
and calculated, according to defined principles and rules. For this reason,
Hermit is coherent and regular.}

Source0:	https://pcaro.es/d/otf-hermit-%{version}.tar.gz
Source10:	60-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
