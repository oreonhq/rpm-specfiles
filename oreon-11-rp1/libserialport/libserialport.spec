%global source0_hash 5deb92b5ca72c0347b07b786848350deca2dcfd975ce613b8e0e1d947a4b4ca9

Name:           libserialport
Version:        0.1.2
Release:        2%{?dist}
Summary:        Library for accessing serial ports
# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later
URL:            http://sigrok.org/wiki/%{name}
Source0:        http://sigrok.org/download/source/%{name}/%{name}-%{version}.tar.gz
# https://github.com/sigrokproject/libserialport/pull/25
Patch0:         libserialport-0.1.2-version.patch
# https://github.com/sigrokproject/libserialport/pull/24
Patch1:         libserialport-0.1.2-glibc-2.42.patch
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf automake libtool

%description
libserialport is a minimal library written in C that is intended to take care
of the OS-specific details when writing software that uses serial ports.

By writing your serial code to use libserialport, you enable it to work
transparently on any platform supported by the library.

The operations that are supported are:

- Port enumeration (obtaining a list of serial ports on the system).
- Opening and closing ports.
- Setting port parameters (baud rate, parity, etc).
- Reading, writing and flushing data.
- Obtaining error information.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       bundled(jquery)

%description    doc
The %{name}-doc package contains documentation for developing software
with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

autoreconf -vif

%build
%configure --disable-static
%make_build

# This builds documentation for the -doc package
make %{?_smp_mflags} doc

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING README
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files doc
%doc doxy/html-api/

%changelog
%autochangelog
