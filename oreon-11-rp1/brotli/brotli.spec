Name:           brotli
Version:        1.2.0
Release:        3%{?dist}
Summary:        Lossless compression algorithm

License:        MIT
URL:            https://github.com/google/brotli
Source0:        %{url}/archive/v%{version}/brotli-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

Requires: libbrotli%{?_isa} = %{version}-%{release}

%global _description %{expand:
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.}

%description %{_description}

%package -n libbrotli
Summary:        Library for brotli lossless compression algorithm

%description -n libbrotli %{_description}

%package -n python3-brotli
Summary:        Lossless compression algorithm (python 3)

%description -n python3-brotli %{_description}

This package installs a Python 3 module.

%package devel
Summary:        Lossless compression algorithm (development files)
Requires: brotli%{?_isa} = %{version}-%{release}
Requires: libbrotli%{?_isa} = %{version}-%{release}

%description devel %{_description}

This package installs the development files.

%prep
%autosetup -p1
# fix permissions for -debuginfo
# rpmlint will complain if I create an extra %%files section for
# -debuginfo for this so we'll put it here instead
chmod 644 c/enc/*.[ch]
chmod 644 c/include/brotli/*.h
chmod 644 c/tools/brotli.c

%generate_buildrequires
%pyproject_buildrequires

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%cmake_build
%pyproject_wheel

%install
%cmake_install
# Names of C API (section 3) man pages are too generic; rename them from .3 to
# .3brotli (which is how they were manually installed in the past anyway)
find %{buildroot}%{_mandir}/man3 -name '*.3' -exec mv -v '{}' '{}brotli' ';'
%pyproject_install
%pyproject_save_files -l brotli _brotli

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
%{_bindir}/brotli
%{_mandir}/man1/brotli.1*

%files -n libbrotli
%license LICENSE
%{_libdir}/libbrotlicommon.so.1*
%{_libdir}/libbrotlidec.so.1*
%{_libdir}/libbrotlienc.so.1*

%files -n python3-brotli -f %{pyproject_files}

%files devel
%{_includedir}/brotli
%{_libdir}/libbrotlicommon.so
%{_libdir}/libbrotlidec.so
%{_libdir}/libbrotlienc.so
%{_libdir}/pkgconfig/libbrotlicommon.pc
%{_libdir}/pkgconfig/libbrotlidec.pc
%{_libdir}/pkgconfig/libbrotlienc.pc
%{_mandir}/man3/constants.h.3brotli*
%{_mandir}/man3/decode.h.3brotli*
%{_mandir}/man3/encode.h.3brotli*
%{_mandir}/man3/types.h.3brotli*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-3
- Prepare for Oreon 11 (RP1)
