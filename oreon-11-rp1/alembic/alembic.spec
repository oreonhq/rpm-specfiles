%global source0_hash ab299bb4b1894a6675c73fa29940522b54c81a91b1d691ca3470d86b7345ffce

# Force out of source build
%undefine __cmake_in_source_build
#%%global prerelease _beta2
# TODO:
# Python Module

Name:           alembic
Version:        1.8.11
Release:        %autorelease
Summary:        Open framework for storing and sharing scene data
License:        BSD-3-Clause AND BSL-1.0
URL:            http://alembic.io/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}%{?prerelease}.tar.gz#/%{name}-%{version}%{?prerelease}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.13
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  cmake(Imath)
BuildRequires:  pkgconfig(zlib)

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

%files
%{_bindir}/abcconvert
%{_bindir}/abcdiff
%{_bindir}/abcecho
%{_bindir}/abcechobounds
%{_bindir}/abcls
%{_bindir}/abcstitcher
%{_bindir}/abctree

%files libs
%license LICENSE.txt
%doc ACKNOWLEDGEMENTS.txt FEEDBACK.txt NEWS.txt README.txt
%{_libdir}/libAlembic.so.*

%files devel
%{_includedir}/Alembic
%{_libdir}/cmake/Alembic
%{_libdir}/libAlembic.so

%changelog
%autochangelog
