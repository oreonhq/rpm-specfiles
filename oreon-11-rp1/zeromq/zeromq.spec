%global source0_hash 6c972d1e6a91a0ecd79c3236f04cf0126f2f4dfbbad407d72b4606a7ba93f9c6
%bcond_with pgm
%bcond_without unwind
Name:           zeromq
Version:        4.3.5
Release:        1%{?dist}
Summary:        Software library for fast, message-based applications
License:        MPL-2.0 AND BSD-3-Clause AND MIT
URL:            https://zeromq.org
Source0:        https://github.com/%{name}/libzmq/archive/v%{version}/%{name}-%{version}.tar.gz#/zeromq-4.3.5.tar.gz
Patch1:         zeromq-configure-c99.patch
%if %{with unwind}
%endif
%if %{with pgm}
%endif
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  libunwind-devel
BuildRequires:  make
BuildRequires:  xmlto
# /oreon:deps
%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ZeroMQ shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libzmq-%{version}

# Remove bundled code.
rm -rf external/wepoll

# Fix permissions.
chmod -x src/xsub.hpp

%build

autoreconf -fi
%configure \
%if %{with pgm}
            --with-pgm \
            --with-libgssapi_krb5 \
%endif
            --with-libsodium \
            --enable-drafts \
%if %{with unwind}
            --enable-libunwind \
%endif
            --disable-Werror \
            --disable-static
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/libzmq.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch s390x
make check V=1 XFAIL_TESTS=tests/test_radio_dish || ( cat test-suite.log && exit 1 )
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n zeromq-devel -f %{oreon_filedir}/zeromq-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3.5-1
- Import
