%global source0_hash none

Name:           jsonnet
Version:        0.21.0
Release:        6%{?dist}
Summary:        A data templating language based on JSON

# The entire source is Apache-2.0, except:
#   - doc/ (the HTML documentation) is doc/_layouts/base.html is CC-BY-2.5,
#     which is reflected in the License of the -doc subpackage
#   - The dependency “json” is a header-only library, so it must be treated as
#     a static library. Its license “MIT AND CC0-1.0” (the latter from a
#     bundled hedley) therefore contributes to the licenses of the binary RPMs
#     that include compiled programs and libraries.
License:        Apache-2.0 AND MIT AND CC0-1.0

URL:            https://github.com/google/jsonnet
%global srcversion %{gsub %{version} ~ -}
Source0:        %{url}/archive/refs/tags/v%{srcversion}.tar.gz

# Downstream man pages in groff_man(7) format
Source1:        jsonnet.1
Source2:        jsonnetfmt.1

# Upstream wants to build single source wheels
# these benefit from static linking,
# but we want to link to libjsonnet here so we are sharing the lib
Patch: 0001-Dynamic-link-to-libjsonnet-rather-than-static.patch
# Upstream hard codes compiler flags
Patch: 0002-patch-CMakeLists.txt-to-stop-overriding-build-flags.patch
# Upstream ships rapidyaml inside this source repo
Patch: 0003-Use-system-provided-rapidyaml.patch
# Fedora/CentOS10 doesn't have the latest setuptools
Patch: 0004-use-older-setuptools.patch
# Fix tag error where libc++ is tagged -rc2
Patch: 0005-fix-cpp-lib-version.patch
# Permit use of cmake4
# https://bugzilla.redhat.com/show_bug.cgi?id=2380666
Patch: 0006-Add-cmake4-to-cmake_minimum_required.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# safe to clean up "if" statements after 2026-05-31
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif

# Bundled MD5 C++ class in third_party/md5/ with very permissive license (RSA)
# Per current guidance, we don’t need to record this as an additional license:
# https://docs.fedoraproject.org/en-US/legal/misc/#_licensing_of_rsa_implementations_of_md5
# rpmlint must be notified of the unversioned provides
Provides:       bundled(md5-thilo)

BuildRequires:  python3-devel pyproject-rpm-macros
BuildRequires:  python3dist(wheel) python3dist(setuptools)

BuildRequires:  bash cmake gcc gcc-c++ gtest-devel make

# json is header only, so note the static lib for tracking
BuildRequires:  json-devel json-static
BuildRequires:  rapidyaml-devel

# Set our toplevel runtime requirements
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global _description %{expand:
A data templating language for app and tool developers based on JSON}

%description %{_description}

%package -n python3-%{name}
Summary:        %{name} Bindings for Python
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name} %{_description}

%package libs
Summary:        Shared Libraries for %{name}

%description libs %{_description}

%package devel
Summary:        Development Headers for %{name}
# This contains nothing derived from json-static, so the (MIT AND CC0-1.0)
# portion can be omitted and the license is simply:
License:        Apache-2.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}

%package doc
Summary:        Documentation for %{name}
# This contains nothing derived from json-static, so the (MIT AND CC0-1.0)
# portion can be omitted. HTML documentation from doc/ is CC-BY-2.5; examples/
# are Apache-2.0.
License:        Apache-2.0 AND CC-BY-2.5
BuildArch:      noarch

%description doc %{_description}

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

%generate_buildrequires
%pyproject_buildrequires

%build
# FIXME:
# For reasons I'm not following, json-devel isn't added to include by cmake
#
# explicitly set -fPIC so python can pick it up later on
export CXXFLAGS="%{optflags} -fPIC -I%{_includedir}/nlohmann"

# setup our build environment
%cmake -DBUILD_SHARED_BINARIES:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF -DUSE_SYSTEM_JSON:BOOL=ON -DUSE_SYSTEM_GTEST:BOOL=ON

# make tools and headers
%cmake_build

# make python binding
%{__cp} %{__cmake_builddir}/lib%{name}*.s* .
%pyproject_wheel

%install
%{cmake_install}

# install python binding
%pyproject_install
%pyproject_save_files _jsonnet

install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 '%{SOURCE1}' '%{SOURCE2}'

%check
%ctest

LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
    PYTHONPATH='%{buildroot}%{python3_sitearch}' \
    %{python3} python/_jsonnet_test.py

%files
%{_bindir}/jsonnet
%{_bindir}/jsonnetfmt
%{_mandir}/man1/jsonnet.1*
%{_mandir}/man1/jsonnetfmt.1*

%files libs
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}++.so.*

%files devel
%{_includedir}/lib%{name}*
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}++.so

%files -n python3-%{name} -f %{pyproject_files}

%files doc
%license LICENSE
%doc README.md
%doc CONTRIBUTING
%doc doc
%doc examples

%changelog
%autochangelog
