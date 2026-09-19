%global source0_hash b64790f94b926acd7e8f84c5d6000a86cb43967bd1e688b03089079799c9e889

%{?mingw_package_header}

%global win32_shared_dir %{_builddir}/mingw32-%{name}-%{version}-%{release}
%global win32_static_dir %{_builddir}/mingw32-%{name}-static-%{version}-%{release}
%global win64_shared_dir %{_builddir}/mingw64-%{name}-%{version}-%{release}
%global win64_static_dir %{_builddir}/mingw64-%{name}-static-%{version}-%{release}

%global pkgname glew

Name:          mingw-%{pkgname}
Version:       2.3.1
Release:       1%{?dist}
Summary:       MinGW Windows GLEW library
License:       BSD-3-Clause AND MIT AND MIT-Khronos-old

BuildArch:     noarch
URL:           https://github.com/nigels-com/glew
Source0:       https://github.com/nigels-com/glew/releases/download/%{pkgname}-%{version}/%{pkgname}-%{version}.tgz
# - Raise minimum cmake version to 3.5
# - Install both static and shared libraries
# - Remove glu requirement in pkgconfig file
Patch0:        glew_cmake.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc

%description
MinGW Windows GLEW library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GLEW library

%description -n mingw32-%{pkgname}
MinGW Windows GLEW library.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of MinGW Windows GLEW library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of MinGW Windows GLEW library.

%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows GLEW library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
Tools for the MinGW Windows GLEW library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GLEW library

%description -n mingw64-%{pkgname}
MinGW Windows GLEW library.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of MinGW Windows GLEW library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of MinGW Windows GLEW library.

%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows GLEW library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
Tools for the MinGW Windows GLEW library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
# ../ because %%mingw_cmake and %%mingw_make work in build_winXX subfolders
%mingw_cmake ../build/cmake
%mingw_make_build

%install
%mingw_make_install

%files -n mingw32-%{pkgname}
%license LICENSE.txt
%{mingw32_bindir}/glew32.dll
%{mingw32_libdir}/pkgconfig/glew.pc
%{mingw32_includedir}/GL/eglew.h
%{mingw32_includedir}/GL/glew.h
%{mingw32_includedir}/GL/glxew.h
%{mingw32_includedir}/GL/wglew.h
%{mingw32_libdir}/libglew32.dll.a
%{mingw32_libdir}/cmake/glew/

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libglew32.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/glewinfo.exe
%{mingw32_bindir}/visualinfo.exe

%files -n mingw64-%{pkgname}
%doc LICENSE.txt
%{mingw64_bindir}/glew32.dll
%{mingw64_libdir}/pkgconfig/glew.pc
%{mingw64_includedir}/GL/eglew.h
%{mingw64_includedir}/GL/glew.h
%{mingw64_includedir}/GL/glxew.h
%{mingw64_includedir}/GL/wglew.h
%{mingw64_libdir}/libglew32.dll.a
%{mingw64_libdir}/cmake/glew/

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libglew32.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/glewinfo.exe
%{mingw64_bindir}/visualinfo.exe

%changelog
%autochangelog
