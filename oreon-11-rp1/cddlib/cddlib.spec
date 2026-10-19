%global source0_hash b87ee07ba2c1d0ab92a3e4eccacdf568f981a095a392e3b9efd7e7e4a9e125b1
%global giturl  https://github.com/cddlib/cddlib
Name:           cddlib
Epoch:          1
Version:        0.94n
Release:        1%{?dist}
Summary:        A library for generating all vertices in convex polyhedrons
License:        GPL-2.0-or-later
URL:            https://people.inf.ethz.ch/fukudak/cdd_home/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(latex)
# /oreon:deps
%description
The C-library cddlib is a C implementation of the Double Description Method of
Motzkin et al. for generating all vertices (i.e. extreme points) and extreme
rays of a general convex polyhedron in R^d given by a system of linear
inequalities:
```
   P = { x=(x1, ..., xd)^T :  b - A∙x ≥ 0 }
```
where `A` is a given `m×d` real matrix, `b` is a given `m`-vector and `0` is
the `m`-vector of all zeros.

The program can be used for the reverse operation (i.e. convex hull
computation). This means that one can move back and forth between an
inequality representation and a generator (i.e. vertex and ray) representation
of a polyhedron with cdd.  Also, cdd can solve a linear programming problem,
i.e. a problem of maximizing and minimizing a linear function over `P`.

%package devel
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN
Summary:        Headers for cddlib
Requires:       gmp-devel%{?_isa}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
%description devel
Include files for cddlib.

%package static
Summary:        Static libraries for cddlib
%description static
Static libraries for cddlib.

%package tools
Summary:        Sample binaries that use cddlib
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
%description tools
Sample binaries that use cddlib.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Fix the FSF's address
for f in $(find . -type f -exec grep -Fl '675 Mass' {} +); do
  sed -i.orig \
    's/675 Mass Ave, Cambridge, MA 02139/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    $f
  touch -r $f.orig $f
  rm -f $f.orig
done

# Force rebuilding of the documentation
rm -f doc/cddlibman.pdf

%build

%configure
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
pushd doc
pdflatex cddlibman
popd
%install
%make_install
rm -fr %{buildroot}%{_pkgdocdir}
%oreon_autofiles cddlib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cddlib-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cddlib-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cddlib-devel -f %{oreon_filedir}/cddlib-devel.list
%files -n cddlib-static -f %{oreon_filedir}/cddlib-static.list
%files -n cddlib-tools -f %{oreon_filedir}/cddlib-tools.list

%changelog

%autochangelog
