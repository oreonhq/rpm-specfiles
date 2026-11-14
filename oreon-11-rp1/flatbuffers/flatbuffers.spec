# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f81c3162b1046fe8b84b9a0dbdd383e24fdbcf88583b9cb6028f90d04d90696a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond cpp_tests 1
# grpc is not in the tree
%bcond cpp_grpc_test 0
# numpy is not in the tree
%bcond python 0
%bcond py_tests %{with python}

Name:           flatbuffers
Version:        25.12.19
# so version follows the project version, see
# https://github.com/google/flatbuffers/issues/7759
%global so_version 25.12.19
Release:        1%{?dist}
Summary:        Memory efficient serialization library

License:        Apache-2.0
URL:            https://google.github.io/flatbuffers
%global forgeurl https://github.com/google/flatbuffers
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        flatc.1

ExcludeArch:    %{ix86}

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  cmake
%if %{with cpp_tests} && %{with cpp_grpc_test}
BuildRequires:  cmake(absl)
BuildRequires:  cmake(protobuf)
BuildRequires:  grpc-devel
%endif
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy)
%endif

Provides:       bundled(grpc) = 1.49.0

%global common_description %{expand:
FlatBuffers is a cross platform serialization library architected for maximum
memory efficiency. It allows you to directly access serialized data without
parsing/unpacking it first, while still having great forwards/backwards
compatibility.}

%description %{common_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains libraries and header files for developing applications
that use FlatBuffers.

%package        compiler
Summary:        FlatBuffers compiler (flatc)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    compiler %{common_description}

This package contains flatc, the FlatBuffers compiler.

%package        doc
Summary:        Documentation and examples for FlatBuffers

BuildArch:      noarch

%description    doc %{common_description}

This package contains documentation and examples for FlatBuffers.

%if %{with python}
%package -n     python3-flatbuffers
Summary:        FlatBuffers serialization format for Python

BuildArch:      noarch

Recommends:     python3dist(numpy)

Provides:       flatbuffers-python3 = %{version}-%{release}
Obsoletes:      flatbuffers-python3 < 2.0.0-6

%description -n python3-flatbuffers %{common_description}

This package contains the Python runtime library for use with the Flatbuffers
serialization format.
%endif

%prep
%oreon_sha256

%autosetup -p1
rm --recursive --verbose android/ kotlin/
%if %{with python}
%py3_shebang_fix samples
sed --regexp-extended --in-place=.upstream \
    --expression='s|[^[:blank:]]*(/flatc)|%{buildroot}%{_bindir}\1|' \
    --expression='s| python3 | %{python3} |' \
    --expression='s|run_tests [^/]|# &|' \
    --expression='s|PYTHONPATH=|&%{buildroot}%{python3_sitelib}:|' \
    --expression='s|which coverage|/bin/false|' \
    tests/PythonTest.sh
%endif

%if %{with python}
%generate_buildrequires
%pyproject_buildrequires --directory python
%endif

%conf
export VERSION='%{version}'
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DFLATBUFFERS_BUILD_TESTS:BOOL=%{?with_cpp_tests:ON}%{!?with_cpp_tests:OFF} \
%if %{with cpp_tests} && %{with cpp_grpc_test}
    -DFLATBUFFERS_BUILD_GRPCTEST:BOOL=ON \
    -DGRPC_INSTALL_PATH:PATH=%{_prefix} \
%else
    -DFLATBUFFERS_BUILD_GRPCTEST:BOOL=OFF \
%endif
    -DFLATBUFFERS_BUILD_SHAREDLIB=ON \
    -DFLATBUFFERS_BUILD_FLATLIB=OFF \
    -DFLATBUFFERS_BUILD_FLATC=ON

%build
%cmake_build
%if %{with python}
%pyproject_wheel --directory python
%endif

%install
%cmake_install
%if %{with python}
%pyproject_install
%pyproject_save_files --no-assert-license flatbuffers
%endif
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' '%{SOURCE1}'

%check
%if %{with cpp_tests}
%ctest
%endif
%if %{with py_tests}
%{py3_test_envvars} ./tests/PythonTest.sh
%endif
%if %{with python}
%pyproject_check_import
%endif

%files
%license LICENSE
%{_libdir}/libflatbuffers.so.%{so_version}

%files devel
%{_includedir}/flatbuffers/
%{_libdir}/libflatbuffers.so
%{_libdir}/cmake/flatbuffers/
%{_libdir}/pkgconfig/flatbuffers.pc

%files compiler
%{_bindir}/flatc
%{_mandir}/man1/flatc.1*

%files doc
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc examples/
%doc samples/

%if %{with python}
%files -n python3-flatbuffers -f %{pyproject_files}
%license LICENSE
%endif

%changelog
%autochangelog
