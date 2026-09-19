%global source0_hash 853b92723750ee2249d8f7aedb1e367a97fb3b9fe4b3741d67e8c1bee7cd97cb

#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
%if 0%{?suse_version}
%{?!python_module:%define python_module() python3-%{**}}
%else
%global python_files -n python3-tensile-devel
%define python_sitelib %python3_sitelib
%define python_subpackages %nil
%define python_alternative %nil
%endif

%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 de5c1aebb641af098d9310a9fcca5591a7c066c8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20251015
%endif

%global upstreamname Tensile
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%if 0%{?suse_version}
Name:           python-tensile-devel
%else
Name:           python-tensile
%endif
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        2%{?dist}
%else
Version:        %{rocm_version}
Release:        4%{?dist}
%endif
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs

License:        MIT
%if %{with gitcommit}
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/archive/%{commit0}/rocm-libraries-%{shortcommit0}.tar.gz
%else
URL:            https://github.com/ROCmSoftwarePlatform/Tensile
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%endif

Patch1:         0001-tensile-fedora-gpus.patch
Patch2:         0001-tensile-gfx1153.patch
Patch3:         0001-tensile-set-default-paths.patch
Patch4:         0001-tensile-ignore-cache-check.patch
Patch5:         0001-tensile-add-cmake-arches.patch
Patch6:         0001-tensile-gfx1036.patch

%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif

%if 0%{?suse_version}
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
Requires:       hipcc
Requires:       rocminfo
Requires:       %{python_module joblib}
Requires:       %{python_module msgpack}
Requires:       %{python_module PyYAML}
Requires:       %{python_module setuptools}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%endif

# Straight python, but only usable for ROCm which is only on x86_64
BuildArch:      noarch
ExclusiveArch:  x86_64
%python_subpackages

%description
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.

%if 0%{?fedora} || 0%{?rhel}
# There are headers and code as part of the code generation.
# This make rpm checkers unhappy
%package -n python3-tensile-devel
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs

Requires:       cmake-filesystem
Requires:       hipcc
Requires:       rocminfo
# Available on ferdora,EPEL 10+
%if 0%{?fedora} || 0%{?rhel} > 9
Requires:       python3dist(joblib)
%endif
Requires:       python3dist(msgpack)
Requires:       python3dist(pyyaml)
Provides:       python3-tensile

%description -n python3-tensile-devel
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd shared/tensile
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

#Fix a few things:
chmod 755 Tensile/Configs/miopen/convert_cfg.py
sed -i -e 's@bin/python@bin/python3@' Tensile/Configs/miopen/convert_cfg.py
sed -i -e 's@bin/python@bin/python3@' Tensile/Tests/create_tests.py
sed -i -e 's@bin/env python3@bin/python3@' Tensile/bin/Tensile
sed -i -e 's@bin/env python3@bin/python3@' Tensile/bin/TensileCreateLibrary

# I'm assuming we don't need these:
rm -r %{upstreamname}/Configs/miopen/archives

# hack where TensileGetPath is located
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g' Tensile/cmake/TensileConfig.cmake

# Use /usr instead of /opt/rocm for prefix
sed -i -e 's@opt/rocm@usr@g' Tensile/Common.py
sed -i -e 's@opt/rocm@usr@g' Tensile/Tests/yaml_only/test_config.py

# Ignora asm cap
sed -i -e 's@globalParameters["IgnoreAsmCapCache"] = False@globalParameters["IgnoreAsmCapCache"] = True@' Tensile/Common.py
sed -i -e 's@arguments["IgnoreAsmCapCache"] = args.IgnoreAsmCapCache@arguments["IgnoreAsmCapCache"] = True@' Tensile/TensileCreateLibrary.py
sed -i -e 's@if not ignoreCacheCheck and derivedAsmCaps@if False and derivedAsmCaps@' Tensile/Common.py

# Reduce requirements
sed -i -e '/joblib/d' requirements.*
sed -i -e '/rich/d' requirements.*
sed -i -e '/msgpack/d' requirements.*

%build
%if %{with gitcommit}
cd shared/tensile
%endif

%py3_build
%{?python_build: %python_build}

%install
%if %{with gitcommit}
cd shared/tensile
%endif

%py3_install
%{?python_install: %python_install}

mkdir -p %{buildroot}%{_datadir}/cmake/Tensile
mv %{buildroot}%{_prefix}/cmake/* %{buildroot}%{_datadir}/cmake/Tensile/
rm -rf %{buildroot}%{_prefix}/cmake

# Do not distribute broken bins
rm %{buildroot}%{_bindir}/tensile*

# Do not distribute tests
rm -rf %{buildroot}%{python3_sitelib}/%{upstreamname}/Tests

#Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{_prefix}
%endif

# rm hard links and replace
rm %{buildroot}%{python3_sitelib}/%{upstreamname}/cmake/*.cmake
mv %{buildroot}%{_datadir}/cmake/Tensile/*.cmake %{buildroot}%{python3_sitelib}/%{upstreamname}/cmake/

%if 0%{?suse_version}
%python_clone -a %{buildroot}%{_bindir}/Tensile
%python_clone -a %{buildroot}%{_bindir}/TensileBenchmarkCluster
%python_clone -a %{buildroot}%{_bindir}/TensileCreateLibrary
%python_clone -a %{buildroot}%{_bindir}/TensileGetPath
%python_clone -a %{buildroot}%{_bindir}/TensileRetuneLibrary

%post
%python_install_alternative Tensile
%python_install_alternative TensileBenchmarkCluster
%python_install_alternative TensileCreateLibrary
%python_install_alternative TensileGetPath
%python_install_alternative TensileRetuneLibrary

%postun
%python_uninstall_alternative Tensile
%python_uninstall_alternative TensileBenchmarkCluster
%python_uninstall_alternative TensileCreateLibrary
%python_uninstall_alternative TensileGetPath
%python_uninstall_alternative TensileRetuneLibrary
%endif

%files %{python_files}
%dir %{python_sitelib}/%{upstreamname}
%dir %{python_sitelib}/%{upstreamname}*.egg-info
%if %{with gitcommit}
%doc shared/tensile/README.md
%license shared/tensile/LICENSE.md
%else
%doc README.md
%license LICENSE.md
%endif
%python_alternative %{_bindir}/Tensile
%python_alternative %{_bindir}/TensileBenchmarkCluster
%python_alternative %{_bindir}/TensileCreateLibrary
%python_alternative %{_bindir}/TensileGetPath
%python_alternative %{_bindir}/TensileRetuneLibrary
%{python_sitelib}/%{upstreamname}/*
%{python_sitelib}/%{upstreamname}*.egg-info/*

%changelog
%autochangelog
