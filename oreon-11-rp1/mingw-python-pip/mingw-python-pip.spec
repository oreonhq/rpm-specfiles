%global source0_hash 8d0538dbbd7babbd207f261ed969c65de439f6bc9e5dbd3b3b9a77f25d95f343

%{?mingw_package_header}

%global pypi_name pip

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       25.3
Release:       2%{?dist}
BuildArch:     noarch

# We bundle a lot of libraries with pip, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:

# appdirs: MIT
# certifi: MPL-2.0
# chardet: LGPL-2.1-only
# colorama: BSD-3-Clause
# CacheControl: Apache-2.0
# distlib: Python-2.0.1
# distro: Apache-2.0
# html5lib: MIT
# idna: BSD-3-Clause
# ipaddress: Python-2.0.1
# msgpack: Apache-2.0
# packaging: Apache-2.0 OR BSD-2-Clause
# progress: ISC
# pygments: BSD-2-Clause
# pyparsing: MIT
# pyproject-hooks: MIT
# requests: Apache-2.0
# resolvelib: ISC
# rich: MIT
# setuptools: MIT
# six: MIT
# tenacity: Apache-2.0
# truststore: MIT
# tomli: MIT
# typing-extensions: Python-2.0.1
# urllib3: MIT
# webencodings: BSD-3-Clause
License:       MIT AND Python-2.0.1 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-2.1-only AND MPL-2.0 AND (Apache-2.0 OR BSD-2-Clause)
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-flit-core

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-flit-core

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

# Copy vendor licenses for %%license
mkdir vendor_licenses
destdir=$PWD/vendor_licenses
(cd src/pip/_vendor && find  -name 'LICENSE*' -exec install -Dp {} $destdir/{} \;)

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

# Strip shebangs from non-executable scripts
sed -i '1d' %{buildroot}%{mingw32_python3_sitearch}/pip/_vendor/distro/distro.py
sed -i '1d' %{buildroot}%{mingw64_python3_sitearch}/pip/_vendor/distro/distro.py
sed -i '1d' %{buildroot}%{mingw32_python3_sitearch}/pip/_vendor/requests/certs.py
sed -i '1d' %{buildroot}%{mingw64_python3_sitearch}/pip/_vendor/requests/certs.py

%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%license vendor_licenses
%if %{without bootstrap}
%{mingw32_bindir}/pip
%{mingw32_bindir}/pip3
%endif
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%license vendor_licenses
%if %{without bootstrap}
%{mingw64_bindir}/pip
%{mingw64_bindir}/pip3
%endif
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
