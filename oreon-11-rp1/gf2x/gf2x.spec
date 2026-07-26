%global source0_hash 741694fac29d56edf58b42dc9827c85303090522ccdd1e89c311c6b22c290efa

Name:           gf2x
Version:        1.3.0
Release:        18%{?dist}
Summary:        Polynomial multiplication over the binary field

# GPL-3.0-or-later: the project as a whole
# LGPL-2.1-or-later: fft/gf2x-cantor-fft.h
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.inria.fr/gf2x/gf2x
VCS:            git:%{url}.git
Source:         %{url}/-/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.bz2
# Fix mismatched declarations and definitions
Patch:          %{name}-mismatched-decls.patch
# Change configure due to the Modern C initiative.  See
# https://fedoraproject.org/wiki/Changes/PortingToModernC
Patch:          %{name}-modern-c.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
Gf2x is a C/C++ software package containing routines for fast arithmetic in
`GF(2)[x]` (multiplication, squaring, GCD) and searching for
irreducible/primitive trinomials.

%package devel
Summary:        Headers and library files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and library files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version} -p1

%conf
# Fix the FSF's address
for badfile in `grep -FRl 'Fifth Floor' .`; do
  sed -e 's/Fifth Floor/Suite 500/' -e 's/02111-1307/02110-1335/' \
      -i.orig $badfile
  touch -r $badfile.orig $badfile
  rm -f $badfile.orig
done

# Generate the configure script
autoreconf -I config -fi .

%build
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Build the SSE2 version for x86, the native version for all other arches.
# Support for pclmul would be nice, but not all x86s support it.
%ifarch %{x86_64}
%configure --disable-static --disable-hardware-specific-code --enable-sse2 \
  --disable-sse3 --disable-ssse3 --disable-sse41 --disable-pclmul \
  --disable-silent-rules --enable-fft-interface hwdir=x86_64
# Workaround broken configure macros
sed -i.orig 's,/\* #undef \(GF2X_HAVE_SSE2_SUPPORT\) \*/,#define \1 1,' \
    gf2x/gf2x-config.h gf2x/gf2x-config-export.h
fixtimestamp gf2x/gf2x-config.h
fixtimestamp gf2x/gf2x-config-export.h
%else
# Workaround broken configure macros
sed -e "s/GF2X_SSE2_AVAILABLE_TRUE=$/&'#'/" \
    -e "/GF2X_SSE2_AVAILABLE_FALSE/s/'#'//" \
    -i configure
%configure --disable-static --disable-hardware-specific-code --disable-sse2 \
  --disable-sse3 --disable-ssse3 --disable-sse41 --disable-pclmul \
  --disable-silent-rules --enable-fft-interface hwdir=generic64
%endif

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build --eval='.SECONDARY:'

%install
%make_install INSTALL="install -p"

%check
LD_LIBRARY_PATH=$PWD/.libs:$PWD/fft/.libs make check

%files
%doc AUTHORS BUGS NEWS README TODO
%license COPYING
%{_libdir}/lib%{name}.so.3{,.*}
%{_libdir}/lib%{name}-fft.so.3{,.*}

%files devel
%doc ChangeLog
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-fft.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
