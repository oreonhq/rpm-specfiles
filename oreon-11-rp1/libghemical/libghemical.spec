%global source0_hash db8c3add0aa1f94c21016d60fa3f66fb194e56b8e9fceaa3860c603700efc3ac

Name:           libghemical
Summary:        Libraries for the Ghemical chemistry package
Version:        3.0.0
Release:        30%{?dist}

# SPDX confirmed
License:        GPL-2.0-or-later
URL:            http://www.bioinformatics.org/ghemical/ghemical/index.html
Source0:        http://www.bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz

BuildRequires:  flexiblas-devel
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  libint-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mpqc-devel
BuildRequires:  mopac7-devel

# Libint releases can have API breakages, leading to segfaults.
Requires:       libint(api)%{?_isa} = %{_libint_apiversion}

%description
Data files and dynamic libraries for the Ghemical chemistry package.
These libraries implement the quantum-mechanics and molecular
mechanics models used to compute molecular properties.

%package devel
Summary:    Header files and static libraries from %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Libraries and header include files for developing programs based on %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

sed -i 's/blas/flexiblas/g' configure.ac
sed -i 's/lapack/flexiblas/g' configure.ac

%build
# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
autoreconf -ivf

%configure --enable-mopac7 --enable-mpqc --disable-static --disable-sctest
%make_build

sed -ir -e 's/^Libs:.*/Libs: -L${libdir} -lghemical/g' libghemical.pc

%install
%make_install

find %{buildroot}%{_libdir} -name *.la -exec rm -rf {} \;

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_datadir}/%{name}/
%{_libdir}/libghemical.so.5.0.1
%{_libdir}/libghemical.so.5

%files devel
%{_includedir}/ghemical/
%{_libdir}/libghemical.so
%{_libdir}/pkgconfig/libghemical.pc

%changelog
%autochangelog
