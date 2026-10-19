%global source0_hash 1781aa049845da89c8fb902ea755123a6710f2b38282a338035caa6211997d14
Version:        3.0.4
%global forgeurl https://github.com/cminyard/gensio
%forgemeta
Name:           gensio
Release:        1%{?dist}
Summary:        General Stream I/O
License:        GPL-2.0-only AND LGPL-2.1-only AND Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  OpenIPMI-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  avahi-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl-devel
# /oreon:deps
%description
This is gensio (pronounced gen'-see-oh), a framework for giving a consistent
view of various stream (and packet) I/O types. You create a gensio object (or
a gensio), and you can use that gensio without having to know too much about
what is going on underneath. You can stack gensio on top of another one to add
protocol functionality. For instance, you can create a TCP gensio, stack SSL on
top of that, and stack Telnet on top of that. It supports a number of network
I/O and serial ports. gensios that stack on other gensios are called filters.

You can do the same thing with receiving ports. You can set up a gensio
accepter (accepter) to accept connections in a stack. So in our previous
example, you can setup TCP to listen on a specific port and automatically stack
SSL and Telnet on top when the connection comes in, and you are not informed
until everything is ready.

A very important feature of gensio is that it makes establishing encrypted and
authenticated connections much easier than without it. Beyond basic key
management, it's really no harder than TCP or anything else. It offers extended
flexibility for controlling the authentication process if needed. It's really
easy to use.

Note that the gensio(5) man page has more details on individual gensio types.

%package     -n libgensio
Summary:        Dynamic gensio Libraries
Requires:       lockdev
%description -n libgensio
The %{name} package contains libraries for applications that use %{name}.

%package     -n libgensio-devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
%description -n libgensio-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n libgensio-ipmisol
Summary:        OpenIPMI support for %{name}
%description -n libgensio-ipmisol
The %{name}-ipmisol package contains additional libraries for OpenIPMI
support in %{name}.

%package     -n libgensio-mdns
Summary:        Avahi (mDNS) support for %{name}
%description -n libgensio-mdns
The %{name}-mdns package contains additional libraries for Avahi (mDNS)
support in %{name}.

%package     -n libgensio-sound
Summary:        ALSA support for %{name}
%description -n libgensio-sound
The %{name}-sound package contains additional libraries for ALSA sound
support in %{name}.

%package     -n libgensio-tcl
Summary:        TCL bindings for %{name}
%description -n libgensio-tcl
The %{name}-tcl package contains TCL bindings for %{name}.

%package     -n python3-%{name}
Summary:        Python library for %{name}
%description -n python3-%{name}
The %{name}-python package contains Python bindings for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

autoreconf -f -i
%configure \
  --enable-static=no \
  --with-go=no \
  --with-pythoninstall=%{python3_sitearch} \
  --with-uucp-locking=%{_rundir}/lock/lockdev
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
sed -i 's|/usr/local/sbin|%{sbindir}|g' tools/gtlsshd.service
install -Dpm 0644 tools/gtlsshd.service %{buildroot}/%{_unitdir}/gtlsshd.service
%oreon_autofiles libgensio usr/*/lib*.so.*
%oreon_autofiles libgensio-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libgensio-ipmisol usr/*/lib*.so.*
%oreon_autofiles libgensio-mdns usr/*/lib*.so.*
%oreon_autofiles libgensio-sound usr/*/lib*.so.*
%oreon_autofiles libgensio-tcl usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post gtlsshd.service
%preun

%systemd_preun gtlsshd.service
%postun

%systemd_postun_with_restart gtlsshd.service
%files -f %{oreon_filedir}/main.list
%files -n libgensio -f %{oreon_filedir}/libgensio.list
%files -n libgensio-devel -f %{oreon_filedir}/libgensio-devel.list
%files -n libgensio-ipmisol -f %{oreon_filedir}/libgensio-ipmisol.list
%files -n libgensio-mdns -f %{oreon_filedir}/libgensio-mdns.list
%files -n libgensio-sound -f %{oreon_filedir}/libgensio-sound.list
%files -n libgensio-tcl -f %{oreon_filedir}/libgensio-tcl.list
%files -n python3-gensio -f %{oreon_filedir}/python3-gensio.list

%changelog

%autochangelog
