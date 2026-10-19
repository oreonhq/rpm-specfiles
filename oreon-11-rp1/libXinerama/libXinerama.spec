%global source0_hash d00fc1599c303dc5cbc122b8068bdc7405d6fcb19060f4597fc51bd3a8be51d7
%global tarball libXinerama
%global gitversion 99c644fc8
Summary:        X.Org X11 libXinerama runtime library
Name: libXinerama
Version: 1.1.6
Release:        1%{?dist}
License: MIT AND MIT-open-group AND X11
URL: http://www.x.org
%if 0%{?gitdate}
Source0:        https://xorg.freedesktop.org/releases/individual/lib/libXinerama-1.1.6.tar.xz
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
%endif
Requires: libX11 >= 1.5.99.902
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXinerama runtime library

%package devel
Summary: X.Org X11 libXinerama development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXinerama development package

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
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXinerama-devel -f %{oreon_filedir}/libXinerama-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.5-10
- Import
