%global source0_hash eea03f2e224b66813226d775053316675375dcec45bd263674c052d9324a49a5

Name:           ann
Version:        1.1.2
Release:        31%{?dist}
Summary:        Library for searching Approximate Nearest Neighbors

License:        LGPL-2.1-or-later
URL:            http://www.cs.umd.edu/~mount/ANN
Source0:        http://www.cs.umd.edu/~mount/ANN/Files/%{version}/%{name}_%{version}.tar.gz
Patch0:         ann-make.patch
Patch1:         ann-gcc43.patch
BuildRequires:  gcc-c++
BuildRequires:  make

%description
ANN is a library written in the C++ programming language to support both
exact and approximate nearest neighbor searching in spaces of various
dimensions.  It was implemented by David M. Mount of the University of
Maryland, and Sunil Arya of the Hong Kong University of Science and
Technology.  ANN (pronounced like the name ``Ann'') stands for
Approximate Nearest Neighbors.  ANN is also a testbed containing
programs and procedures for generating data sets, collecting and
analyzing statistics on the performance of nearest neighbor algorithms
and data structures, and visualizing the geometric structure of these
data structures.

%package libs
Summary:        Runtime files for the ANN library

%description libs
Runtime files needed to use ANN library.

%package devel
Summary:        Development files for the ANN library
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Development files needed to use ANN library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}_%{version} -p1

%build
%make_build linux CFLAGS="-fPIC -DPIC %{build_cxxflags}" LDFLAGS="%{build_ldflags} -L../lib"

%install
mkdir -p %{buildroot}%{_includedir}/ANN
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_bindir}

install -p -m 0644 include/ANN/*.h %{buildroot}%{_includedir}/ANN
install -p -m 0755 lib/libANN.so.* %{buildroot}%{_libdir}
install -p -m 0755 bin/ann2fig %{buildroot}%{_bindir}

pushd %{buildroot}%{_libdir}
ln -s libANN.so.1.0 libANN.so.1
ln -s libANN.so.1.0 libANN.so
popd

# create pkg-config file
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: Library for searching Approximate Nearest Neighbors
Version: %{version}
Requires:
Libs: -L\${libdir} -lANN
Cflags: -I\${includedir}
EOF

%files
%{_bindir}/*

%files libs
%doc Copyright.txt License.txt ReadMe.txt
%{_libdir}/*.so.*

%files devel
%doc doc/ANNmanual.pdf
%{_includedir}/ANN
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
