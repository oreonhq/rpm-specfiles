%global source0_hash cf4e87714ef774d5d760ef252f81bcfe6d0b3bb726ae263c602c68cd5d3a495b

%global gap_pkgname float
%global giturl      https://github.com/gap-packages/float

Name:           gap-pkg-%{gap_pkgname}
Version:        1.0.9
Release:        %autorelease
Summary:        GAP access to mpfr, mpfi, mpc, fplll and cxsc

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/float/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Remove atexit hack, not needed for non-coverage builds
Patch:          %{name}-atexit.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): lib tst
BuildOption(check): tst/testall.g

BuildRequires:  cxsc-devel
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gcc-c++
BuildRequires:  libmpc-devel
BuildRequires:  make
BuildRequires:  mpfi-devel
BuildRequires:  pkgconfig(fplll)
BuildRequires:  pkgconfig(mpfr)

Requires:       gap-core%{?_isa}

%description
This package implements floating-point numbers within GAP, with arbitrary
precision, based on the C libraries FPLLL, MPFR, MPFI, MPC and CXSC.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        FLOAT documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p0

%conf
# Do not override Fedora build flags
sed -i 's/-O3 -fomit-frame-pointer//;s/-O3/-O2/' configure

%build -p
export CPPFLAGS='-I %{_includedir}/cxsc'
%configure --with-gaproot=%{gap_archdir}
%make_build

%install -p
%make_install

%files
%doc README.md THANKS
%license COPYING
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/lib/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
