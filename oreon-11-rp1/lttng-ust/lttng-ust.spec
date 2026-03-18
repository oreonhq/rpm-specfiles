%define with_numactl          0%{!?_without_numactl:1}

# Numactl is not available on armhf
%ifarch armv7hl
%define with_numactl 0
%endif

%if %{with_numactl}
    %define arg_numactl --enable-numa
%else
    %define arg_numactl --disable-numa
%endif


Name:           lttng-ust
Version:        2.15.0
Release:        1%{?dist}

License:        LGPL-2.1-only AND MIT AND GPL-2.0-only AND BSD-3-Clause AND BSD-2-Clause
Summary:        LTTng Userspace Tracer library
URL:            https://lttng.org
Source0:        https://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2
Source1:        https://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2.asc
# gpg2 --export --export-options export-minimal 2A0B4ED915F2D3FA45F5B16217280A9781186ACF > gpgkey-2A0B4ED915F2D3FA45F5B16217280A9781186ACF.gpg
Source2:        gpgkey-2A0B4ED915F2D3FA45F5B16217280A9781186ACF.gpg
Patch0:         lttng-gen-tp-shebang.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  g++
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig
BuildRequires:  systemtap-sdt-devel
BuildRequires:  userspace-rcu-devel >= 0.15.0
%if %{with_numactl}
BuildRequires:  numactl-devel
%endif

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
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# Reinitialize libtool with the fedora version to remove Rpath
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

%check
make check

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%{_mandir}/man3/do_tracepoint.3.gz
%{_mandir}/man3/lttng-ust.3.gz
%{_mandir}/man3/lttng-ust-cyg-profile.3.gz
%{_mandir}/man3/lttng-ust-dl.3.gz
%{_mandir}/man3/lttng_ust_do_tracepoint.3.gz
%{_mandir}/man3/lttng_ust_tracef.3.gz
%{_mandir}/man3/lttng_ust_tracelog.3.gz
%{_mandir}/man3/lttng_ust_tracepoint.3.gz
%{_mandir}/man3/lttng_ust_tracepoint_enabled.3.gz
%{_mandir}/man3/lttng_ust_vtracef.3.gz
%{_mandir}/man3/lttng_ust_vtracelog.3.gz
%{_mandir}/man3/tracef.3.gz
%{_mandir}/man3/tracelog.3.gz
%{_mandir}/man3/tracepoint.3.gz
%{_mandir}/man3/tracepoint_enabled.3.gz

%dir %{_docdir}/%{name}
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/java-agent.md
%{_docdir}/%{name}/python-agent.md
%{_docdir}/%{name}/LICENSE
%{_docdir}/%{name}/README.md


%files -n %{name}-devel
%{_bindir}/lttng-gen-tp
%{_mandir}/man1/lttng-gen-tp.1.gz
%{_prefix}/include/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lttng-ust*.pc

%dir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples/*

%files -n python3-lttngust
%{python3_sitelib}/lttngust/
%{python3_sitelib}/lttngust-*.egg-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15.0-1
- Prepare for Oreon 11 (RP1)
