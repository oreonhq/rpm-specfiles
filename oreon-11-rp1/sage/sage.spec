%global source0_hash 9be861636b52cf978ac009261f133990d332ab4b82331fa6f3fb25e69bd375a3

Name:           sage
Version:        0.2.0
Release:        36%{?dist}
Summary:        OpenGL extensions library using SDL

License:        LGPL-2.0-or-later
URL:            http://worldforge.org/dev/eng/libraries/sage
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz
Patch0:         sage-0.1.2-noopt.patch
Patch1: sage-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel

%description
Sage is an OpenGL extensions library using SDL. It aims to simplify the use of
checking for and loading OpenGL extensions in an application.

%package devel
Summary:        Development files for sage
Requires: pkgconfig %{name} = %{version}-%{release}

%description devel
Libraries and header files for developing applications that use sage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
touch -r configure.ac configure.ac.stamp
%patch -P0 -p0
%patch -P1 -p1
touch -r configure.ac.stamp configure.ac
rm -f sage/glxext_sage.h
rm -f sage/wglext_sage.h

%build
%configure --disable-static
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}.la

%check
# There are no tests yet, but upstream tends to be good about adding 
# them.  This is a placeholder for when upstread finally adds the tests.
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.gz

%changelog
%autochangelog
