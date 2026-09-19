%global source0_hash e60a89364f2b5d9c9b1f143175fc1a5018027a59bb31af56e5df88806b506e49

%bcond          test 0
%global         soversion 1.20.0

Name:           partio
Version:        1.20.0
Release:        %autorelease
Summary:        Library for manipulating common animation particle

License:        BSD-3-Clause-Modification
URL:            https://github.com/wdas/%{name}
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(zlib)
#BuildRequires:  swig

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
Summary:        %{summary}
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

#Remove files from unversioned python directory
rm -f %{buildroot}%{_libdir}/python/site-packages/*.py

chmod +x %{buildroot}%{python3_sitearch}/*.py

#Remove all tests containing arch-dependant binaries
rm -rf %{buildroot}%{_datadir}/%{name}/test

# Generate and install man pages
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

%check
%{?with_test:%ctest}

%files
%license LICENSE
%doc README.md
%{_bindir}/part{attr,convert,edit,info,inspect,json,view}
%{_mandir}/man1/part{attr,convert,edit,info,inspect,json,view}.1*

%files devel
%{_includedir}/Partio{,Attribute,Iterator,Vec3}.h
%{_libdir}/lib%{name}.so

%files doc
%doc %{_defaultdocdir}/%{name}/html

%files libs
%license LICENSE
%{_libdir}/lib%{name}.so.{1,%{soversion}}

%files -n python3-%{name}
%pycached %{python3_sitearch}/*.py

%changelog
%autochangelog
