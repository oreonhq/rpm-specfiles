%global source0_hash d0a61a5c52d99fa7ce7d00ed0a07e341dbda67101dbed1ab0cdae3f37db4eb0b

%define plugindir %{_libdir}/esmtp-plugins

Summary:        SMTP client library
Name:           libesmtp
Version:        1.0.6
Release:        35%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Source:         http://www.stafford.uklinux.net/libesmtp/%{name}-%{version}.tar.bz2
URL:            http://www.stafford.uklinux.net/libesmtp/
BuildRequires:  gcc
BuildRequires:  openssl-devel pkgconfig autoconf automake libtool
BuildRequires: make
Patch0: libesmtp-1.0.6-openssl-1.1.patch
Patch1: libesmtp-configure-c99.patch

%description
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim. It may be used as part of a Mail User Agent (MUA) or another
program that must be able to post electronic mail but where mail
functionality is not the program's primary purpose.

%package devel
Summary: Headers and development libraries for libESMTP
# example file is under the GPLv2+
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
Requires: %{name} = %{version}-%{release}, openssl-devel

%description devel
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim.

The libesmtp-devel package contains headers and development libraries
necessary for building programs against libesmtp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .openssl-1.1
%patch -P1 -p1

autoreconf -fi

# Keep rpmlint happy about libesmtp-debuginfo...
chmod a-x htable.c

%build

if pkg-config openssl ; then
  export CFLAGS="$CFLAGS $RPM_OPT_FLAGS `pkg-config --cflags openssl`"
  export LDFLAGS="$LDFLAGS `pkg-config --libs-only-L openssl`"
fi
%configure --with-auth-plugin-dir=%{plugindir} --enable-pthreads \
  --enable-require-all-recipients --enable-debug \
  --enable-etrn --disable-isoc --disable-more-warnings --disable-static
make %{?_smp_mflags}
cat << "EOF" > libesmtp.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libESMTP
Version: %{version}
Description: SMTP client library.
Requires: openssl
Libs: -pthread -L${libdir} -lesmtp
Cflags:
EOF

cat << "EOF" > libesmtp-config
#! /bin/sh
exec pkg-config "$@" libesmtp
EOF

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install INSTALL='install -p'
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
rm $RPM_BUILD_ROOT/%{_libdir}/esmtp-plugins/*.la
install -p -m644 -D libesmtp.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libesmtp.pc

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING.LIB NEWS Notes README
%{_libdir}/libesmtp.so.*
%{plugindir}

%files devel
%doc examples COPYING
%{_bindir}/libesmtp-config
%{_prefix}/include/*
%{_libdir}/libesmtp.so
%{_libdir}/pkgconfig/libesmtp.pc

%changelog
%autochangelog
