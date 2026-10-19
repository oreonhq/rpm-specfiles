%global source0_hash f042a370666815e7b941e9b7019024755bd1c6c2954afbfa515af378251799e2
Summary:        X.Org X11 libXfont2 runtime library
Name: libXfont2
Version: 2.0.9
Release:        1%{?dist}
License: BSD-2-Clause AND BSD-4-Clause-UC AND HPND-sell-variant AND MIT-open-group AND SMLNJ AND X11
URL: http://www.x.org
Source0:        http://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
Requires:       libfontenc%{?_isa}
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
X.Org X11 libXfont2 runtime library

%package devel
Summary: X.Org X11 libXfont2 development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libfontenc-devel%{?_isa}
%description devel
X.Org X11 libXfont development package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%files -n libXfont2-devel -f %{oreon_filedir}/libXfont2-devel.list

%changelog

%autochangelog
