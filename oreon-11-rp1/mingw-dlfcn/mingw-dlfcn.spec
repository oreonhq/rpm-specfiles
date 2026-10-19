%global source0_hash f61a874bc9163ab488accb364fd681d109870c86e8071f4710cbcdcbaf9f2565
%global mingw_build_ucrt64 1
%{?mingw_package_header}
%global realname dlfcn-win32
Name:          mingw-dlfcn
Version:       1.4.2
Release:        3%{?dist}
Summary:        Implements a wrapper for dlfcn (dlopen dlclose dlsym dlerror)
License:       MIT
URL:           https://github.com/%{realname}/%{realname}
Source0:        https://github.com/%{realname}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc
# /oreon:deps
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

export MINGW_BUILDDIR_SUFFIX=-shared
%mingw_cmake
%mingw_make_build
export MINGW_BUILDDIR_SUFFIX=-static
%mingw_cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%mingw_make_build
%install
export MINGW_BUILDDIR_SUFFIX=-shared
%mingw_make_install
export MINGW_BUILDDIR_SUFFIX=-static
%mingw_make_install
%oreon_autofiles mingw32-dlfcn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-dlfcn-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-dlfcn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-dlfcn-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-dlfcn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-dlfcn-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-dlfcn -f %{oreon_filedir}/mingw32-dlfcn.list
%files -n mingw32-dlfcn-static -f %{oreon_filedir}/mingw32-dlfcn-static.list
%files -n mingw64-dlfcn -f %{oreon_filedir}/mingw64-dlfcn.list
%files -n mingw64-dlfcn-static -f %{oreon_filedir}/mingw64-dlfcn-static.list
%files -n ucrt64-dlfcn -f %{oreon_filedir}/ucrt64-dlfcn.list
%files -n ucrt64-dlfcn-static -f %{oreon_filedir}/ucrt64-dlfcn-static.list

%changelog

%autochangelog
