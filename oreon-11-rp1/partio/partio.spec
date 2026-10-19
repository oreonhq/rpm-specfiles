%global source0_hash e60a89364f2b5d9c9b1f143175fc1a5018027a59bb31af56e5df88806b506e49
%bcond          test 0
%global         soversion 1.20.0
Name:           partio
Version:        1.20.0
Release:        1%{?dist}
Summary:        Library for manipulating common animation particle
License:        BSD-3-Clause-Modification
URL:            https://github.com/wdas/%{name}
Source0:        https://github.com/wdas/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
C++ (with python bindings) library for easily reading/writing/manipulating 
common animation particle formats such as PDB, BGEO, PTC.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
%{summary}

%package        libs
Summary:        Core %{name} libraries
%description    libs
C++ (with python bindings) library for easily reading/writing/manipulating 
common animation particle formats such as PDB, BGEO, PTC.

%package -n python3-%{name}
Summary:        Library for manipulating common animation particle
BuildRequires:  pkgconfig(python3)
%description -n python3-%{name} 
The python3-%{name} contains Python 3 binning for the library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%build

%cmake \
 -DCMAKE_PREFIX_PATH=%{_prefix} \
 -DCXXFLAGS_STD=c++17
%cmake_build
%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_libdir}/python/site-packages/*.py
chmod +x %{buildroot}%{python3_sitearch}/*.py
rm -rf %{buildroot}%{_datadir}/%{name}/test
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  PYTHONPATH='%{buildroot}%{python3_sitearch}' \
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{?with_test:%ctest}
%files -f %{oreon_filedir}/main.list
%files -n partio-devel -f %{oreon_filedir}/partio-devel.list
%files -n partio-doc -f %{oreon_filedir}/partio-doc.list
%files -n partio-libs -f %{oreon_filedir}/partio-libs.list
%files -n python3-partio -f %{oreon_filedir}/python3-partio.list

%changelog

%autochangelog
