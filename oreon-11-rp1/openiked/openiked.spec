%global source0_hash 19b72b48080240c3eff585f5cbcf6aa7b5734192ad8bc6677ae64a455074358a
Name:           openiked
Version:        7.4
Release:        1%{?dist}
Summary:        A free Internet Key Exchange (IKEv2) implementation
License:        ISC
URL:            https://github.com/openiked/openiked-portable
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenIKED/openiked-%{version}.tar.gz
Source1:        openiked.service
Source2:        sysusers.conf
Source3:        openiked-keygen
Source4:        openiked-keygen.service
Source5:        openiked-keygen.target
# oreon:deps
BuildRequires:  byacc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
OpenIKED is a free, permissively licensed Internet Key Exchange (IKEv2)
implementation, developed as part of the OpenBSD project. It is intended to be
a lean, secure and inter-operable daemon that allows for easy setup and
management of IPsec VPNs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DWITH_SYSTEMD:BOOL=ON
%cmake_build
%install
%cmake_install
install -p -D -m644 %{SOURCE1} %{buildroot}%{_unitdir}/openiked.service
install -p -D -m644 %{SOURCE2} %{buildroot}%{_sysusersdir}/openiked.conf
install -p -D -m755 %{SOURCE3} %{buildroot}%{_libexecdir}/openiked/openiked-keygen
install -p -m644 %{SOURCE4} %{buildroot}%{_unitdir}/openiked-keygen.service
install -p -m644 %{SOURCE5} %{buildroot}%{_unitdir}/openiked-keygen.target
%oreon_autofiles main

%check

%{__cmake_builddir}/regress/dh/dhtest
%{__cmake_builddir}/regress/parser/test_parser
%post

%systemd_post openiked.service
%preun

%systemd_preun openiked.service
%postun

%systemd_postun_with_restart openiked.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
