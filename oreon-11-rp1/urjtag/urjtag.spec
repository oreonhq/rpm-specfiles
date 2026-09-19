%global source0_hash b0a2eaa245513af096dc4d770109832335c694c6c12aa5e92fefae8685416f1c

%if 0%{?centos} > 6 || 0%{?rhel} > 6 || 0%{?fedora}
%global with_python3 1
%else
%global without_python3 1
%endif

Name:           urjtag
Version:        2021.03
Release:        20%{?dist}
Summary:        A tool for communicating over JTAG with flash chips and CPUs

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://urjtag.org
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:         %{name}-fixarm.patch

%global py3_prefix python3

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libftdi-devel
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  readline-devel
BuildRequires:  swig
%if 0%{?rhel} || 0%{?centos}
BuildRequires: %{py3_prefix}4-devel
%else
BuildRequires: %{py3_prefix}-devel
%endif
BuildRequires:  bison
BuildRequires:  flex

%description
UrJTAG aims to create an enhanced, modern tool for communicating
over JTAG with flash chips, CPUs, and many more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n %{py3_prefix}-%{name}
%if 0%{?rhel} || 0%{?centos}
Provides:       python3-%{name}
%else
%{?python_provide:%python_provide %{py3_prefix}-%{name}}
%endif
Summary:        Python bindings for %{name}
Requires:       %{name} = %{version}-%{release}

%description    -n %{py3_prefix}-%{name}
Python bindings and examples for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p2 -b .armfix

%build
%configure --enable-jedec-exp --enable-stapl --enable-bsdl --enable-svf --disable-static --enable-shared
# V=1: verbose build, disables AM_SILENT_RULES
%{__make} %{?_smp_mflags} V=1
pushd bindings/python/
%py3_build

%install
# cd urjtag
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
%find_lang %{name}
pushd bindings/python/
%py3_install

%ldconfig_scriptlets
 
%files -f %{name}.lang
%doc README NEWS ChangeLog COPYING AUTHORS
%doc doc/howto_add_support_for_more_flash.txt
%doc doc/README.ejtag doc/README.pld doc/README.stapl
%doc doc/UrJTAG.txt
%{_bindir}/jtag
%{_bindir}/bsdl2jtag
%{_libdir}/liburjtag.so.*
%dir %{_datadir}/urjtag/
%{_datadir}/urjtag/*
%{_mandir}/man1/jtag.1*
%{_mandir}/man1/bsdl2jtag.1*

%files devel
%dir %{_includedir}/urjtag
%{_includedir}/urjtag/*.h
%{_libdir}/liburjtag.so
%{_libdir}/pkgconfig/urjtag.pc

%files -n %{py3_prefix}-%{name}
%{python3_sitearch}/urjtag*
%doc doc/urjtag-python.txt 
%doc bindings/python/t_urjtag_chain.py
%doc bindings/python/t_srst.py

%changelog
%autochangelog
