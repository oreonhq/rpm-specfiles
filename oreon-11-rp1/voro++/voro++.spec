%global source0_hash ef7970071ee2ce3800daa8723649ca069dc4c71cc25f0f7d22552387f3ea437e

%global _vpath_srcdir src
%undefine __cmake_in_source_dir

Name:           voro++
Version:        0.4.6
Release:        33%{?dist}
Summary:        Library for 3D computations of the Voronoi tessellation

License:        BSD-3-Clause-LBNL
URL:            http://math.lbl.gov/voro++/
Source0:        http://math.lbl.gov/voro++/download/dir/%{name}-%{version}.tar.gz
Source1:        CMakeLists.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

# Make base class destructors virtual
Patch0:         voro++_virtual-destructor.patch
# Fix manpage formatting
Patch1:         voro++_man.patch

%description
Voro++ is a software library for carrying out three-dimensional computations
of the Voronoi tessellation. A distinguishing feature of the Voro++ library
is that it carries out cell-based calculations, computing the Voronoi cell for
each particle individually. It is particularly well-suited for applications
that rely on cell-based statistics, where features of Voronoi cells (e.g.
volume, centroid, number of faces) can be used to analyze a system of particles.

%package devel
Summary:        %{name} headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for %{name}.

%package doc
Summary:        %{name} documentation
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

cp -a %{SOURCE1} src

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dpm 0644 man/voro++.1 %{buildroot}%{_mandir}/man1/voro++.1

# Fix path in examples
find examples -name "*.cc" -exec sed -i 's/"voro++.hh"/<voro++\/voro++.hh>/g' '{}' \;
cp config.mk examples/
find examples -name "Makefile" -exec sed -i 's/..\/..\/config.mk/..\/config.mk/g' '{}' \;

%ldconfig_scriptlets

%files
%doc LICENSE README NEWS
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%files doc
%doc LICENSE
%doc html/
%doc examples/
%doc scripts/

%changelog
%autochangelog
