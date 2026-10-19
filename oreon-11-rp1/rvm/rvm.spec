%global source0_hash 76475b364b449ffb4f47b3094c48e38560ba25da84fd14d0b8ba66a3373454ae
%global optflags %{optflags} -std=gnu17
Name:           rvm
Version:        1.28
Release:        1%{?dist}
Summary:        C library for unstructured recoverable virtual memory
License:        LGPL-2.0-only
URL:            http://www.coda.cs.cmu.edu/
Source0:        %{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  lwp-devel
BuildRequires:  make
# /oreon:deps
%description
The RVM persistent recoverable memory library. The RVM library is used by
the Coda distributed file-system.

%package tools
Summary:        Tools for %{name}
License:        GPL-2.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
User-space tools to initialize and manipulate RVM log and data segments.
The RVM library is used by the Coda distributed file-system.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-2.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}, lwp-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
autoreconf -ifv

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH=`pwd`/rvm/.libs:`pwd`/seg/.libs
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rvm-tools -f %{oreon_filedir}/rvm-tools.list
%files -n rvm-devel -f %{oreon_filedir}/rvm-devel.list

%changelog

%autochangelog
