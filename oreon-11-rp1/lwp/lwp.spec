%global source0_hash 36daaf072d3ac019d223198ed8b6657f4519d8e12e2c238ea8f8050194a81e59

Name:           lwp
Version:        2.17
Release:        3%{?dist}
Summary:        C library for user-mode threading
License:        LGPL-2.0-only
URL:            http://www.coda.cs.cmu.edu/
# This only seems to be maintained inside the coda github
# git clone https://github.com/cmusatyalab/coda.git
# cp -a coda/lib-src/lwp/ lwp-2.17
# tar cvfz lwp-2.17.tar.gz lwp-2.17
Source0:        %{name}-%{version}.tar.gz
Patch0:         lwp-2.17-no-longjmp_chk.patch
Patch1:         lwp-2.17-system-valgrind.patch
Patch2:         lwp-2.17-c23.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  valgrind-devel
BuildRequires:  autoconf, automake, libtool

%description
The LWP user-space threads library. The LWP threads library is used by the Coda
distributed file-system, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .nolongjmpchk
%patch -P1 -p1 -b .system-valgrind
%patch -P2 -p1 -b .c23

# using system header
rm -rf src/valgrind.h

autoreconf -ifv

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
./src/testlwp 2

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
