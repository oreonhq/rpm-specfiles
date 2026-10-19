%global source0_hash c0beb4747528ad931da43acc567c6a0190f7fc624465571ed9ccece02c34dd23
%global tls_priority "@LIBVIRT,SYSTEM"
%global with_mingw 0
%if 0%{?fedora} || (0%{?oreon} >= 11)
%ifarch aarch64 armv7hl armv8l ppc64le s390x riscv64
%global with_mingw 0
%else
%global with_mingw 1
%endif
%endif
Summary:        A GTK widget for VNC clients
Name: gtk-vnc
Version: 1.5.0
%global verdir %(echo %{version} | cut -d. -f1,2)
Release:        1%{?dist}
License: LGPL-2.1-or-later
Source0:        https://download.gnome.org/sources/%{name}/%{verdir}/%{name}-%{version}.tar.xz
Patch0:        0001-make-gtk-vnc-debug-work-with-new-glib.patch
URL: https://gitlab.gnome.org/GNOME/gtk-vnc
Requires: gvnc = %{version}-%{release}
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  gmp-devel
BuildRequires:  gnutls-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  meson
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gmp
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gmp
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw64-gtk3
BuildRequires:  perl-podlators
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel
BuildRequires:  vala
BuildRequires:  zlib-devel
# /oreon:deps
%description
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%package -n gvnc
Summary: A GObject for VNC connections
%description -n gvnc
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

%package -n gvnc-devel
Summary: Libraries, includes, etc. to compile with the gvnc library
Requires: gvnc = %{version}-%{release}
Requires: pkgconfig
%description -n gvnc-devel
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

Libraries, includes, etc. to compile with the gvnc library

%package -n gvncpulse
Summary: A Pulse Audio bridge for VNC connections
Requires: gvnc = %{version}-%{release}
%description -n gvncpulse
gvncpulse is a bridge to the Pulse Audio system for VNC.
It allows VNC clients to play back audio on the local
system

%package -n gvncpulse-devel
Summary: Libraries, includes, etc. to compile with the gvncpulse library
Requires: gvncpulse = %{version}-%{release}
Requires: pkgconfig
%description -n gvncpulse-devel
gvncpulse is a bridge to the Pulse Audio system for VNC.
It allows VNC clients to play back audio on the local
system

Libraries, includes, etc. to compile with the gvnc library

%package -n gvnc-tools
Summary: Command line VNC tools
Requires: gvnc = %{version}-%{release}
%description -n gvnc-tools
Provides useful command line utilities for interacting with
VNC servers. Includes the gvnccapture program for capturing
screenshots of a VNC desktop

%package -n gtk-vnc2
Summary: A GTK3 widget for VNC clients
Requires: gvnc = %{version}-%{release}
Obsoletes: gtk-vnc < 1.0.0
%description -n gtk-vnc2
gtk-vnc is a VNC viewer widget for GTK3. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%package -n gtk-vnc2-devel
Summary: Development files to build GTK3 applications with gtk-vnc
Requires: gtk-vnc2 = %{version}-%{release}
Requires: pkgconfig
Requires: gtk3-devel
Obsoletes: gtk-vnc-devel < 1.0.0
%description -n gtk-vnc2-devel
gtk-vnc is a VNC viewer widget for GTK3. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

Libraries, includes, etc. to compile with the gtk-vnc library

# Mingw32
%package -n mingw32-gvnc
Summary: MinGW Windows port of VNC GObject
BuildArch: noarch
%package -n mingw32-gvnc-tools
Summary: Command line VNC tools
BuildArch: noarch
%package -n mingw32-gtk-vnc2
Summary: A GTK3 widget for VNC clients
Requires: pkgconfig
Obsoletes: mingw32-gtk-vnc < 1.0.0
BuildArch: noarch
%description -n mingw32-gvnc
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

%description -n mingw32-gvnc-tools
Provides useful command line utilities for interacting with
VNC servers. Includes the gvnccapture program for capturing
screenshots of a VNC desktop

%description -n mingw32-gtk-vnc2
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

# Mingw64
%package -n mingw64-gvnc
Summary: MinGW Windows port of VNC GObject
BuildArch: noarch
%package -n mingw64-gvnc-tools
Summary: Command line VNC tools
BuildArch: noarch
%package -n mingw64-gtk-vnc2
Summary: A GTK3 widget for VNC clients
Requires: pkgconfig
Obsoletes: mingw64-gtk-vnc < 1.0.0
BuildArch: noarch
%description -n mingw64-gvnc
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

%description -n mingw64-gvnc-tools
Provides useful command line utilities for interacting with
VNC servers. Includes the gvnccapture program for capturing
screenshots of a VNC desktop

%description -n mingw64-gtk-vnc2
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gtk-vnc-%{version}
%oreon_prep
%build

%meson
%meson_build
chmod -x examples/*.pl examples/*.js examples/*.py
%mingw_meson -Dintrospection=disabled -Dgi-docs=disabled
%mingw_ninja
%install
%meson_install
%find_lang %{name}
export DESTDIR=%{buildroot}
%mingw_ninja install
rm -f $RPM_BUILD_ROOT%{mingw32_mandir}/man1/gvnccapture.1*
rm -f $RPM_BUILD_ROOT%{mingw64_mandir}/man1/gvnccapture.1*
%mingw_debug_install_post
%mingw_find_lang gtk-vnc
%oreon_autofiles gvnc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gvnc-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gvncpulse usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gvncpulse-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gvnc-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gtk-vnc2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gtk-vnc2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mingw32-gvnc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-gvnc-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-gtk-vnc2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gvnc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gvnc-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gtk-vnc2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gvnc -f %{oreon_filedir}/gvnc.list
%files -n gvnc-devel -f %{oreon_filedir}/gvnc-devel.list
%files -n gvncpulse -f %{oreon_filedir}/gvncpulse.list
%files -n gvncpulse-devel -f %{oreon_filedir}/gvncpulse-devel.list
%files -n gvnc-tools -f %{oreon_filedir}/gvnc-tools.list
%files -n gtk-vnc2 -f %{oreon_filedir}/gtk-vnc2.list
%files -n gtk-vnc2-devel -f %{oreon_filedir}/gtk-vnc2-devel.list
%files -n mingw32-gvnc -f %{oreon_filedir}/mingw32-gvnc.list
%files -n mingw32-gvnc-tools -f %{oreon_filedir}/mingw32-gvnc-tools.list
%files -n mingw32-gtk-vnc2 -f %{oreon_filedir}/mingw32-gtk-vnc2.list
%files -n mingw64-gvnc -f %{oreon_filedir}/mingw64-gvnc.list
%files -n mingw64-gvnc-tools -f %{oreon_filedir}/mingw64-gvnc-tools.list
%files -n mingw64-gtk-vnc2 -f %{oreon_filedir}/mingw64-gtk-vnc2.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-1
- Import
