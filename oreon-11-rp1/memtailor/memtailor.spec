%global source0_hash d16726040d73751d220f2a2d6404a74b2a3f7d2d7a62d11d69f845bafce55136
Name:           memtailor
Version:        1.4
Release:        1%{?dist}
Summary:        C++ library of special-purpose memory allocators
License:        BSD-3-Clause
URL:            https://github.com/Macaulay2/memtailor
VCS:            git:%{url}.git
Source0:        https://github.com/Macaulay2/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtest)
# /oreon:deps
%description
Memtailor is a C++ library of special purpose memory allocators.  It currently
offers an arena allocator and a memory pool.

The main motivation to use a memtailor allocator is better and more
predictable performance than you get with new/delete.  Sometimes a memtailor
allocator can also be more convenient due to the ability to free many
allocations at one time.

The Memtailor memory pool is useful if you need to do many allocations of a
fixed size.  For example a memory pool is well suited to allocate the nodes in
a linked list.

You can think of the Memtailor arena allocator as being similar to stack
allocation.  Both kinds of allocation are very fast and require you to
allocate/deallocate memory in last-in-first-out order.  Arena allocation has
the further benefits that it stays within the C++ standard, it will not cause
a stack overflow, you can have multiple arena allocators at the same time and
allocation is not tied to a function invocation.

%package devel
Summary:        Development files for memtailor
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for developing applications that use memtailor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
# Fix the URL in the pkgconfig file
sed -i 's/broune/Macaulay2/' build/autotools/memtailor.pc.in

# Upstream doesn't generate the configure script
autoreconf -fi

%build

export GTEST_PATH=%{_prefix}
export GTEST_VERSION=$(gtest-config --version)
%configure --disable-static --enable-shared --with-gtest=yes
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=$PWD/.libs make check
%files -f %{oreon_filedir}/main.list
%files -n memtailor-devel -f %{oreon_filedir}/memtailor-devel.list

%changelog

%autochangelog
