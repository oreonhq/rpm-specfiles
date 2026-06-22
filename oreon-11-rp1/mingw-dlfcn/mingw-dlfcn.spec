%global source0_hash f61a874bc9163ab488accb364fd681d109870c86e8071f4710cbcdcbaf9f2565

%global mingw_build_ucrt64 1
%{?mingw_package_header}

%global realname dlfcn-win32

Name:          mingw-dlfcn
Version:       1.4.2
Release:       3%{?dist}
Summary:       Implements a wrapper for dlfcn (dlopen dlclose dlsym dlerror)

License:       MIT
URL:           https://github.com/%{realname}/%{realname}
Source0:       https://github.com/%{realname}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz

BuildArch:     noarch

BuildRequires: cmake
BuildRequires: make

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils

BuildRequires: ucrt64-filesystem
BuildRequires: ucrt64-gcc
BuildRequires: ucrt64-binutils


%description
This library implements a wrapper for dlfcn, as specified in POSIX and SUS,
around the dynamic link library functions found in the Windows API.


# Win32
%package -n mingw32-dlfcn
Summary:        Implements a wrapper for dlfcn (dlopen dlclose dlsym dlerror)

%description -n mingw32-dlfcn
This library implements a wrapper for dlfcn, as specified in POSIX and SUS,
around the dynamic link library functions found in the Windows API.


%package -n mingw32-dlfcn-static
Summary:        Static version of the MinGW Windows dlfcn library
Requires:       mingw32-dlfcn = %{version}-%{release}

%description -n mingw32-dlfcn-static
Static version of the MinGW Windows dlfcn library.


# Win64
%package -n mingw64-dlfcn
Summary:        Implements a wrapper for dlfcn (dlopen dlclose dlsym dlerror)

%description -n mingw64-dlfcn
This library implements a wrapper for dlfcn, as specified in POSIX and SUS,
around the dynamic link library functions found in the Windows API.


%package -n mingw64-dlfcn-static
Summary:        Static version of the MinGW Windows dlfcn library
Requires:       mingw64-dlfcn = %{version}-%{release}

%description -n mingw64-dlfcn-static
Static version of the MinGW Windows dlfcn library.


# UCRT64
%package -n ucrt64-dlfcn
Summary:        Implements a wrapper for dlfcn (dlopen dlclose dlsym dlerror)

%description -n ucrt64-dlfcn
This library implements a wrapper for dlfcn, as specified in POSIX and SUS,
around the dynamic link library functions found in the Windows API.


%package -n ucrt64-dlfcn-static
Summary:        Static version of the MinGW Windows dlfcn library
Requires:       ucrt64-dlfcn = %{version}-%{release}

%description -n ucrt64-dlfcn-static
Static version of the MinGW Windows dlfcn library.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{realname}-%{version}

for f in README.md COPYING; do
    %{__sed} -i 's/\r//' "${f}";
done


%build
# Shared
export MINGW_BUILDDIR_SUFFIX=-shared
%mingw_cmake
%mingw_make_build

# Static
export MINGW_BUILDDIR_SUFFIX=-static
%mingw_cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%mingw_make_build


%install
# Shared
export MINGW_BUILDDIR_SUFFIX=-shared
%mingw_make_install

# Static
export MINGW_BUILDDIR_SUFFIX=-static
%mingw_make_install


# Win32
%files -n mingw32-dlfcn
%doc README.md
%license COPYING
%{mingw32_bindir}/libdl.dll
%{mingw32_libdir}/libdl.dll.a
%{mingw32_includedir}/dlfcn.h
%{mingw32_datadir}/%{realname}

%files -n mingw32-dlfcn-static
%{mingw32_libdir}/libdl.a

# Win64
%files -n mingw64-dlfcn
%doc README.md
%license COPYING
%{mingw64_bindir}/libdl.dll
%{mingw64_libdir}/libdl.dll.a
%{mingw64_includedir}/dlfcn.h
%{mingw64_datadir}/%{realname}

%files -n mingw64-dlfcn-static
%{mingw64_libdir}/libdl.a

# UCRT64
%files -n ucrt64-dlfcn
%doc README.md
%license COPYING
%{ucrt64_bindir}/libdl.dll
%{ucrt64_libdir}/libdl.dll.a
%{ucrt64_includedir}/dlfcn.h
%{ucrt64_datadir}/%{realname}

%files -n ucrt64-dlfcn-static
%{ucrt64_libdir}/libdl.a

%changelog
%autochangelog
