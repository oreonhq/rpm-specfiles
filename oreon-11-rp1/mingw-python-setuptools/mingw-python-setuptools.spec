%global source0_hash 8b0e9d10c784bf7d262c4e5ec5d4ec94127ce206e8738f29a437945fbc219b70

%{?mingw_package_header}

%global pypi_name setuptools

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       80.10.2
Release:       1%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:       %{pypi_source %{pypi_name} %{version}}

# Adapt is_mingw check to only check get_platform, as sys.platform will be 'linux' when cross-compiling
Patch0:        mingw-python-setuptools_is_mingw.patch
# Don't append -s to linker commandline
Patch1:        mingw-python-setuptools_nostrip.patch
# Don't override shared_lib_extension with SHLIB_SUFFIX config value
# The value set by Mingw32CCompiler class is already correct, no need to override
Patch2:        mingw-python-setuptools-shlib-suffix.patch

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-python3

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-python3

%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled exes
rm -f setuptools/*.exe

# Strip shebangs on python modules
find setuptools -name \*.py | xargs sed -i -e '1 {/^#!\//d}'

%build
%{mingw32_py3_build_host}
%{mingw64_py3_build_host}
%{mingw32_py3_build}
%{mingw64_py3_build}

%install
%{mingw32_py3_install_host}
%{mingw64_py3_install_host}
%{mingw32_py3_install}
%{mingw64_py3_install}

find %{buildroot}%{mingw32_python3_sitearch}/ -name '*.exe' | xargs rm -f
find %{buildroot}%{mingw64_python3_sitearch}/ -name '*.exe' | xargs rm -f

%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/%{pypi_name}/
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/pkg_resources/
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/_distutils_hack/
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/distutils-precedence.pth
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/pkg_resources/
%{mingw32_python3_sitearch}/_distutils_hack/
%{mingw32_python3_sitearch}/distutils-precedence.pth
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{_prefix}/%{mingw64_target}/lib/python%{mingw64_python3_version}/site-packages/%{pypi_name}/
%{_prefix}/%{mingw64_target}/lib/python%{mingw64_python3_version}/site-packages/pkg_resources/
%{_prefix}/%{mingw64_target}/lib/python%{mingw64_python3_version}/site-packages/_distutils_hack/
%{_prefix}/%{mingw64_target}/lib/python%{mingw64_python3_version}/site-packages/distutils-precedence.pth
%{_prefix}/%{mingw64_target}/lib/python%{mingw64_python3_version}/site-packages/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/pkg_resources/
%{mingw64_python3_sitearch}/_distutils_hack/
%{mingw64_python3_sitearch}/distutils-precedence.pth
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/

%changelog
%autochangelog
