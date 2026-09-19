%global source0_hash 67bc662955c6ca2fa6a0ce372c4794ec3d0cd2c1e50b124e7a75af7e23dd1d0c

Name:		sha2
Version:	1.0.1
Release:	31%{?dist}
Summary:	SHA Implementation Library
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.aarongifford.com/computers/sha.html
Source0:	http://www.aarongifford.com/computers/%{name}-%{version}.tgz
# Makefile to build the binaries. Sent upstream via email
Source1:	%{name}-Makefile
Patch0:		sha2-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-interpreter

%description
The library implements the SHA-256, SHA-384, and SHA-512 hash algorithms. The
interface is similar to the interface to SHA-1 found in the OpenSSL library.

sha2 is a simple program that accepts input from either STDIN or reads one or
more files specified on the command line, and then generates the specified hash
(either SHA-256, SHA-384, SHA-512, or any combination thereof, including all
three at once).

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp -a %{SOURCE1} Makefile

%build
make %{?_smp_mflags} \
	OPTFLAGS="%{optflags}"

%install
make install \
	DESTDIR=%{buildroot} \
	LIBDIR=%{_libdir} \
	INCLUDEDIR=%{_includedir} \
	BINDIR=%{_bindir} \
	OPTFLAGS="%{optflags}"

%check
LD_PRELOAD=./libsha2.so ./sha2test.pl

%ldconfig_scriptlets

%files
%doc README
%{_libdir}/libsha2.so.*
%{_bindir}/sha2*

%files devel
%{_includedir}/sha2.h
%{_libdir}/libsha2.so

%changelog
%autochangelog
