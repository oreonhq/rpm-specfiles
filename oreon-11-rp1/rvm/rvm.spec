%global source0_hash 76475b364b449ffb4f47b3094c48e38560ba25da84fd14d0b8ba66a3373454ae

# ugly academic code. :(
%global optflags %{optflags} -std=gnu17

Name:           rvm
Version:        1.28
Release:        3%{?dist}
Summary:        C library for unstructured recoverable virtual memory
License:        LGPL-2.0-only
URL:            http://www.coda.cs.cmu.edu/
# This only seems to be maintained inside the coda github
# git clone https://github.com/cmusatyalab/coda.git
# cp -a coda/lib-src/rvm/ rvm-1.28
# tar cvfz rvm-1.28.tar.gz rvm-1.28
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  lwp-devel
BuildRequires:  autoconf, automake, libtool

%description
The RVM persistent recoverable memory library. The RVM library is used by
the Coda distributed file-system.

%package tools
Summary:        Tools for %{name}
# Automatically converted from old format: GPLv2 - review is highly recommended.
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
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# work around linking failures because of the disabling of rpath above
export LD_LIBRARY_PATH=`pwd`/rvm/.libs:`pwd`/seg/.libs
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING NEWS
%{_libdir}/*.so.*

%files tools
%{_sbindir}/rvmutl
%{_sbindir}/rdsinit
%{_mandir}/man1/*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}lwp.pc

%changelog
%autochangelog
