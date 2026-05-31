%global source0_hash 599ebf9996710fea71622e6e184f3a8ad5b43d0e5fa8c4e407123c88a59a6d55

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:       libxcb
Version:    1.17.0
Release:    7%{?dist}
Summary:    A C binding to the X11 protocol
License:    X11
URL:        http://xcb.freedesktop.org/

Source0:        http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz

# This is stolen straight from the pthread-stubs source:
# http://cgit.freedesktop.org/xcb/pthread-stubs/blob/?id=6900598192bacf5fd9a34619b11328f746a5956d
# we don't need the library because glibc has working pthreads, but we need
# the pkgconfig file so libs that link against libxcb know this...
Source1:    pthread-stubs.pc.in

BuildRequires:  make
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xau) >= 0.99.2
BuildRequires:  pkgconfig(xcb-proto) >= 1.16
BuildRequires:  pkgconfig(xorg-macros) >= 1.18
BuildRequires:  python3 python3-devel

%description
The X protocol C-language Binding (XCB) is a replacement for Xlib featuring a
small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch

%description doc
The %{name}-doc package contains documentation for the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
sed -i 's/pthread-stubs //' configure.ac
# autoreconf -f needed to expunge rpaths
autoreconf -v -f --install
%configure \
    --disable-static \
    --docdir=%{_pkgdocdir} \
    --enable-selinux \
    --enable-xkb \
    --enable-xinput \
    --disable-xprint \
    --disable-silent-rules

# Remove rpath from libtool (extra insurance if autoreconf is ever dropped)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install
install -pm 644 COPYING NEWS README.md %{buildroot}%{_pkgdocdir}
sed 's,@libdir@,%{_libdir},;s,@prefix@,%{_prefix},;s,@exec_prefix@,%{_exec_prefix},' %{SOURCE1} \
    > %{buildroot}%{_libdir}/pkgconfig/pthread-stubs.pc

find %{buildroot} -name '*.la' -delete

# Pick up the license file separately:
rm -f %{buildroot}%{_pkgdocdir}/COPYING

%files
%license COPYING
%{_libdir}/libxcb-composite.so.0*
%{_libdir}/libxcb-damage.so.0*
%{_libdir}/libxcb-dbe.so.0*
%{_libdir}/libxcb-dpms.so.0*
%{_libdir}/libxcb-dri2.so.0*
%{_libdir}/libxcb-dri3.so.0*
%{_libdir}/libxcb-glx.so.0*
%{_libdir}/libxcb-present.so.0*
%{_libdir}/libxcb-randr.so.0*
%{_libdir}/libxcb-record.so.0*
%{_libdir}/libxcb-render.so.0*
%{_libdir}/libxcb-res.so.0*
%{_libdir}/libxcb-screensaver.so.0*
%{_libdir}/libxcb-shape.so.0*
%{_libdir}/libxcb-shm.so.0*
%{_libdir}/libxcb-sync.so.1*
%{_libdir}/libxcb-xf86dri.so.0*
%{_libdir}/libxcb-xfixes.so.0*
%{_libdir}/libxcb-xinerama.so.0*
%{_libdir}/libxcb-xinput.so.0*
%{_libdir}/libxcb-xkb.so.1*
%{_libdir}/libxcb-xselinux.so.0*
%{_libdir}/libxcb-xtest.so.0*
%{_libdir}/libxcb-xv.so.0*
%{_libdir}/libxcb-xvmc.so.0*
%{_libdir}/libxcb.so.1*

%files devel
%{_includedir}/xcb
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*

%files doc
%license COPYING
%{_pkgdocdir}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-7
- Prepare for Oreon 11 (RP1)
