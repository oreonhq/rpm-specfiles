%global source0_hash 7bf0ccd560313a07861caf7a1e20e2a45f0fa5544acc3ffb9f61efd5f227f59d
Name:           frobby
Summary:        Computations with monomial ideals
Version:        0.9.9
Release:        1%{?dist}
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN
URL:            https://github.com/Macaulay2/frobby
VCS:            git:%{url}.git
Source0:        https://github.com/Macaulay2/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-sharedlib.patch
ExcludeArch:    %{ix86}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gmp)
# /oreon:deps
%description
Frobby is a software system and project for computations with monomial ideals.
Frobby is free software and it is intended as a vehicle for research on
monomial ideals, as well as a useful practical tool for investigating monomial
ideals.

The current functionality includes Hilbert series, maximal standard monomials,
combinatorial optimization on monomial ideals, primary decomposition,
irreducible decomposition, Alexander dual, associated primes, minimization and
intersection of monomial ideals as well as the computation of Frobenius
problems (using 4ti2) with very large numbers.  Frobby is also able to
translate between formats that can be used with several different computer
systems, such as Macaulay 2, Monos, 4ti2, CoCoA4 and Singular.  Thus Frobby
can be used with any of those systems.

%package -n libfrobby
License:        GPL-2.0-or-later
Summary:        Frobby internals as a library
%description -n libfrobby
This package contains the frobby internals as a library, often called
libfrobby.

%package -n libfrobby-devel
License:        GPL-2.0-or-later
Summary:        Developer files for libfrobby
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description -n libfrobby-devel
Header files and library links to develop applications that use the
Frobby internals as a library (libfrobby).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%cmake -DBUILD_TESTING:BOOL=ON

%build

export STRIP=true
%cmake_build
cd doc
pdflatex manual.tex
pdflatex manual.tex
cd -
%install
%cmake_install
rm -fr %{buildroot}%{_prefix}/licenses %{buildroot}%{_defaultlicensedir}
%oreon_autofiles libfrobby usr/*/lib*.so.*
%oreon_autofiles libfrobby-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir bin
ln -s ../%{_vpath_builddir}/frobby-tests bin/frobby
test/runTests
%files -f %{oreon_filedir}/main.list
%files -n libfrobby -f %{oreon_filedir}/libfrobby.list
%files -n libfrobby-devel -f %{oreon_filedir}/libfrobby-devel.list

%changelog

%autochangelog
