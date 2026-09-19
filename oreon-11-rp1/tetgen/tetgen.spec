%global source0_hash 4d114861d5ef2063afd06ef38885ec46822e90e7b4ea38c864f76493451f9cf3

Name:           tetgen
Version:        1.5.0
Release:        31%{?dist}
Summary:        A Quality Tetrahedral Mesh Generator

License:        AGPL-3.0-or-later
URL:            http://wias-berlin.de/software/tetgen/
Source0:        http://www.tetgen.org/1.5/src/%{name}%{version}.tar.gz
Source1:        http://www.tetgen.org/1.5/doc/manual/manual.pdf
# - Raise minimum cmake version
# - Use GNUInstallDirs
# - Fix cmake file to build a shared library and support installation
# - Don't compile the entire code twice, once for the library and once for the
#   executable, but link the executable against the library instead
# - Split off main function to separate file
Patch0:         tetgen_build.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
TetGen is a program to generate tetrahedral meshes of any 3D polyhedral
domains.
TetGen generates exact constrained Delaunay tetrahedralizations, boundary
conforming Delaunay meshes, and Voronoi partitions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Manual for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the %{name} manual.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n%{name}%{version}
cp -a %{SOURCE1} .

# Fix line endings
sed -i 's|\r||g' example.poly

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/libtet.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libtet.so

%files doc
%doc example.poly manual.pdf
%license LICENSE

%changelog
%autochangelog
