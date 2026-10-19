%global source0_hash 02572df81596ff1d06b5d841e3fa7652f7d7976ef021c80728bcf0b08824e30c
%global giturl  https://github.com/algebraic-solving/msolve
Name:           msolve
Version:        0.10.1
Release:        1%{?dist}
Summary:        Polynomial System Solving through Algebraic Methods
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://msolve.lip6.fr/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-avx2.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%global _desc %{expand:msolve is an open source C library implementing computer algebra algorithms
for solving polynomial systems (with rational coefficients or coefficients in
a prime field).
Currently, with msolve, you can basically solve multivariate polynomial
systems.  This encompasses:
- the computation of Groebner bases
- real root isolation of the solutions to polynomial systems
- the computation of the dimension and the degree of the solution set and many
  other things you can do using msolve.}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flint-devel
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
# /oreon:deps
%description
%_desc

This package contains a command line tool to access the msolve
functionality.

%package        libs
Summary:        Library for Polynomial System Solving through Algebraic Methods
%description    libs
%_desc

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
%description    devel
Header files and library links for developing applications that use
msolve.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Fix the pkgconfig file
sed -i 's/ -lflint -lmpfr -lgmp/\nLibs.private:&/' msolve.pc.in

# Generate the configure script
./autogen.sh

%build

%configure --enable-openmp --disable-static
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
%install
%make_install
cd %{buildroot}%{_includedir}/msolve
for h in msolve/*.h; do
  sed -e '/#include/s,"\.\./\(neogb/[[:alnum:]_-]*\.h\)",<msolve/\1>,' \
      -e '/#include/s,"\([[:alnum:]_-]*\.h\)",<msolve/msolve/\1>,' \
      -i.orig $h
  touch -r $h.orig $h
  rm $h.orig
done
for h in neogb/*.h; do
  sed -i.orig '/#include/s,"\([[:alnum:]_-]*\.h\)",<msolve/neogb/\1>,' $h
  touch -r $h.orig $h
  rm $h.orig
done
cd -
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -v %{version} %{buildroot}%{_bindir}/msolve \
  -n 'Polynomial System Solving through Algebraic Methods' \
  > %{buildroot}%{_mandir}/man1/msolve.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n msolve-libs -f %{oreon_filedir}/msolve-libs.list
%files -n msolve-devel -f %{oreon_filedir}/msolve-devel.list

%changelog

%autochangelog
