%global source0_hash d9ec76cbe34db98eec3539fe2c899d26b0c837cb3eb466a56b0f109cabf658f7

%if 0%{?fedora} > 40 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global _preprocessor_defines %{?_preprocessor_defines} -DOPENSSL_NO_ENGINE
%endif

Name:		libssh2
Version:	1.11.1
Release:	1%{?dist}
Summary:	A library implementing the SSH2 protocol
License:	BSD-3-Clause
URL:		https://www.libssh2.org/
Source0:	https://libssh2.org/download/libssh2-%{version}.tar.gz
Source1:	https://libssh2.org/download/libssh2-%{version}.tar.gz.asc
Source2:	mykey.asc
Patch0:		libssh2-1.11.1-CVE-2026-7598.patch

BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	gpgverify
BuildRequires:	groff
BuildRequires:	glibc-langpack-en
BuildRequires:	make
BuildRequires:	openssh-server
BuildRequires:	openssl-devel > 1:1.0.2
BuildRequires:	pkgconfig
BuildRequires:	sed
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/man

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package	devel
Summary:	Development files for libssh2
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The libssh2-devel package contains libraries and header files for
developing applications that use libssh2.

%package	docs
Summary:	Documentation for libssh2
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	docs
The libssh2-docs package contains man pages and examples for
developing applications that use libssh2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0
sed -i s/4711/47%{?__isa_bits}/ tests/{openssh_fixture.c,test_ssh{2.c,d.test}}

%build
%configure \
	--disable-rpath \
	--disable-silent-rules \
	--disable-static \
	--enable-shared \
	--disable-docker-tests
%{make_build}

%install
%{make_install} INSTALL="install -p"
find %{buildroot} -name '*.la' -delete
make -C example clean
find example/ -type f \
	'(' -name '*.am' -o -name '*.in' -o -name CMakeLists.txt ')' \
	-print -delete
sed -i	-e 's|-L%{_libdir} ||g' \
	-e 's|-L[$]{libdir} ||g' %{buildroot}%{_libdir}/pkgconfig/libssh2.pc
mv -v example example.%{_arch}

%check
LC_ALL=en_US.UTF-8 make -C tests check

%ldconfig_scriptlets

%files
%license COPYING
%doc docs/AUTHORS README RELEASE-NOTES
%{_libdir}/libssh2.so.1
%{_libdir}/libssh2.so.1.*

%files docs
%doc docs/BINDINGS.md docs/HACKING.md docs/TODO NEWS
%{_mandir}/man3/libssh2_*.3*

%files devel
%doc example.%{_arch}/
%{_includedir}/libssh2.h
%{_includedir}/libssh2_publickey.h
%{_includedir}/libssh2_sftp.h
%{_libdir}/libssh2.so
%{_libdir}/pkgconfig/libssh2.pc

%changelog
%autochangelog
