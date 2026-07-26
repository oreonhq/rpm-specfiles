%global source0_hash aa20997dc001180b8c12d7000edf4941c757fb0e8c9fcf21dcdde52cd33c5506

%undefine __cmake_in_source_build

%{?!mono_arches: %global mono_arches %{ix86} x86_64 sparc sparcv9 ia64 %{arm} alpha s390x ppc ppc64}

%ifarch %{mono_arches}
# No linux system is actually using the csharp bindings
%global with_csharp 0
%endif
%global with_java 1
%if 0%{?fedora} >= 41
%ifarch %{ix86}
%global with_php 0
%else
%global with_php 1
%endif
%else
%global with_php 1
%endif
%global with_python 1

%if 0%{?with_php} > 0
%global ini_name     40-kolabformat.ini
%endif

# Filter out private python and php libs. Does not work on EPEL5,
# therefor we use it conditionally
%if 0%{?with_php} > 0
%if 0%{?with_python} > 0
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_provides_in %{php_extdir}/.*\.so$
%filter_setup
}
%else
%{?filter_setup:
%filter_provides_in %{php_extdir}/.*\.so$
%filter_setup
}
%endif
%else
%if 0%{?with_python} > 0
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}
%endif
%endif

Name:           libkolabxml
Version:        1.2.0
Release:        38%{?dist}
Summary:        Kolab XML format collection parser library

License:        LGPL-3.0-or-later
URL:            http://www.kolab.org

Source0:        https://cgit.kolab.org/libkolabxml/snapshot/libkolabxml-%{version}.tar.gz
Patch0:         libkolabxml-1.2.0-fix-for-swig4.patch

BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.6
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  swig
BuildRequires:  uuid-devel
BuildRequires:  xerces-c-devel
BuildRequires:  xsd

# libkolab FTBFS, so ...
# https://bugzilla.redhat.com/show_bug.cgi?id=1518800
%global libkolab_obsoletes 1.0.2-20
%if 0%{?libkolab_obsoletes:1}
Obsoletes: libkolab < %{libkolab_obsoletes}
Obsoletes: libkolab-devel < %{libkolab_obsoletes}
Obsoletes: python2-libkolab < %{libkolab_obsoletes}
%endif

%if 0%{?with_csharp} < 1
Obsoletes:      csharp-kolabformat < %{version}-%{release}
#Provides:       csharp-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_java} < 1
Obsoletes:      java-kolabformat < %{version}-%{release}
#Provides:       java-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_php} < 1
Obsoletes:      php-kolabformat < %{version}-%{release}
#Provides:       php-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_python} < 1
Obsoletes:      python-kolabformat < %{version}-%{release}
Obsoletes:      python2-kolabformat < %{version}-%{release}
%endif

%description
The libkolabxml parsing library interprets Kolab XML formats (xCal, xCard)
with bindings for Python, PHP and other languages. The language bindings
are available through sub-packages.

%package devel
Summary:        Kolab XML library development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       libcurl-devel
Requires:       xerces-c-devel
Requires:       cmake
%description devel
Development headers for the Kolab XML libraries.

%if 0%{?with_csharp} > 0
%package -n csharp-kolabformat
Summary:        C# Bindings for libkolabxml
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  mono-core
%description -n csharp-kolabformat
C# bindings for libkolabxml
%endif

%if 0%{?with_java} > 0
%package -n java-kolabformat
Summary:        Java Bindings for libkolabxml
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n java-kolabformat
Java bindings for libkolabxml
%endif

%if 0%{?with_php} > 0
%package -n php-kolabformat
Summary:        PHP bindings for libkolabxml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
BuildRequires:  php >= 5.3
BuildRequires:  php-devel >= 5.3
%description -n php-kolabformat
The PHP kolabformat package offers a comprehensible PHP library using the
bindings provided through libkolabxml.
%endif

%if 0%{?with_python} > 0
%package -n python3-kolabformat
Summary:        Python bindings for libkolabxml
Obsoletes:      python-kolabformat < 1.1.4
Provides:       python-kolabformat = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
%description -n python3-kolabformat
The PyKolab format package offers a comprehensive Python library using the
bindings provided through libkolabxml.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i "s/-php/-php7/g" src/php/CMakeLists.txt

%build
# TODO: Please submit an issue to upstream (rhbz#2380728)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
    -DBUILD_TESTS:BOOL=OFF \
%if 0%{?with_csharp} > 0
    -DCSHARP_BINDINGS=ON \
    -DCSHARP_INSTALL_DIR=%{_datadir}/%{name}/csharp/ \
%endif
%if 0%{?with_java} > 0
    -DJAVA_BINDINGS=ON \
    -DJAVA_INSTALL_DIR=%{_datadir}/%{name}/java/ \
%endif
%if 0%{?with_php} > 0
    -DPHP_BINDINGS=ON \
    -DPHP_INSTALL_DIR=%{php_extdir} \
%endif
%if 0%{?with_python} > 0
    -DPYTHON_BINDINGS=ON \
    -DPYTHON_INSTALL_DIR=%{python3_sitearch}
%endif

%cmake_build

%install
%cmake_install

%if 0%{?with_php} > 0
mkdir -p \
    %{buildroot}/%{_datadir}/php \
    %{buildroot}/%{php_inidir}/
cat > %{buildroot}/%{php_inidir}/%{ini_name} << EOF
extension=kolabformat.so
EOF
%endif

%check
pushd %{_vpath_builddir}
export LD_LIBRARY_PATH=$( pwd )/src/
%if 0%{?with_php} > 0
php -d enable_dl=On -dextension=src/php/kolabformat.so src/php/test.php ||:
%endif
%if 0%{?with_python} > 0
python3 src/python/test.py ||:
%endif
popd

%ldconfig_scriptlets

%files
%doc DEVELOPMENT NEWS README
%license COPYING*
%{_libdir}/libkolabxml.so.1*

%files devel
%{_includedir}/kolabxml/
%{_libdir}/libkolabxml.so
%{_libdir}/cmake/Libkolabxml/

%if 0%{?with_csharp} > 0
%files -n csharp-kolabformat
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/csharp
%endif

%if 0%{?with_java} > 0
%files -n java-kolabformat
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/java
%endif

%if 0%{?with_php} > 0
%files -n php-kolabformat
%{php_extdir}/kolabformat.so
%config(noreplace) %{php_inidir}/%{ini_name}
%endif

%if 0%{?with_python} > 0
%files -n python3-kolabformat
%{python3_sitearch}/kolabformat.py
%{python3_sitearch}/_kolabformat.so
%{python3_sitearch}/__pycache__/*
%endif

%changelog
%autochangelog
