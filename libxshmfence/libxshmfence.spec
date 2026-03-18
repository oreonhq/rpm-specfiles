Name:           libxshmfence
Version:        1.3.2
Release:        8%{?dist}
Summary:        X11 shared memory fences

License:        HPND-sell-variant
URL:            https://www.x.org/
Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
Patch0:         0001-alloc-Allow-disabling-memfd-usage-at-runtime-with-XS.patch

# upstream tarball has broken libtool because libtool is never not broken
BuildRequires:  autoconf automake libtool xorg-x11-util-macros
BuildRequires:  pkgconfig(xproto)
BuildRequires: make
#Requires:       

%description
Shared memory fences for X11, as used in DRI3.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
autoreconf -v -i -f
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_post
%ldconfig_postun

%files
%doc
%license COPYING
%{_libdir}/libxshmfence.so.1*

%files devel
%doc
%{_includedir}/*
%{_libdir}/pkgconfig/xshmfence.pc
%{_libdir}/*.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-8
- Prepare for Oreon 11 (RP1)
