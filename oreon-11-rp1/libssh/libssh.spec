%global source2_hash 7c59d0fdea72cdfbaca82f77eb6e6e416fd4c5aacf1c853bc7f911ce4e4dc051
%global source1_hash f9f3708372d86771bd0b1db96d0e3adfb2b51075cd14b849e3747f3ac406c713
%global source0_hash 49560f677d96e3706a904ac2de1116e25f3680937d51e5c92198fcba4a1c1e9f
%global source2_key_fpr 88A228D89B07C2C77D0C780903D5DF8CFDD3E8E7
Name:           libssh
Version:        0.12.2
Release:        1%{?dist}
Summary:        A library implementing the SSH protocol
License:        LGPL-2.1-or-later
%bcond_without check
URL:            http://www.libssh.org
Source0:        https://www.libssh.org/files/0.12/%{name}-%{version}.tar.xz
Source1:        https://www.libssh.org/files/0.12/%{name}-%{version}.tar.xz.asc
Source2:        https://www.libssh.org/files/0x03D5DF8CFDD3E8E7_libssh_libssh_org_gpgkey.asc#/%{name}.keyring
Source3:        libssh_client.config
Source4:        libssh_server.config
Requires:       %{name}-config = %{version}-%{release}
Recommends:     crypto-policies
%ifarch aarch64 ppc64 ppc64le s390x x86_64 riscv64
Provides: libssh_threads.so.4()(64bit)
%else
Provides: libssh_threads.so.4
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  gnutls-utils
BuildRequires:  hostname
BuildRequires:  krb5-devel
BuildRequires:  krb5-server
BuildRequires:  krb5-workstation
BuildRequires:  libcmocka-devel
BuildRequires:  libfido2-devel
BuildRequires:  nmap-ncat
BuildRequires:  nss_wrapper
BuildRequires:  opensc
BuildRequires:  openssh-clients
BuildRequires:  openssh-server
BuildRequires:  openssh-sk-dummy
BuildRequires:  openssl-devel
BuildRequires:  p11-kit-devel
BuildRequires:  pam_wrapper
BuildRequires:  pkcs11-provider
BuildRequires:  pkgconfig
BuildRequires:  priv_wrapper
BuildRequires:  socket_wrapper
BuildRequires:  softhsm
BuildRequires:  uid_wrapper
BuildRequires:  zlib-devel
# /oreon:deps
%description
The ssh library was designed to be used by programmers needing a working SSH
implementation by the mean of a library. The complete control of the client is
made by the programmer. With libssh, you can remotely execute programs, transfer
files, use a secure and transparent tunnel for your remote programs. With its
Secure FTP implementation, you can play with remote files easily, without
third-party programs others than libcrypto (from openssl).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package config
Summary:        Configuration files for %{name}
BuildArch:      noarch
Obsoletes:      %{name} < 0.9.0-3
%description config
The %{name}-config package provides the default configuration files for %{name}.

%prep

test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DUNIT_TESTING=ON \
    -DCLIENT_TESTING=ON \
    -DSERVER_TESTING=ON \
    -DGSSAPI_TESTING=ON \
    -DWITH_PKCS11_URI=ON \
    -DWITH_PKCS11_PROVIDER=ON \
    -DWITH_FIDO2=ON \
    -DGLOBAL_CLIENT_CONFIG="%{_sysconfdir}/libssh/libssh_client.config" \
    -DGLOBAL_BIND_CONFIG="%{_sysconfdir}/libssh/libssh_server.config"
%cmake_build
%install
%cmake_install
install -d -m755 %{buildroot}%{_sysconfdir}/libssh
install -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/libssh/libssh_client.config
install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/libssh/libssh_server.config
pushd %{buildroot}%{_libdir}
for i in libssh.so*;
do
    _target="${i}"
    _link_name="${i%libssh*}libssh_threads${i##*libssh}"
    if [ -L "${i}" ]; then
        _target="$(readlink ${i})"
    fi
    ln -s "${_target}" "${_link_name}"
done;
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%if %{with check}
%global _smp_build_ncpus 1
%ifarch aarch64
%ctest -E 'torture_server_direct_tcpip|torture_forwarded_tcpip_callback|torture_request_pty_modes'
%else
%ctest -E 'torture_server_direct_tcpip'
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n libssh-devel -f %{oreon_filedir}/libssh-devel.list
%files -n libssh-config -f %{oreon_filedir}/libssh-config.list

%changelog

* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.0-2
- Run %%check (ctest) by default

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.0-1
- Prepare for Oreon 11 (RP1)
