%global source0_hash 5914b9904d97efa662d919519cef1a14e4132bfddddaeed8b061b4a8af628f8d
Name:           jsonnet
Version:        0.22.0
Release:        1%{?dist}
Summary:        A data templating language based on JSON
License:        Apache-2.0 AND MIT AND CC0-1.0
URL:            https://github.com/google/jsonnet
%global srcversion %{gsub %{version} ~ -}
Source0:        https://github.com/google/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        jsonnet.1
Source2:        jsonnetfmt.1
Patch: 0001-Dynamic-link-to-libjsonnet-rather-than-static.patch
Patch: 0002-patch-CMakeLists.txt-to-stop-overriding-build-flags.patch
Patch: 0003-Use-system-provided-rapidyaml.patch
Patch: 0004-use-older-setuptools.patch
Patch: 0005-fix-cpp-lib-version.patch
Patch: 0006-Add-cmake4-to-cmake_minimum_required.patch
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif
Provides:       bundled(md5-thilo)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 72.2
Requires:       python3-jsonnet = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{name}
Summary:        %{name} Bindings for Python
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description -n python3-%{name}

%package libs
Summary:        Shared Libraries for %{name}
%description libs

%package devel
Summary:        Development Headers for %{name}
License:        Apache-2.0
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel

%package doc
Summary:        Documentation for %{name}
License:        Apache-2.0 AND CC-BY-2.5
BuildArch:      noarch
%description doc

%prep

%autosetup -n %{name}-%{srcversion} -p1

# use system json lib instead
rm -rfv third_party/json/*

# don't bundel rapidyaml
rm -rfv third_party/rapidyaml/*

# don't bundle thirdparty doc resources
# this leaves the doc "unbuilt" but still sorta useful
rm -rf doc/third_party
rm -rf doc/.gitignore

# The documentation and examples include a few executable shell scripts.
# Because this is an unusual location to install scripts, we need to fix their
# shebangs manually. See:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_shebang_lines
find doc examples -type f -perm /0111 -name '*.sh' -print0 |
  xargs -r -0 -t sed -r -i '1{s@^#!/usr/bin/env[[:blank:]]+bash@#!/bin/bash@}'

%build

export CXXFLAGS="%{optflags} -fPIC -I%{_includedir}/nlohmann"
%cmake -DBUILD_SHARED_BINARIES:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF -DUSE_SYSTEM_JSON:BOOL=ON -DUSE_SYSTEM_GTEST:BOOL=ON
%cmake_build
%{__cp} %{__cmake_builddir}/lib%{name}*.s* .
%pyproject_wheel
%install
%{cmake_install}
%pyproject_install
install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 '%{SOURCE1}' '%{SOURCE2}'
%oreon_autofiles main usr/lib/python3*/site-packages/jsonnet* usr/lib64/python3*/site-packages/jsonnet* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
    PYTHONPATH='%{buildroot}%{python3_sitearch}' \
    %{python3} python/_jsonnet_test.py
%files
%files -n python3-jsonnet -f %{oreon_filedir}/python3-jsonnet.list
%files -n jsonnet-libs -f %{oreon_filedir}/jsonnet-libs.list
%files -n jsonnet-devel -f %{oreon_filedir}/jsonnet-devel.list
%files -n jsonnet-doc -f %{oreon_filedir}/jsonnet-doc.list

%changelog

%autochangelog
