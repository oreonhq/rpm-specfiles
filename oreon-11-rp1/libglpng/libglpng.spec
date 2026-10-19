%global source0_hash c5634a4aca62d94a2c3fd056d8b12da9ad10aba48155bfbed61ff1a350fabba0
Name:           libglpng
Version:        1.45
Release:        36%{?dist}
Summary:        Toolkit for loading PNG images as OpenGL textures
License:        MIT
URL:            https://admin.fedoraproject.org/pkgdb/packages/name/libglpng
Source0:        http://ftp.de.debian.org/debian/pool/main/libg/%{name}/%{name}_%{version}.orig.tar.gz
Source1:        libglpng-1.45-makefile
Patch0:         libglpng-1.45-debian.patch
Patch1:         libglpng-1.45-CVE-2010-1519.patch
Patch2:         libglpng-1.45-libpng15.patch
Patch3: glpng-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libGL-devel
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
glpng is a small toolkit to make loading PNG image files as an OpenGL
texture as easy as possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}.orig
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
cp %{SOURCE1} Makefile

%build

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -Iinclude" libglpng.so.1.45
%install
make install DESTDIR=$RPM_BUILD_ROOT%{_prefix} LIB=%{_lib}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libglpng-devel -f %{oreon_filedir}/libglpng-devel.list

%changelog

%autochangelog
