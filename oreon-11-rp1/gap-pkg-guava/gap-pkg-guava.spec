%global source0_hash f3ecfcd66163f37a850fc71806cb6cefc21b54a050c8a4df2d04c3392c51c348
%global gap_pkgname guava
%global giturl      https://github.com/gap-packages/guava
Name:           gap-pkg-%{gap_pkgname}
Version:        3.21
Release:        1%{?dist}
Summary:        Computing with error-correcting codes
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/guava/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_pkgname}-%{version}.tar.gz
Patch:          %{name}-warning.patch
Patch:          %{name}-popcount.patch
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin lib tbl tst
Requires:       gap-pkg-sonata
%global _docdir_fmt %{name}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-sonata
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  parallel
# /oreon:deps
%description
GUAVA is a package that implements coding theory algorithms in GAP.  Codes can
be created and manipulated and information about codes can be calculated.

GUAVA consists of various files written in the GAP language, and an external
program from J. S. Leon for dealing with automorphism groups of codes and
isomorphism testing functions.  Several algorithms that need the speed are
integrated in the GAP kernel.

The functions within GUAVA can be divided into four categories:
- Construction of codes.  GUAVA can construct non-linear, linear and cyclic
  codes over an arbitrary finite field.  Examples are HadamardCode,
  ReedMullerCode, BestKnownLinearCode, QRCode and GoppaCode.
- Manipulation of codes.  These functions allow the user to transform one code
  into another or to construct a new code from two codes.  Examples are
  PuncturedCode, DualCode, DirectProductCode and UUVCode.
- Computation of information about codes.  This information is stored in the
  code record.  Examples are MinimumDistance, OuterDistribution,
  IsSelfDualCode and AutomorphismGroup.
- Generation of bounds on linear codes.  The table by Brouwer and Verhoeff (as
  it existed in the mid-1990s) is incorporated into GUAVA.  For example,
  BoundsMinimumDistance.

%package doc
License:        GFDL-1.2-no-invariants-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        GUAVA documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{gap_upname}-%{version}

%conf
# Avoid name collisions in the documentation
cp -p src/ctjhai/README README.ctjhai

%build -p

./configure %{gap_archdir}
make CFLAGS='%{build_cflags} -DLONG_EXTERNAL_NAMES'
parallel %{?_smp_mflags} --no-notice gzip --best ::: tbl/*.g
pushd src/leon/doc
pdftex manual.tex
popd
%check

cd tst
gap -l '%{buildroot}%{gap_archdir};' << EOF
LoadPackage("guava");
if Test("bugfix.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("decoding.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("external.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("guava.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("guava01.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("guava02.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("guava08.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("hadamard.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("QCLDPCCodeFromGroup.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("table.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
EOF
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-guava-doc -f %{oreon_filedir}/gap-pkg-guava-doc.list

%changelog

%autochangelog
