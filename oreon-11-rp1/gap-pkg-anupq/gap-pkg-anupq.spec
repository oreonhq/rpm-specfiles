%global source0_hash 3806108f248d9592e98ecd33acda0f6d58a7b6703578e711f638524122c5dda2
%global gap_pkgname anupq
%global giturl      https://github.com/gap-packages/anupq
%global _fortify_level 2
Name:           gap-pkg-%{gap_pkgname}
Version:        3.3.3
Release:        1%{?dist}
Summary:        ANU p-Quotient for GAP
License:        Artistic-2.0
URL:            https://gap-packages.github.io/anupq/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.bz%{_fortify_level}
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): bin examples lib standalone testPq tst
BuildOption(check): tst/testinstall.g
Requires:       gap-core%{?_isa}
Requires:       gap-pkg-autpgrp
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-autpgrp-doc
BuildRequires:  gcc
# /oreon:deps
%description
This package gives access to the following algorithms from inside GAP:
1. A p-quotient algorithm to compute a power-commutator presentation for a
   group of prime power order.
2. A p-group generation algorithm to generate descriptions of groups of prime
   power order.
3. A standard presentation algorithm used to compute a canonical
   power-commutator presentation of a p-group.
4. An algorithm which can be used to compute the automorphism group of a
   p-group.

%package doc
License:        Artistic-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        ANUPQ documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-autpgrp-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
cp -p standalone-doc/README README.standalone

%build -p

%configure --with-gaproot=%{gap_archdir} --disable-silent-rules
%make_build
ln -s %{gap_libdir}/doc ../../doc
%build -a

rm -fr ../../doc
cd standalone-doc
pdflatex guide
pdflatex guide
pdflatex guide
cd -
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-anupq-doc -f %{oreon_filedir}/gap-pkg-anupq-doc.list

%changelog

%autochangelog
