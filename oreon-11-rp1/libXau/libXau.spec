Summary: Sample Authorization Protocol for X
Name: libXau
Version: 1.0.12
Release: 4%{?dist}
License: MIT-open-group
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 74d0e4dfa3d39ad8939e99bda37f5967aba528211076828464d2777d477fc0fb
%global source0_file libXau-1.0.12.tar.xz
# oreon url source checksums end

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel

%description
This is a very simple mechanism for providing individual access to an X Window
System display. It uses existing core protocol and library hooks for specifying
authorization data in the connection setup block to restrict use of the display
to only those clients that show that they know a server-specific key 
called a "magic cookie".

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: xorg-x11-proto-devel
Requires: pkgconfig
BuildRequires: xorg-x11-proto-devel

%description devel
X.Org X11 libXau development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXau-1.0.12.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "74d0e4dfa3d39ad8939e99bda37f5967aba528211076828464d2777d477fc0fb" || { echo "oreon: Source0 SHA256 mismatch for libXau-1.0.12.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
#patch0 -p1 -b .local

%build
autoreconf -v --install --force

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXau.so.6
%{_libdir}/libXau.so.6.0.0

%files devel
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_libdir}/pkgconfig/xau.pc
%{_mandir}/man3/*.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.12-4
- Import
