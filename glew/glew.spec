Name:           glew
Version:        2.2.0
Release:        12%{?dist}
Summary:        The OpenGL Extension Wrangler Library
License:        BSD-3-Clause AND MIT AND MIT-Khronos-old
URL:            https://github.com/nigels-com/glew

Source0:        https://github.com/nigels-com/glew/releases/download/glew-%{version}/glew-%{version}.tgz
Patch0:         glew-2.1.0-install.patch
Patch1:         glew-2.2.0-gcc12-cplusplus.patch
BuildRequires:  gcc
BuildRequires:  libGLU-devel
BuildRequires:  make

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library. GLEW provides efficient run-time mechanisms for
determining which OpenGL extensions are supported on the target platform.
OpenGL core and extension functionality is exposed in a single header file.
GLEW is available for a variety of operating systems, including Windows, Linux,
Mac OS X, FreeBSD, Irix, and Solaris.

This package contains the demo GLEW utilities.  The libraries themselves
are in libGLEW.

%package devel
Summary:        Development files for glew
Requires:       libGLEW%{?_isa} = %{version}-%{release}
Requires:       mesa-libGLU-devel%{?_isa}

%description devel
Development files for glew


%package -n libGLEW
Summary:        libGLEW

%description -n libGLEW
libGLEW

%prep
%autosetup -p1

# update config.guess for new arch support
cp /usr/lib/rpm/redhat/config.guess config/

%build
%make_build CFLAGS.EXTRA="$RPM_OPT_FLAGS -fPIC"\
     STRIP= \
     GLEW_PREFIX=%{_prefix} GLEW_DEST=%{_prefix} \
     includedir=%{_includedir} \
     BINDIR=%{_bindir} LIBDIR=%{_libdir} PKGDIR=%{_libdir}/pkgconfig

%install
make install.all DESTDIR="$RPM_BUILD_ROOT" \
     GLEW_PREFIX=%{_prefix} GLEW_DEST=%{_prefix} \
     includedir=%{_includedir} \
     BINDIR=%{_bindir} LIBDIR=%{_libdir} PKGDIR=%{_libdir}/pkgconfig
find $RPM_BUILD_ROOT -type f -name "*.a" -delete
# sigh
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/*.so*

%ldconfig_scriptlets -n libGLEW

%files
%license LICENSE.txt
%{_bindir}/*

%files -n libGLEW
%license LICENSE.txt
%{_libdir}/libGLEW.so.2.2*

%files devel
%{_libdir}/libGLEW.so
%{_libdir}/pkgconfig//glew.pc
%{_includedir}/GL/*.h
%doc doc/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.0-12
- Prepare for Oreon 11 (RP1)
