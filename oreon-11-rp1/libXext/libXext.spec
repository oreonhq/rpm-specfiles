%global source0_hash 6c643c7035cdacf67afd68f25d01b90ef889d546c9fcd7c0adf7c2cf91e3a32d
%global tarball libXext
%global gitversion dfe6e1f3b
Summary:        X.Org X11 libXext runtime library
Name: libXext
Version: 1.3.7
Release:        1%{?dist}
License: MIT-open-group AND X11 AND HPND AND HPND-sell-variant AND SMLNJ AND MIT AND ISC AND HPND-doc AND HPND-doc-sell
URL: http://www.x.org
%if 0%{?gitdate}
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
%endif
Requires: libX11 >= 1.5.99.902
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXext runtime library

%package devel
Summary: X.Org X11 libXext development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXext development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build

autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXext-devel -f %{oreon_filedir}/libXext-devel.list

%changelog

%autochangelog
