%global source0_hash f0678dec1dd2ef04843268eb80c443155a9859523e151e7870219fa7a26d7688
Name:           python-zlib-ng
Version:        1.0.0
Release:        1%{?dist}
Summary:        Drop-in replacement for zlib and gzip modules using zlib-ng
License:        PSF-2.0
URL:            https://github.com/pycompression/python-zlib-ng
Source0:        https://github.com/pycompression/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%global common_description %{expand:
Faster zlib and gzip compatible compression and decompression by providing
Python bindings for the zlib-ng library.
This package provides Python bindings for the zlib-ng library.
python-zlib-ng provides the bindings by offering three modules:
  • zlib_ng: A drop-in replacement for the zlib module that uses zlib-ng to
    accelerate its performance.
  • gzip_ng: A drop-in replacement for the gzip module that uses zlib_ng
    instead of zlib to perform its compression and checksum tasks, which
    improves performance.
  • gzip_ng_threaded offers an open function which returns buffered read or
    write streams that can be used to read and write large files while escaping
    the GIL using one or multiple threads. This functionality only works for
    streaming, seeking is not supported.
zlib_ng and gzip_ng are almost fully compatible with zlib and gzip from the
Python standard library. There are some minor differences see:
https://pypi.org/project/zlib-ng/#differences-with-zlib-and-gzip-modules
Beginning with Fedora Linux 40, zlib-ng provides the system-wide zlib
implementation, so the Python standard library already uses it by default.
However, some projects still need the APIs provided by this package.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-zlib-ng = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-zlib-ng
Summary:        Drop-in replacement for zlib and gzip modules using zlib-ng
%description -n python3-zlib-ng %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n python-zlib-ng-%{version} -p1
rm -rvf src/zlib_ng/zlib-ng

%build

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
export CFLAGS="${CFLAGS} $(pkgconf --cflags zlib-ng)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs zlib-ng)"
export PYTHON_ZLIB_NG_LINK_DYNAMIC='1'
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zlib-ng usr/lib/python3*/site-packages/zlib_ng* usr/lib64/python3*/site-packages/zlib_ng* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zlib_ng* usr/lib64/python3*/site-packages/zlib_ng* usr/bin/*

%check

%pytest -v -k "${k-}" tests/
%files
%files -n python3-zlib-ng -f %{oreon_filedir}/python3-zlib-ng.list

%changelog

%autochangelog
