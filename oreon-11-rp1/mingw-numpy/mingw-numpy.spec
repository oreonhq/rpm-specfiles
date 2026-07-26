%global source0_hash none

%{?mingw_package_header}

# Disable debugsource packages
%undefine _debugsource_packages

%global pypi_name numpy

Name:          mingw-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2.4.2
Release:       1%{?dist}

# Everything is BSD except for class SafeEval in numpy/lib/utils.py which is Python
License:       BSD-3-Clause AND Apache-2.0
URL:           http://www.numpy.org/
Source0:       %{pypi_source}

# Make longdouble_format settable as option, as it cannot be determined when crosscompiling
Patch0:        mingw-numpy-longdoubleformat.patch
# Mingw does not have endian.h
Patch1:        mingw-numpy-endian.patch
# Fix FTBFS with GCC 16
# Sent upstream:
# https://github.com/numpy/x86-simd-sort/pull/225
Patch2:          fix-gcc-16-ftbfs.patch

BuildRequires: gcc-c++
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools
BuildRequires: mingw32-python3-Cython

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools
BuildRequires: mingw64-python3-Cython

%description
%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
(
mkdir build_win32
cd build_win32
%mingw32_python3 ../vendored-meson/meson/meson.py setup \
        --cross-file /usr/share/mingw/toolchain-mingw32.meson \
        --default-library shared \
        --prefix %{mingw32_prefix} \
        --bindir %{mingw32_bindir} \
        --sbindir %{mingw32_sbindir} \
        --sysconfdir %{mingw32_sysconfdir} \
        --datadir %{mingw32_datadir} \
        --includedir %{mingw32_includedir} \
        --libdir %{mingw32_libdir} \
        --libexecdir %{mingw32_libexecdir} \
        --localstatedir %{mingw32_localstatedir} \
        --sharedstatedir %{mingw32_sharedstatedir} \
        --mandir %{mingw32_mandir} \
        --infodir %{mingw32_infodir} \
        -Dlongdouble_format=INTEL_EXTENDED_12_BYTES_LE \
        ..

%mingw32_python3 ../vendored-meson/meson/meson.py compile
)
(
mkdir build_win32_host
cd build_win32_host
%mingw32_python3_host ../vendored-meson/meson/meson.py setup \
        --default-library shared \
        --prefix %{_prefix}/%{mingw32_target} \
        --bindir %{_prefix}/%{mingw32_target}/bin \
        --sbindir %{_prefix}/%{mingw32_target}/sbin \
        --sysconfdir %{_prefix}/%{mingw32_target}/etc \
        --datadir %{_prefix}/%{mingw32_target}/share \
        --includedir %{_prefix}/%{mingw32_target}/include \
        --libdir %{_prefix}/%{mingw32_target}/lib \
        --libexecdir %{_prefix}/%{mingw32_target}/libexec \
        --localstatedir %{_prefix}/%{mingw32_target}/var \
        --sharedstatedir %{_prefix}/%{mingw32_target}/var/lib \
        --mandir %{_prefix}/%{mingw32_target}/share/man \
        --infodir %{_prefix}/%{mingw32_target}/share/info \
        -Dlongdouble_format=UNKNOWN \
        ..

%mingw32_python3_host ../vendored-meson/meson/meson.py compile
)

