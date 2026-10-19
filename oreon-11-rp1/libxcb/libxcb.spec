%global source0_hash 599ebf9996710fea71622e6e184f3a8ad5b43d0e5fa8c4e407123c88a59a6d55
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:       libxcb
Version:    1.17.0
Release:        7%{?dist}
Summary:        A C binding to the X11 protocol
License:    X11
URL:        http://xcb.freedesktop.org/
Source0:        http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
Source1:    pthread-stubs.pc.in
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  python3
BuildRequires:  python3-devel
# /oreon:deps
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
%oreon_prep
%build

sed -i 's/pthread-stubs //' configure.ac
autoreconf -v -f --install
%configure \
    --disable-static \
    --docdir=%{_pkgdocdir} \
    --enable-selinux \
    --enable-xkb \
    --enable-xinput \
    --disable-xprint \
    --disable-silent-rules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
install -pm 644 COPYING NEWS README.md %{buildroot}%{_pkgdocdir}
sed 's,@libdir@,%{_libdir},;s,@prefix@,%{_prefix},;s,@exec_prefix@,%{_exec_prefix},' %{SOURCE1} \
    > %{buildroot}%{_libdir}/pkgconfig/pthread-stubs.pc
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_pkgdocdir}/COPYING
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libxcb-devel -f %{oreon_filedir}/libxcb-devel.list
%files -n libxcb-doc -f %{oreon_filedir}/libxcb-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-7
- Prepare for Oreon 11 (RP1)
