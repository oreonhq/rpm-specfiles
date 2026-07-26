%global source0_hash d8c39c26cec13b7bd82551cd52a22efc358b888e36ebcf9c1b60ef1c3a3c2fd3

%define with_python          0%{!?_without_python:1}

%if %{with_python}
    %define arg_python --enable-python-bindings
%else
    %define arg_python --disable-python-bindings
%endif

Name:           lttng-tools
Version:        2.14.0
Release:        5%{?dist}
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            http://lttng.org
Summary:        LTTng control and utility programs
Source0:        http://lttng.org/files/lttng-tools/%{name}-%{version}.tar.bz2
Source1:        http://lttng.org/files/lttng-tools/%{name}-%{version}.tar.bz2.asc
# gpg2 --export --export-options export-minimal 7F49314A26E0DE78427680E05F1B2A0789F12B11 > gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Source2:        gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Source3:        lttng-sessiond.service
Source4:        lttng-tools.sysusers.conf

Patch0:         libfmt.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  g++
BuildRequires:  kmod-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel >= 2.7.6
BuildRequires:  lttng-ust-devel >= 2.14.0
BuildRequires:  lttng-ust-devel < 2.15.0
BuildRequires:  make
BuildRequires:  popt-devel >= 1.13
BuildRequires:  systemd-units
BuildRequires:  systemtap-sdt-devel
BuildRequires:  userspace-rcu-devel >= 0.14.0

# For check
BuildRequires:  babeltrace2
BuildRequires:  hostname
BuildRequires:  kmod
BuildRequires:  libbabeltrace2-devel
BuildRequires:  procps-ng
BuildRequires:  python3-bt2
BuildRequires:  xxd

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

#GCC crash when building this package on arm with hardening activated (See bug 987192).
%ifnarch %{arm}
%global _hardened_build 1
%endif

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

%autosetup -p1

%build
# The build flags include -Wl,--as-needed by default, and this causes
# some tests to fail (eg. regression/ust/libc-wrapper)
%undefine _ld_as_needed
# Reinitialize libtool with the fedora version to remove Rpath
autoreconf -vif
touch doc/man/*.1 doc/man/*.3 doc/man/*.8

%configure \
    --disable-static \
    %{?arg_python}

make %{?_smp_mflags} V=1

%check
# Tests (eg. test_nprocesses) were failing with the default open files limit (1024)
ulimit -n 4096
make check

%install
make DESTDIR=%{buildroot} install
rm -vf %{buildroot}%{_libdir}/*.la
rm -vf %{buildroot}%{python3_sitearch}/*.la
install -D -m644 %{_sourcedir}/lttng-sessiond.service %{buildroot}%{_unitdir}/lttng-sessiond.service
# Install upstream bash auto completion for lttng
install -D -m644 extras/lttng-bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/lttng

install -m0644 -D %SOURCE4 %{buildroot}%{_sysusersdir}/lttng-tools.conf

%post
/sbin/ldconfig
%systemd_post lttng-sessiond.service

%preun
%systemd_preun lttng-sessiond.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart lttng-sessiond.service

%files
%dir %{_libdir}/lttng
%dir %{_libdir}/lttng/libexec
%{_bindir}/lttng
%{_bindir}/lttng-crash
%{_bindir}/lttng-sessiond
%{_bindir}/lttng-relayd
%{_libdir}/lttng/libexec/lttng-consumerd
%{_libdir}/*.so.*
%{_mandir}/man1/lttng.1.gz
%{_mandir}/man1/lttng-add-context.1.gz
%{_mandir}/man1/lttng-add-trigger.1.gz
%{_mandir}/man1/lttng-clear.1.gz
%{_mandir}/man1/lttng-crash.1.gz
%{_mandir}/man1/lttng-create.1.gz
%{_mandir}/man1/lttng-destroy.1.gz
%{_mandir}/man1/lttng-disable-channel.1.gz
%{_mandir}/man1/lttng-disable-event.1.gz
%{_mandir}/man1/lttng-disable-rotation.1.gz
%{_mandir}/man1/lttng-enable-channel.1.gz
%{_mandir}/man1/lttng-enable-event.1.gz
%{_mandir}/man1/lttng-enable-rotation.1.gz
%{_mandir}/man1/lttng-help.1.gz
%{_mandir}/man1/lttng-list.1.gz
%{_mandir}/man1/lttng-list-triggers.1.gz
%{_mandir}/man1/lttng-load.1.gz
%{_mandir}/man1/lttng-metadata.1.gz
%{_mandir}/man1/lttng-regenerate.1.gz
%{_mandir}/man1/lttng-remove-trigger.1.gz
%{_mandir}/man1/lttng-rotate.1.gz
%{_mandir}/man1/lttng-save.1.gz
%{_mandir}/man1/lttng-set-session.1.gz
%{_mandir}/man1/lttng-snapshot.1.gz
%{_mandir}/man1/lttng-start.1.gz
%{_mandir}/man1/lttng-status.1.gz
%{_mandir}/man1/lttng-stop.1.gz
%{_mandir}/man1/lttng-track.1.gz
%{_mandir}/man1/lttng-untrack.1.gz
%{_mandir}/man1/lttng-version.1.gz
%{_mandir}/man1/lttng-view.1.gz
%{_mandir}/man7/lttng-concepts.7.gz
%{_mandir}/man7/lttng-event-rule.7.gz
%{_mandir}/man8/lttng-relayd.8.gz
%{_mandir}/man8/lttng-sessiond.8.gz
%{_defaultdocdir}/%{name}/LICENSE
%{_defaultdocdir}/%{name}/README.adoc
%{_defaultdocdir}/%{name}/ChangeLog
%{_defaultdocdir}/%{name}/live-reading-howto.txt
%{_defaultdocdir}/%{name}/python-howto.txt
%{_defaultdocdir}/%{name}/quickstart.txt
%{_defaultdocdir}/%{name}/snapshot-howto.txt
%{_defaultdocdir}/%{name}/streaming-howto.txt
%{_unitdir}/lttng-sessiond.service
%{_sysconfdir}/bash_completion.d/
%{_datadir}/xml/lttng/session.xsd
%{_sysusersdir}/lttng-tools.conf

%files -n %{name}-devel
%{_mandir}/man3/lttng-health-check.3.gz
%{_defaultdocdir}/%{name}/live-reading-protocol.txt
%{_defaultdocdir}/%{name}/valgrind-howto.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lttng-ctl.pc

%if %{with_python}
%files -n python%{python3_pkgversion}-lttng
%{_defaultdocdir}/%{name}/python-howto.txt
%{python3_sitelib}/lttng.py
%{python3_sitelib}/__pycache__/*.pyc
%{python3_sitearch}/_lttng.so*
%endif

%changelog
%autochangelog
