%global source0_hash 75e20d1744139644f9951b78ea3910b162d3380302315cb4b3d0640f23694c79

Name:		libgxim
Version:	0.5.0
Release:	32%{?dist}
License:	LGPL-2.1-or-later
URL:		https://gitlab.com/tagoh/libgxim/
BuildRequires:	intltool gettext ruby rubygems
BuildRequires:	glib2-devel >= 2.26, gtk2-devel
BuildRequires:	gcc
BuildRequires: make
Source0:	http://bitbucket.org/tagoh/%{name}/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-fix-build.patch

Summary:	GObject-based XIM protocol library

%description
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

This package contains the shared library.

%package	devel
Summary:	Development files for libgxim
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	glib2-devel >= 2.26.0
Requires:	gtk2-devel

%description	devel
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

This package contains the development files to make any applications with
libgxim.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static --disable-rebuilds

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# clean up the unnecessary files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/libgxim.so.*

%files	devel
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/libgxim.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libgxim
%{_datadir}/gtk-doc/html/libgxim

%changelog
%autochangelog
