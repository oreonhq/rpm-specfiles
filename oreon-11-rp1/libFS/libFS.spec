%global source0_hash 597379438b3242ccc7d7b0fc432dc6c844eca0d4a82a7b82518bfeb203fc208a

%global tarball libFS
#global gitdate 20130524
#global gitversion 26dc23446

Summary: X.Org X11 libFS runtime library
Name: libFS
Version: 1.0.9
Release: 9%{?dist}
License: MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:    %{tarball}-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
%endif

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool make
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-4

%description
X.Org X11 libFS runtime library

%package devel
Summary: X.Org X11 libFS development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libFS development package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# hack, we'll %%doc this on our own
rm -rf $RPM_BUILD_ROOT%{_docdir}

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README.md
%{_libdir}/libFS.so.6
%{_libdir}/libFS.so.6.0.0

%files devel
%doc doc/FSlib.txt
%{_includedir}/X11/fonts/FSlib.h
%{_libdir}/libFS.so
%{_libdir}/pkgconfig/libfs.pc

%changelog
%autochangelog
