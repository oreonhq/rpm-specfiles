%global source0_hash 816c96e8e8f193b40151dad7e8ff37b1221d019dbcb9c35cd3fadbfe6477dfec
Name:           brotli
Version:        1.2.0
Release:        3%{?dist}
Summary:        Lossless compression algorithm
License:        MIT
URL:            https://github.com/google/brotli
Source0:        https://github.com/google/brotli/archive/refs/tags/v1.2.0.tar.gz#/brotli-1.2.0.tar.gz
Requires: libbrotli%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-brotli = %{version}-%{release}
# /oreon:deps
%description

%package -n libbrotli
Summary:        Library for brotli lossless compression algorithm
%description -n libbrotli

%package -n python3-brotli
Summary:        Lossless compression algorithm (python 3)
%description -n python3-brotli

This package installs a Python 3 module.

%package devel
Summary:        Lossless compression algorithm (development files)
Requires: brotli%{?_isa} = %{version}-%{release}
Requires: libbrotli%{?_isa} = %{version}-%{release}
%description devel

This package installs the development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n brotli-1.2.0
# fix permissions for -debuginfo
# rpmlint will complain if I create an extra %%files section for
# -debuginfo for this so we'll put it here instead
chmod 644 c/enc/*.[ch]
chmod 644 c/include/brotli/*.h
chmod 644 c/tools/brotli.c

%build

%cmake \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%cmake_build
%pyproject_wheel
%install
%cmake_install
find %{buildroot}%{_mandir}/man3 -name '*.3' -exec mv -v '{}' '{}brotli' ';'
%pyproject_install
%oreon_autofiles libbrotli usr/*/lib*.so.*
%oreon_autofiles python3-brotli usr/lib/python3*/site-packages/brotli* usr/lib64/python3*/site-packages/brotli* usr/bin/*
%oreon_autofiles main usr/*/lib*.so.* usr/lib/python3*/site-packages/brotli* usr/lib64/python3*/site-packages/brotli* usr/bin/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%pyproject_check_import
cd python
%{py3_test_envvars} %{python3} -m tests.bro_test
%{py3_test_envvars} %{python3} -m tests.compress_test
%{py3_test_envvars} %{python3} -m tests.compressor_test
%{py3_test_envvars} %{python3} -m tests.decompress_test
%{py3_test_envvars} %{python3} -m tests.decompressor_test
%files
%files -n libbrotli -f %{oreon_filedir}/libbrotli.list
%files -n python3-brotli -f %{oreon_filedir}/python3-brotli.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-3
- Import
