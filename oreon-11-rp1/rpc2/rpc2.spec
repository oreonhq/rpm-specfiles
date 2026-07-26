%global source0_hash e9df7b83bd5d19a2e331a3cfcae7fbea1dae335776eb83ea089bbacfc9e1d3ad

# cleaning up this code for c23 is non-trivial
%global optflags %{optflags} -fPIC -fPIE -std=gnu17

Name:           rpc2
Version:        2.37
Release:        3%{?dist}
Summary:        C library for remote procedure calls over UDP
License:        LGPL-2.0-only
URL:            http://www.coda.cs.cmu.edu/
# This only seems to be maintained inside the coda github
# git clone https://github.com/cmusatyalab/coda.git
# cp -a coda/lib-src/rpc2/ rpc2-2.37
# tar cvfz rpc2-2.37.tar.gz rpc2-2.37
Source0:        %{name}-%{version}.tar.gz
Patch2:         rpc2-2.10-lua-5.4.patch
Patch3:         rpc2-2.37-rp2gen-cflags.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  lwp-devel lua-devel flex bison
BuildRequires:  autoconf, automake, libtool

%description
The RPC2 library, a C library for remote procedure calls over UDP.

%package        devel
Summary:        Development files for %{name}
# headers are LGPLv2, rp2gen is GPLv2
License:        LGPL-2.0-only AND GPL-2.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P2 -p1 -b .lua54
%patch -P3 -p1 -b .cflags

autoreconf -ifv

%build
%configure --disable-static --with-lua
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING NEWS
%{_libdir}/*.so.*
%{_datadir}/%{name}

%files devel
%{_bindir}/rp2gen
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
