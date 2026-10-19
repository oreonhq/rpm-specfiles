%global source0_hash e9df7b83bd5d19a2e331a3cfcae7fbea1dae335776eb83ea089bbacfc9e1d3ad
%global optflags %{optflags} -fPIC -fPIE -std=gnu17
Name:           rpc2
Version:        2.37
Release:        1%{?dist}
Summary:        C library for remote procedure calls over UDP
License:        LGPL-2.0-only
URL:            http://www.coda.cs.cmu.edu/
Source0:        %{name}-%{version}.tar.gz
Patch2:         rpc2-2.10-lua-5.4.patch
Patch3:         rpc2-2.37-rp2gen-cflags.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  lwp-devel
BuildRequires:  make
# /oreon:deps
%description
The RPC2 library, a C library for remote procedure calls over UDP.

%package        devel
Summary:        Development files for %{name}
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
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} CFLAGS="%{optflags}"
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rpc2-devel -f %{oreon_filedir}/rpc2-devel.list

%changelog

%autochangelog
