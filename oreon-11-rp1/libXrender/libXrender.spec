%global source0_hash b832128da48b39c8d608224481743403ad1691bf4e554e4be9c174df171d1b97

%global tarball libXrender
#global gitdate 20130524
%global gitversion 786f78fd8

Summary: X.Org X11 libXrender runtime library
Name: libXrender
Version: 0.9.12
Release: 4%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: HPND-sell-variant
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig
BuildRequires: libX11-devel >= 1.5.99.902

%description
X.Org X11 libXrender runtime library

%package devel
Summary: X.Org X11 libXrender development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXrender development package

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
# undo this, we'll add it ourselves in %%doc
rm $RPM_BUILD_ROOT/%{_docdir}/*/libXrender.txt

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING
%{_libdir}/libXrender.so.1
%{_libdir}/libXrender.so.1.3.0

%files devel
%doc doc/libXrender.txt
%{_includedir}/X11/extensions/Xrender.h
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.12-4
- Prepare for Oreon 11 (RP1)
