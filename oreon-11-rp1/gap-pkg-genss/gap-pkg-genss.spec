%global source0_hash 001355e8d7add19febf86e7d9eb0f74979fa6e03312cbbf65434584cd28d2200

%global gap_pkgname genss
%global giturl      https://github.com/gap-packages/genss

Name:           gap-pkg-%{gap_pkgname}
Version:        1.6.9
Release:        %autorelease
Summary:        Randomized Schreier-Sims algorithm

License:        GPL-3.0-or-later
URL:            https://gap-packages.github.io/genss/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples gap test tst
BuildOption(check): tst/testall.g

# The AtlasRep, TomLib, and CtblLib dependencies are needed for the tests only
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-orb-doc
BuildRequires:  gap-pkg-tomlib

Requires:       gap-pkg-orb

Recommends:     gap-pkg-io

%description
The genss package implements the randomized Schreier-Sims algorithm to compute
a stabilizer chain and a base and strong generating set for arbitrary finite
groups.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Genss documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-orb-doc

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Fix encodings
for fil in init.g read.g; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%files
%doc CHANGES README
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/test/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
