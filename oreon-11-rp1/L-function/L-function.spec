%global source0_hash 94efc160a2761de75df534707fd2ec53949c5389296d20ddbac1b285fe26d1ad

# FIXME: This package should be renamed to lcalc.

Name:		L-function
Version:	2.0.5
Release:	14%{?dist}
Summary:	C++ L-function class library and command line interface
License:	GPL-2.0-or-later
URL:		https://gitlab.com/sagemath/lcalc
VCS:		git:%{url}.git
Source0:	%{url}/-/archive/%{version}/lcalc-%{version}.tar.bz2
# Fix use of the wrong delete operator
# https://gitlab.com/sagemath/lcalc/-/merge_requests/5
Patch0:		%{name}-mismatched-delete.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:	gcc-c++
BuildRequires:	gengetopt
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	pari-devel

%description
C++ L-function class library and command line interface.

%package	devel
Summary:	Development libraries/headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Headers and libraries for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lcalc-%{version}

autoreconf -fi .

%build
%configure --with-pari

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libLfunction.la

# We select the files we want in doc
rm -fr %{buildroot}%{_docdir}/lcalc

%check
make check

%files
%doc doc/{ChangeLog,CONTRIBUTORS,README.md}
%license doc/COPYING
%{_bindir}/lcalc
%{_libdir}/libLfunction.so.1*
%{_mandir}/man1/lcalc.1*

%files devel
%doc doc/examples
%{_includedir}/lcalc/
%{_libdir}/libLfunction.so
%{_libdir}/pkgconfig/lcalc.pc

%changelog
%autochangelog
