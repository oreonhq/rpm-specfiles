%global source0_hash 81a99e94c4501e81c427cbaa4a11748b584933e94b7a156830c3621256857bc4
Summary:        X.Org X11 libXmu/libXmuu runtime libraries
Name: libXmu
Version: 1.3.1
Release:        1%{?dist}
License: MIT-open-group AND SMLNJ AND X11 AND ISC
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  xmlto
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXmu/libXmuu runtime libraries

%package devel
Summary: X.Org X11 libXmu development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXmu development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -v --install --force
%configure --disable-static
make  %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXmu-devel -f %{oreon_filedir}/libXmu-devel.list

%changelog

%autochangelog
