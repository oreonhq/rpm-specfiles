%global source1_hash 469eb1e8e371eaaebd3886155ff75e41505c18516e42782467cd3e3733946f58
%global source0_hash 1e84e02fa1fc1261eb6cf3d14d64006506a29f7c605ac85de02180318c6aa38a
%global source2_key_fpr 2A0B4ED915F2D3FA45F5B16217280A9781186ACF
%define with_numactl          0%{!?_without_numactl:1}
%ifarch armv7hl
%define with_numactl 0
%endif
%if %{with_numactl}
    %define arg_numactl --enable-numa
%else
    %define arg_numactl --disable-numa
%endif
Name:           lttng-ust
Version:        2.16.0
Release:        1%{?dist}
License:        LGPL-2.1-only AND MIT AND GPL-2.0-only AND BSD-3-Clause AND BSD-2-Clause
Summary:        LTTng Userspace Tracer library
URL:            https://lttng.org
Source0:        https://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2
Source1:        https://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2.asc
Source2:        gpgkey-2A0B4ED915F2D3FA45F5B16217280A9781186ACF.gpg
Patch0:        lttng-gen-tp-shebang.patch
%if %{with_numactl}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  g++
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemtap-sdt-devel
BuildRequires:  userspace-rcu-devel
# /oreon:deps
%description
This library may be used by user-space applications to generate 
trace-points using LTTng.

%package -n %{name}-devel
Summary:        LTTng Userspace Tracer library headers and development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       userspace-rcu-devel
Requires:       systemtap-sdt-devel
%description -n %{name}-devel
The %{name}-devel package contains libraries and header to instrument
applications using %{name}

%package -n python3-lttngust
Summary:        Python bindings for LTTng UST
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires: make
%{?python_provide:%python_provide python3-lttngust}
%description -n python3-lttngust
The python3-lttngust package contains libraries needed to instrument
applications that use %{name}'s Python logging backend.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -vif
%ifarch armv7hl
export CPPFLAGS="-DUATOMIC_NO_LINK_ERROR"
%endif
%configure \
	--docdir=%{_docdir}/%{name} \
	--disable-static \
	--enable-python-agent \
	--with-sdt \
	%{?arg_numactl}
make %{?_smp_mflags} V=1
%install
make DESTDIR=%{buildroot} install
rm -vf %{buildroot}%{_libdir}/*.la
%oreon_autofiles python3-lttngust usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n lttng-ust-devel -f %{oreon_filedir}/lttng-ust-devel.list
%files -n python3-lttngust -f %{oreon_filedir}/python3-lttngust.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15.0-1
- Prepare for Oreon 11 (RP1)
