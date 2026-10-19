%global source0_hash 1971d86c7dc0f3e6b906890297635d6a3a84e5e7ad64d36521b74da202fda62f
Name: fluent-bit
Version: 5.1.2
Release:        1%{?dist}
Summary:        Fluent Bit is a super fast, lightweight, and highly scalable logging and metrics processor and forwarder.
License: Apache-2.0
URL: https://github.com/fluent/fluent-bit
Source0:        https://github.com/fluent/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%{?systemd_requires}
ExclusiveArch: x86_64 aarch64
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  graphviz
BuildRequires:  libpq-devel
BuildRequires:  libyaml-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Fluent Bit is a high performance and multi-platform log forwarder.

%prep
%oreon_prep
%build

%cmake\
    -DCMAKE_BUILD_TYPE=RelWithDebInfo\
    -DCMAKE_C_STANDARD=17\
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}\
    -DFLB_DEBUG=Off\
    -DFLB_EXAMPLES=Off\
    -DFLB_HTTP_SERVER=On\
    -DFLB_IN_PODMAN_METRICS=On\
    -DFLB_IN_SYSTEMD=On\
    -DFLB_OUT_ES=On\
    -DFLB_OUT_SLACK=Off\
    -DFLB_OUT_TD=Off\
    -DFLB_PREFER_SYSTEM_LIB_ZSTD=On\
    -DFLB_RELEASE=On\
    -DFLB_SHARED_LIB=Off\
    -DFLB_TESTS_INTERNAL=Off\
    -DFLB_TESTS_RUNTIME=Off\
    -DFLB_TLS=On\
    -DSYSTEMD_UNITDIR=%{_unitdir}\
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
rm -rvf %{buildroot}%{_includedir}
%oreon_autofiles main

%check

%ctest
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
