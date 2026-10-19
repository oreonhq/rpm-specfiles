%global source0_hash 4f277f89735c8b0b8a6bbd043b3efb3fa1cc68a9a5da6a076507d067fc3b3bf8
Name:           nacl
URL:            http://nacl.cace-project.eu/
Version:        20110221
Release:        1%{?dist}
License:        LicenseRef-Fedora-Public-Domain
Summary:        Networking and Cryptography library
Source0:        http://hyperelliptic.org/nacl/nacl-%{version}.tar.bz2
Source1:        curvecpclient.1
Source2:        curvecpserver.1
Source3:        curvecpmakekey.1
Source4:        curvecpmessage.1
Source5:        curvecpprintkey.1
Source6:        nacl-sha256.1
Source7:        nacl-sha512.1
Patch0:         nacl-20110221-dist-flags.patch
Patch1:         nacl-20110221-build-dir.patch
Patch2:         nacl-20110221-noexec-stack.patch
Patch3:         nacl-20110221-cpufreq-fallback.patch
Patch4:         nacl-20110221-abi-len-limit.patch
# oreon:deps
BuildRequires:  e2fsprogs
BuildRequires:  gcc
# /oreon:deps
%description
NaCl (pronounced "salt") is a new easy-to-use high-speed software library for
network communication, encryption, decryption, signatures, etc. NaCl's goal
is to provide all of the core operations needed to build higher-level
cryptographic tools.

%package devel
Summary:        Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Include files and devel library.

%package static
Summary:        Static version of the NaCl library
Provides:       nacl-static%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Statically linkable version of the NaCl library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .dist-flags
%patch -P1 -p1 -b .build-dir
%patch -P2 -p1 -b .noexec-stack
%patch -P3 -p1 -b .cpufreq-fallback
%patch -P4 -p1 -b .abi-len-limit

# It's necessary to build in C89 mode because of implicit function
# declarations and implicit int.
%global build_type_safety_c 0
sed -i 's|\${CFLAGS}|%{optflags} -fPIC|g' okcompilers/c okcompilers/cpp

%build

./do
gcc -shared -fPIC -Wl,-soname,libnacl.so.0 -o libnacl.so.0.0.0 \
  -Wl,-whole-archive build/fedora/lib/*/libnacl.a -Wl,-no-whole-archive \
  build/fedora/lib/*/cpucycles.o build/fedora/lib/*/randombytes.o
%install
mkdir -p %{buildroot}%{_includedir}/%{name}
install -m 0644 -t %{buildroot}%{_includedir}/%{name} build/fedora/include/*/*.h
mkdir -p %{buildroot}%{_libdir}/
install -m 0644 -t %{buildroot}%{_libdir} build/fedora/lib/*/*.a
install -m 0644 -t %{buildroot}%{_libdir} build/fedora/lib/*/cpucycles.o build/fedora/lib/*/randombytes.o
install -m 0755 -t %{buildroot}%{_libdir} libnacl.so.*
pushd %{buildroot}%{_libdir}
ln -s libnacl.so.0.0.0 libnacl.so.0
ln -s libnacl.so.0 libnacl.so
popd
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 -t %{buildroot}%{_mandir}/man1 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}
mkdir -p %{buildroot}%{_bindir}
rm -f build/fedora/bin/ok*
install -m 0755 -t %{buildroot}%{_bindir} build/fedora/bin/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n nacl-devel -f %{oreon_filedir}/nacl-devel.list
%files -n nacl-static -f %{oreon_filedir}/nacl-static.list

%changelog

%autochangelog
