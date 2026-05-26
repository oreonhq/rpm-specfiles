# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 ad1e2dd9b500c58ee462acd839d0a0ea9a2b9248a1287840bc601e774fb6b28f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary:        C library for portable packet creation and injection
Name:           libnet
Version:        1.3
Release:        7%{?dist}
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/libnet/libnet
Source0:        https://github.com/libnet/libnet/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         libnet-config.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{_bindir}/pod2man

%description
Libnet is an API to help with the construction and handling of network
packets. It provides a portable framework for low-level network packet
writing and handling (use libnet in conjunction with libpcap and you can
write some really cool stuff). Libnet includes packet creation at the IP
layer and at the link layer as well as a host of supplementary and
complementary functionality.

%package devel
Summary:        Development files for the libnet library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
The libnet-devel package includes header files and libraries necessary
for developing programs which use the libnet library. Libnet is very
handy with which to write network tools and network test code. See the
man page and sample test code for more detailed information.

%if 0%{!?_without_doc:1}
%package doc
Summary:        Documentation files for the libnet library
BuildArch:      noarch
BuildRequires:  doxygen
BuildRequires:  graphviz

%description doc
Libnet is an API to help with the construction and handling of network
packets. It provides a portable framework for low-level network packet
writing and handling. This package contains the API documentation for
developing applications that use libnet.
%endif

%prep
%oreon_verify_sources
%setup -q
%patch -P 0 -p1
# Avoid library soname bump (https://github.com/libnet/libnet/issues/115)
sed -e 's/-version-info 9:0:0/-version-info 9:0:8/' -i src/Makefile.{am,in}

%build
%configure
%make_build

%install
%make_install INSTALL='install -p'

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.{a,la}

# Clean up for later usage in documentation
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

# Prepare samples for usage in documentation
rm -rf sample/{Makefile*,win32}
for file in sample/*.[hc]; do
  sed \
    -e 's@#include "../include/libnet.h"@#include <libnet.h>@' \
    -e 's@#include "../include/config.h"@#include <config.h>@' \
    $file > $file.new
    touch -c -r $file{,.new}
    mv -f $file{.new,}
done

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md ChangeLog.md
%{_libdir}/%{name}.so.*

%files devel
%doc doc/MIGRATION.md doc/RAWSOCKET.md sample/
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man3/%{name}*.3*

%if 0%{!?_without_doc:1}
%files doc
%doc doc/html/
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-7
- Import
