%global source0_hash 6898ba9dd836d618b71dc7a4bb786a502c173cef5cafbf20fe5e0567ba4ea30c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libssh
Version: 0.11.5
Release: 1%{?dist}
Summary: C library implementing the SSH protocol
License: LGPL-2.1-or-later
URL: https://www.libssh.org/
Source0: https://www.libssh.org/files/0.11/libssh-%{version}.tar.xz
Source1: libssh-%{version}.tar.xz.asc
Source2: libssh-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: krb5-devel
%endif

%description
libssh is a multiplatform C library implementing the SSHv2 protocol on
client and server side.

%package devel
Summary: Development files for libssh
Requires: libssh%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libssh)

%description devel
Headers and libraries for developing against libssh.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n libssh-%{version} -p1

%build
%oreon_cmake -DUNIT_TESTING=OFF -DCLIENT_TESTING=OFF -DSERVER_TESTING=OFF -DWITH_EXAMPLES=OFF -DWITH_GSSAPI=ON -DWITH_ZLIB=ON -DGLOBAL_CLIENT_CONFIG=%{_sysconfdir}/libssh/libssh_client.config -DGLOBAL_BIND_CONFIG=%{_sysconfdir}/libssh/libssh_server.config
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
