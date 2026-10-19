%global source0_hash 1a7f7490774c87f2052d146d1e0e64518d32e6848184a18654e8d0bb57883242
Summary:        X.Org X11 libXfont runtime library
Name: libXfont
Version: 1.5.4
Release:        21%{?dist}
License: MIT
URL: http://www.x.org
Source0:        http://www.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freetype-devel
BuildRequires:  libfontenc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  xorg-x11-util-macros
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
X.Org X11 libXfont runtime library

%package devel
Summary: X.Org X11 libXfont development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libfontenc-devel%{?_isa}
%description devel
X.Org X11 libXfont development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

autoreconf -v --install --force
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-static
make %{?_smp_mflags}  
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXfont-devel -f %{oreon_filedir}/libXfont-devel.list

%changelog

%autochangelog
