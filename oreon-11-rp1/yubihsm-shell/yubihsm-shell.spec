%global source1_hash 659ccc36e90cb7236f94fce3a68f00ead6f3bf0e9531f005e1f447b2f698a22a
%global source0_hash 627a06899096f8bc81a806ef415e00cf7f08a3fc38f4b6b3f39b8129e64dd481
%undefine __cmake_in_source_build
Name:		yubihsm-shell
Version:	2.8.0
Release:        1%{?dist}
Summary:        Tools to interact with YubiHSM 2
License:	Apache-2.0 
URL:		https://github.com/Yubico/%{name}/
Source0:        https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:	gpgkey-9588EA0F.gpg
Patch2:	yubihsm-shell-2.5.0-pcsc-lite.patch
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  cppcheck
BuildRequires:  gcc
BuildRequires:  gengetopt
BuildRequires:  gnupg2
BuildRequires:  help2man
BuildRequires:  libcurl-devel
BuildRequires:  libedit-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  openssl-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
# /oreon:deps
%description
This package contains most of the components used to interact with
the YubiHSM 2 at both a user-facing and programmatic level.

%package devel
Summary: Development tools for interacting with YubiHSM 2
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries for working with yubihsm 2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch 2 -p1

%build

%set_build_flags
%ifarch s390x
export CFLAGS="$CFLAGS -Wno-error=format-overflow"
%endif
export CFLAGS="$CFLAGS -Wno-error=deprecated-declarations"
%cmake -DCMAKE_SKIP_INSTALL_RPATH=ON \
   %if "%{?_lib}" == "lib64"
     %{?_cmake_lib_suffix64}
   %endif
   %{nil}
%cmake_build
%install
%cmake_install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubihsm-shell
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubihsm-wrap
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/pkcs11/yubihsm_pkcs11.so
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n yubihsm-shell-devel -f %{oreon_filedir}/yubihsm-shell-devel.list

%changelog

%autochangelog
