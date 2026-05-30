%global source0_hash 92e6de1be9ec176428fd2367677e61ceffc2ee1cb119035037a27d346b0403bb

%global develdocdir %{_docdir}/%{name}-devel

Name:           libevent
Version:        2.1.12
Release:        17%{?dist}
Summary:        Abstract asynchronous event notification library

# arc4random.c, which is used in build, is ISC. The rest is BSD-3-Clause.
# evndns.* and include/event2/dns.h has part of LicenseRef-Fedora-Public-Domain
License:        BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
URL:            http://libevent.org/
Source0:        https://github.com/libevent/libevent/releases/download/release-%{version}-stable/libevent-%{version}-stable.tar.gz

BuildRequires: make
BuildRequires:  gcc
# Needed for ./autogen.sh:
BuildRequires:  automake libtool
%if ! 0%{?_module_build}
BuildRequires: doxygen
%endif
BuildRequires: openssl-devel
BuildRequires: python3-devel

# Disable network tests
Patch01: libevent-nonettests.patch
# Upstream patch:
Patch02: 0001-build-do-not-try-install-doxygen-man-pages-if-they-w.patch
# Upstream patch:
Patch03: 0001-build-add-doxygen-to-all.patch
# Temporary downstream change: revert a problematic upstream change
# until Transmission is fixed. Please drop the patch when the Transmission
# issue is fixed.
# https://github.com/transmission/transmission/issues/1437
Patch04: 0001-Revert-Fix-checking-return-value-of-the-evdns_base_r.patch

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.

%package devel
Summary: Development files for %{name}
License: BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and libraries for developing
with %{name}.

%package doc
Summary: Development documentation for %{name}
# The files sample/openssl_hostname_validation.{c,h} and sample/hostcheck.{c,h}
# are MIT, sample/ssl-client-mbedtls.c is Apache-2.0, and the rest is BSD.
License: BSD-3-Clause AND MIT AND Apache-2.0
BuildArch: noarch

%description doc
This package contains the development documentation for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n libevent-%{version}-stable

%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -pn test/check-dumpevents.py \
                               event_rpcgen.py

%build
# We're patching doxygen.am, so regenerate the autotools stuff to be
# safe
./autogen.sh
%configure \
%if ! 0%{?_module_build}
    --enable-doxygen-doc \
%endif
    --disable-dependency-tracking --disable-static
%make_build all

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Maintain the Fedora-specific location of libevent documentation, at
# least for now
mv $RPM_BUILD_ROOT/%{_docdir}/%{name} $RPM_BUILD_ROOT/%{develdocdir}

# Fix multilib install of devel (bug #477685)
mv $RPM_BUILD_ROOT%{_includedir}/event2/event-config.h \
   $RPM_BUILD_ROOT%{_includedir}/event2/event-config-%{__isa_bits}.h
cat > $RPM_BUILD_ROOT%{_includedir}/event2/event-config.h << EOF
#include <bits/wordsize.h>

# if __WORDSIZE == 32
#include <event2/event-config-32.h>
#elif __WORDSIZE == 64
#include <event2/event-config-64.h>
#else
#error "Unknown word size"
# endif
EOF

mkdir -p $RPM_BUILD_ROOT/%{develdocdir}/sample
(cd sample; \
	install -p -m 644 *.c *.am $RPM_BUILD_ROOT/%{develdocdir}/sample)

%check
# Tests fail due to nameserver not running locally
# [msg] Nameserver 127.0.0.1:38762 has failed: request timed out.
# On some architects this error is ignored on others it is not.
#make check

%ldconfig_scriptlets

%files
%license LICENSE
%doc ChangeLog
%{_libdir}/libevent-2.1.so.*
%{_libdir}/libevent_core-2.1.so.*
%{_libdir}/libevent_extra-2.1.so.*
%{_libdir}/libevent_openssl-2.1.so.*
%{_libdir}/libevent_pthreads-2.1.so.*

%files devel
%{_includedir}/event.h
%{_includedir}/evdns.h
%{_includedir}/evhttp.h
%{_includedir}/evrpc.h
%{_includedir}/evutil.h
%dir %{_includedir}/event2
%{_includedir}/event2/*.h
%{_libdir}/libevent.so
%{_libdir}/libevent_core.so
%{_libdir}/libevent_extra.so
%{_libdir}/libevent_openssl.so
%{_libdir}/libevent_pthreads.so
%{_libdir}/pkgconfig/libevent.pc
%{_libdir}/pkgconfig/libevent_core.pc
%{_libdir}/pkgconfig/libevent_extra.pc
%{_libdir}/pkgconfig/libevent_openssl.pc
%{_libdir}/pkgconfig/libevent_pthreads.pc
%{_bindir}/event_rpcgen.*

%files doc
%doc %{develdocdir}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.12-17
- Prepare for Oreon 11 (RP1)