(
mkdir build_win64
cd build_win64
%mingw64_python3 ../vendored-meson/meson/meson.py setup \
        --cross-file /usr/share/mingw/toolchain-mingw64.meson \
        --default-library shared \
        --prefix %{mingw64_prefix} \
        --bindir %{mingw64_bindir} \
        --sbindir %{mingw64_sbindir} \
        --sysconfdir %{mingw64_sysconfdir} \
        --datadir %{mingw64_datadir} \
        --includedir %{mingw64_includedir} \
        --libdir %{mingw64_libdir} \
        --libexecdir %{mingw64_libexecdir} \
        --localstatedir %{mingw64_localstatedir} \
        --sharedstatedir %{mingw64_sharedstatedir} \
        --mandir %{mingw64_mandir} \
        --infodir %{mingw64_infodir} \
        -Dlongdouble_format=INTEL_EXTENDED_16_BYTES_LE \
        ..

%mingw64_python3 ../vendored-meson/meson/meson.py compile
)
(
mkdir build_win64_host
cd build_win64_host
%mingw64_python3_host ../vendored-meson/meson/meson.py setup \
        --default-library shared \
        --prefix %{_prefix}/%{mingw64_target} \
        --bindir %{_prefix}/%{mingw64_target}/bin \
        --sbindir %{_prefix}/%{mingw64_target}/sbin \
        --sysconfdir %{_prefix}/%{mingw64_target}/etc \
        --datadir %{_prefix}/%{mingw64_target}/share \
        --includedir %{_prefix}/%{mingw64_target}/include \
        --libdir %{_prefix}/%{mingw64_target}/lib \
        --libexecdir %{_prefix}/%{mingw64_target}/libexec \
        --localstatedir %{_prefix}/%{mingw64_target}/var \
        --sharedstatedir %{_prefix}/%{mingw64_target}/var/lib \
        --mandir %{_prefix}/%{mingw64_target}/share/man \
        --infodir %{_prefix}/%{mingw64_target}/share/info \
        -Dlongdouble_format=UNKNOWN \
        ..

%mingw64_python3_host ../vendored-meson/meson/meson.py compile
)

# Manually generate dist-info as invoking the the venored meson directly does not do this
cat > setup.cfg <<EOF
[metadata]
name = %{pypi_name}
version = %{version}

[options]
py_modules = %{pypi_name}
EOF
%{mingw32_python3} -c "import setuptools.build_meta; print(setuptools.build_meta.prepare_metadata_for_build_wheel('.'))"

%install
(
cd build_win32
%mingw32_python3 ../vendored-meson/meson/meson.py install --destdir=%{buildroot}
)
(
cd build_win32_host
%mingw32_python3_host ../vendored-meson/meson/meson.py install --destdir=%{buildroot}
)
(
cd build_win64
%mingw64_python3 ../vendored-meson/meson/meson.py install --destdir=%{buildroot}
)
(
cd build_win64_host
%mingw64_python3_host ../vendored-meson/meson/meson.py install --destdir=%{buildroot}
)

# Install dist-info
cp -a %{pypi_name}-%{version}.dist-info %{buildroot}%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info
cp -a %{pypi_name}-%{version}.dist-info %{buildroot}%{mingw32_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info
cp -a %{pypi_name}-%{version}.dist-info %{buildroot}%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info
cp -a %{pypi_name}-%{version}.dist-info %{buildroot}%{mingw64_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info

# Symlink includedir
mkdir -p %{buildroot}%{_prefix}/%{mingw32_target}/include
mkdir -p %{buildroot}%{_prefix}/%{mingw64_target}/include
ln -s %{mingw32_python3_sitearch}/numpy/_core/include/numpy/ %{buildroot}%{_prefix}/%{mingw32_target}/include/numpy
ln -s %{mingw64_python3_sitearch}/numpy/_core/include/numpy/ %{buildroot}%{_prefix}/%{mingw64_target}/include/numpy

mkdir -p %{buildroot}%{mingw32_includedir}
mkdir -p %{buildroot}%{mingw64_includedir}
ln -s %{mingw32_python3_sitearch}/numpy/_core/include/numpy/ %{buildroot}%{mingw32_includedir}/numpy
ln -s %{mingw64_python3_sitearch}/numpy/_core/include/numpy/ %{buildroot}%{mingw64_includedir}/numpy

%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%{mingw32_includedir}/%{pypi_name}
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info

%dir %{_prefix}/%{mingw32_target}/include/
%{_prefix}/%{mingw32_target}/include/%{pypi_name}
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%{mingw64_includedir}/%{pypi_name}
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info

%dir %{_prefix}/%{mingw64_target}/include/
%{_prefix}/%{mingw64_target}/include/%{pypi_name}
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info

%changelog
%autochangelog
