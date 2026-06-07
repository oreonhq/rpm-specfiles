%global source0_hash 8b0f4d6c2ae7f5f0f475f03fad5496cadb8cb57914a811616599092cd830b56e

%global source2_key_fpr 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D

Name:           socket_wrapper
Version:        1.5.2
Release:        %autorelease

License:        BSD-3-Clause
Summary:        A library passing all socket communications through Unix sockets
Url:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        socket_wrapper.keyring

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel >= 1.1.0

Recommends:     cmake
Recommends:     pkgconfig

%description
socket_wrapper aims to help client/server software development teams willing to
gain full functional test coverage. It makes it possible to run several
instances of the full software stack on the same machine and perform locally
functional testing of complex network configurations.

To use it set the following environment variables:

LD_PRELOAD=libsocket_wrapper.so
SOCKET_WRAPPER_DIR=/path/to/swrap_dir

This package doesn't have a devel package because this project is for
development/testing.

%package -n libsocket_wrapper_noop
Summary:        A library providing dummies for socket_wrapper

%description -n libsocket_wrapper_noop
Applications with the need to call socket_wrapper_enabled() should link against
-lsocket_wrapper_noop in order to resolve the symbol at link time.

%package -n libsocket_wrapper_noop-devel
Summary:        Development headers for libsocket_wrapper_noop
Requires:       libsocket_wrapper_noop = %{version}-%{release}

%description -n libsocket_wrapper_noop-devel
Development headers for applications with the need to call
socket_wrapper_enabled().

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DUNIT_TESTING=ON

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%ldconfig_scriptlets -n libsocket_wrapper_noop

%check
%ctest

ls -l %{__cmake_builddir}/src/libsocket_wrapper.so
LD_PRELOAD=%{__cmake_builddir}/src/libsocket_wrapper.so bash -c '>/dev/null'

%files
%doc AUTHORS README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libsocket_wrapper.so*
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config-version.cmake
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config.cmake
%{_libdir}/pkgconfig/socket_wrapper.pc
%{_mandir}/man1/socket_wrapper.1*

%files -n libsocket_wrapper_noop
%{_libdir}/libsocket_wrapper_noop.so.*

%files -n libsocket_wrapper_noop-devel
%{_includedir}/socket_wrapper.h
%{_libdir}/libsocket_wrapper_noop.so
%{_libdir}/cmake/socket_wrapper/socket_wrapper_noop-config*.cmake
%{_libdir}/pkgconfig/socket_wrapper_noop.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-1
- Prepare for Oreon 11 (RP1)
