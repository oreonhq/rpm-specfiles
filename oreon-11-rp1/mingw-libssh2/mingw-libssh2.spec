%global source0_hash d9ec76cbe34db98eec3539fe2c899d26b0c837cb3eb466a56b0f109cabf658f7

%?mingw_package_header

Name:           mingw-libssh2
Version:        1.11.1
Release:        3%{?dist}
Summary:        MinGW Windows library implementation of the SSH2 protocol

License:        BSD-3-Clause
URL:            https://www.libssh2.org/
Source0:        https://libssh2.org/download/libssh2-%{version}.tar.gz
Source1:        https://libssh2.org/download/libssh2-%{version}.tar.gz.asc
# Daniel Stenberg's GPG keys; linked from https://daniel.haxx.se/address.html
Source2:        https://daniel.haxx.se/mykey.asc

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-zlib

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

# Win32
%package -n mingw32-libssh2
Summary:        MinGW Windows library implementation of the SSH2 protocol
Requires:       pkgconfig

%description -n mingw32-libssh2
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package -n mingw32-libssh2-static
Summary:        Static version of the MinGW Windows SSH2 library
Requires:       mingw32-libssh2 = %{version}-%{release}

%description -n mingw32-libssh2-static
Static version of the MinGW Windows SSH2 library.

# Win64
%package -n mingw64-libssh2
Summary:        MinGW Windows library implementation of the SSH2 protocol
Requires:       pkgconfig

%description -n mingw64-libssh2
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package -n mingw64-libssh2-static
Summary:        Static version of the MinGW Windows SSH2 library
Requires:       mingw64-libssh2 = %{version}-%{release}

%description -n mingw64-libssh2-static
Static version of the MinGW Windows SSH2 library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n libssh2-%{version}

%build
%mingw_configure --disable-silent-rules --enable-static --enable-shared
%mingw_make %{?_smp_mflags}

%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Remove .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Remove man pages which duplicate native Fedora.
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}/man3
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}/man3

# Win32
%files -n mingw32-libssh2
%doc COPYING
%{mingw32_bindir}/libssh2-1.dll
%{mingw32_libdir}/libssh2.dll.a
%{mingw32_libdir}/pkgconfig/libssh2.pc
%{mingw32_includedir}/libssh2.h
%{mingw32_includedir}/libssh2_publickey.h
%{mingw32_includedir}/libssh2_sftp.h

%files -n mingw32-libssh2-static
%{mingw32_libdir}/libssh2.a

# Win64
%files -n mingw64-libssh2
%doc COPYING
%{mingw64_bindir}/libssh2-1.dll
%{mingw64_libdir}/libssh2.dll.a
%{mingw64_libdir}/pkgconfig/libssh2.pc
%{mingw64_includedir}/libssh2.h
%{mingw64_includedir}/libssh2_publickey.h
%{mingw64_includedir}/libssh2_sftp.h

%files -n mingw64-libssh2-static
%{mingw64_libdir}/libssh2.a

%changelog
%autochangelog
