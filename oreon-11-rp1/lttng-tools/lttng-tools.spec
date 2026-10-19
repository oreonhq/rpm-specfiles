%global source1_hash 1b148d1e55acbd0202223b5a12888d7e9dea867c25a1bda895c4269489f0fb49
%global source0_hash b8b3244894e49e773d4942b8899f768057974edf75c18dbb48b65bb123c7b2c7
%define with_python          0%{!?_without_python:1}
%if %{with_python}
    %define arg_python --enable-python-bindings
%else
    %define arg_python --disable-python-bindings
%endif
Name:           lttng-tools
Version:        2.16.0
Release:        1%{?dist}
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            http://lttng.org
Summary:        LTTng control and utility programs
Source0:        http://lttng.org/files/lttng-tools/%{name}-%{version}.tar.bz2
Source1:        http://lttng.org/files/lttng-tools/%{name}-%{version}.tar.bz2.asc
Source2:        gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Source3:        lttng-sessiond.service
Source4:        lttng-tools.sysusers.conf
Patch0:         libfmt.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%ifnarch %{arm}
%global _hardened_build 1
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  babeltrace2
BuildRequires:  g++
BuildRequires:  hostname
BuildRequires:  kmod
BuildRequires:  kmod-devel
BuildRequires:  libbabeltrace2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  lttng-ust-devel
BuildRequires:  make
BuildRequires:  popt-devel
BuildRequires:  procps-ng
BuildRequires:  python3-bt2
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  systemd-units
BuildRequires:  systemtap-sdt-devel
BuildRequires:  userspace-rcu-devel
BuildRequires:  xxd
# /oreon:deps
%description
This package provides the unified interface to control both the LTTng kernel
and userspace (UST) tracers.

%package -n %{name}-devel
Summary:        LTTng control and utility library (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n %{name}-devel
This package provides the development files to
implement trace control in external applications

%if %{with_python}
%package -n python3-lttng
Summary:        Python bindings for LTTng
%{?python_provide:%python_provide python3-lttng}
BuildRequires:  swig
BuildRequires:  python3-devel
%description -n python3-lttng
This package provides Python bindings for LTTng
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%undefine _ld_as_needed
autoreconf -vif
touch doc/man/*.1 doc/man/*.3 doc/man/*.8
%configure \
    --disable-static \
    %{?arg_python}
make %{?_smp_mflags} V=1
%check

ulimit -n 4096
make check
%install
make DESTDIR=%{buildroot} install
rm -vf %{buildroot}%{_libdir}/*.la
rm -vf %{buildroot}%{python3_sitearch}/*.la
install -D -m644 %{_sourcedir}/lttng-sessiond.service %{buildroot}%{_unitdir}/lttng-sessiond.service
install -D -m644 extras/lttng-bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/lttng
install -m0644 -D %SOURCE4 %{buildroot}%{_sysusersdir}/lttng-tools.conf
%oreon_autofiles python3-lttng usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

/sbin/ldconfig
%systemd_post lttng-sessiond.service
%preun

%systemd_preun lttng-sessiond.service
%postun

/sbin/ldconfig
%systemd_postun_with_restart lttng-sessiond.service
%files -f %{oreon_filedir}/main.list
%files -n lttng-tools-devel -f %{oreon_filedir}/lttng-tools-devel.list
%files -n python3-lttng -f %{oreon_filedir}/python3-lttng.list

%changelog

%autochangelog
