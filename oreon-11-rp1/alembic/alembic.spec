%global source0_hash b6d916c40446e8c502c84273092ab3d98f3f7f6094f8a2b8203d23e2f1d2a4a0
%undefine __cmake_in_source_build
Name:           alembic
Version:        1.8.12
Release:        1%{?dist}
Summary:        Open framework for storing and sharing scene data
License:        BSD-3-Clause AND BSL-1.0
URL:            http://alembic.io/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(Imath)
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Alembic is an open computer graphics interchange framework. Alembic distills
complex, animated scenes into a non-procedural, application-independent set of
baked geometric results. This 'distillation' of scenes into baked geometry is
exactly analogous to the distillation of lighting and rendering scenes into
rendered image data.

%package        libs
Summary:        Core Alembic libraries
%description    libs
Alembic is an open computer graphics interchange framework. Alembic distills
complex, animated scenes into a non-procedural, application-independent set of
baked geometric results. This 'distillation' of scenes into baked geometry is
exactly analogous to the distillation of lighting and rendering scenes into
rendered image data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake%{?_isa}
Requires:       imath-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?prerelease}

sed -i -e 's/ConfigPackageLocation lib/ConfigPackageLocation %{_lib}/g' \
    lib/Alembic/CMakeLists.txt

iconv -f iso8859-1 -t utf-8 ACKNOWLEDGEMENTS.txt > ACKNOWLEDGEMENTS.txt.conv && \
    mv -f ACKNOWLEDGEMENTS.txt.conv ACKNOWLEDGEMENTS.txt

%build

export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake %{?_cmake_skip_rpath} \
    -DALEMBIC_LIB_INSTALL_DIR=%{_libdir} \
    -DALEMBIC_SHARED_LIBS=ON \
    -DUSE_BINARIES=ON \
    -DUSE_HDF5=ON \
    -DUSE_EXAMPLES=ON \
    -DUSE_PYALEMBIC=OFF \
    -DUSE_STATIC_BOOST=OFF \
    -DUSE_STATIC_HDF5=OFF \
    -DUSE_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles alembic-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles alembic-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n alembic-libs -f %{oreon_filedir}/alembic-libs.list
%files -n alembic-devel -f %{oreon_filedir}/alembic-devel.list

%changelog

%autochangelog
