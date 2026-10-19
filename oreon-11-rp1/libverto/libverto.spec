%global source0_hash 8d1756fd704f147549f606cd987050fb94b0b1ff621ea6aa4d6bf0b74450468a
%global homepage https://github.com/latchset/libverto
Name:           libverto
Version:        0.3.2
Release:        1%{?dist}
Summary:        Main loop abstraction library
License:        MIT
URL:            %{homepage}
Source0:        https://github.com/latchset/libverto/releases/download/0.3.2/libverto-0.3.2.tar.gz
Obsoletes:      libverto-tevent < 0.3.0-2
Obsoletes:      libverto-tevent-devel < 0.3.0-2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  libev-devel
BuildRequires:  libevent-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libverto provides a way for libraries to expose asynchronous interfaces
without having to choose a particular event loop, offloading this
decision to the end application which consumes the library.

If you are packaging an application, not library, based on libverto,
you should depend either on a specific implementation module or you
can depend on the virtual provides 'libverto-module-base'. This will
ensure that you have at least one module installed that provides io,
timeout and signal functionality. Currently glib is the only module
that does not provide these three because it lacks signal. However,
glib will support signal in the future.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        glib
Summary:        glib module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    glib
Module for %{name} which provides integration with glib.

This package does NOT yet provide %{name}-module-base.

%package        glib-devel
Summary:        Development files for %{name}-glib
Requires:       %{name}-glib%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description    glib-devel
The %{name}-glib-devel package contains libraries and header files for
developing applications that use %{name}-glib.

%package        libevent
Summary:        libevent module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-module-base = %{version}-%{release}
%description    libevent
Module for %{name} which provides integration with libevent.

%package        libevent-devel
Summary:        Development files for %{name}-libevent
Requires:       %{name}-libevent%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description    libevent-devel
The %{name}-libevent-devel package contains libraries and header files for
developing applications that use %{name}-libevent.

%package        libev
Summary:        libev module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-module-base = %{version}-%{release}
%description    libev
Module for %{name} which provides integration with libev.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%package        libev-devel
Summary:        Development files for %{name}-libev
Requires:       %{name}-libev%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description    libev-devel
The %{name}-libev-devel package contains libraries and header files for
developing applications that use %{name}-libev.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%ldconfig_scriptlets glib
%ldconfig_scriptlets libevent
%ldconfig_scriptlets libev
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libverto-devel -f %{oreon_filedir}/libverto-devel.list
%files -n libverto-glib -f %{oreon_filedir}/libverto-glib.list
%files -n libverto-glib-devel -f %{oreon_filedir}/libverto-glib-devel.list
%files -n libverto-libevent -f %{oreon_filedir}/libverto-libevent.list
%files -n libverto-libevent-devel -f %{oreon_filedir}/libverto-libevent-devel.list
%files -n libverto-libev -f %{oreon_filedir}/libverto-libev.list
%files -n libverto-libev-devel -f %{oreon_filedir}/libverto-libev-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.2-12
- Prepare for Oreon 11 (RP1)
