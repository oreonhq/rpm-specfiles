%global source0_hash d62b89a82520a553edf63fd3ae11275be6f16ec86ed90d8ef7b113d06b239fa2
%global krun_opts %{nil}
%global wasmedge_opts %{nil}
%global yajl_opts %{nil}
%if %{defined copr_username}
%define copr_build 1
%endif
%ifarch aarch64 || x86_64
%endif
%global yajl_opts --enable-embedded-yajl
Summary:        OCI runtime written in C
Name: crun
%if %{defined copr_build}
Epoch: 102
%endif
Version: 1.30.1
Release:        1%{?dist}
URL: https://github.com/containers/%{name}
Source0:        https://github.com/containers/crun/releases/download/%{version}/crun-%{version}.tar.zst
License: GPL-2.0-only
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le riscv64 s390x x86_64
%endif
%if %{defined krun_support}
%endif
%if %{defined system_yajl}
%endif
Recommends: criu >= 3.17.1
Recommends: criu-libs
%if %{defined wasmedge_support}
%endif
Provides: oci-runtime
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  criu-devel
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glibc-static
BuildRequires:  gperf
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libtool
BuildRequires:  protobuf-c-devel
BuildRequires:  python
BuildRequires:  python3-libmount
BuildRequires:  systemd-devel
BuildRequires:  yajl-devel
# /oreon:deps
%description
%{name} is a OCI runtime

%if %{defined krun_support}
%package krun
Summary: %{name} with libkrun support
Requires: libkrun
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: krun = %{?epoch:%{epoch}:}%{version}-%{release}
%description krun
krun is a symlink to the %{name} binary, with libkrun as an additional dependency.
%endif

%if %{defined wasm_support}
%package wasm
Summary: %{name} with wasm support
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends: wasmedge
%description wasm
%{name}-wasm is a symlink to the %{name} binary, with wasm as an additional dependency.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

./autogen.sh
./configure --disable-silent-rules %{krun_opts} %{wasmedge_opts} %{yajl_opts}
%make_build
%install
%make_install prefix=%{_prefix}
rm -rf %{buildroot}%{_prefix}/lib*
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
