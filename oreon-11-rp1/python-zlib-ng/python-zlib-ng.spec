%global source0_hash f0678dec1dd2ef04843268eb80c443155a9859523e151e7870219fa7a26d7688

Name:           python-zlib-ng
Version:        1.0.0
Release:        %autorelease
Summary:        Drop-in replacement for zlib and gzip modules using zlib-ng

# The entire source is PSF-2.0, since we do not use the vendored zlib-ng
# sources that would be present in the PyPI sdist. We use the GitHub archive
# because it contains tests and changelogs that the PyPI sdist lacks.
License:        PSF-2.0
URL:            https://github.com/pycompression/python-zlib-ng
Source:         %{url}/archive/v%{version}/python-zlib-ng-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib-ng)

# List test dependencies manually because this is easier than patching coverage
# out of tox.ini
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-timeout}
BuildRequires:  python3-test

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

%description %{common_description}

%package -n python3-zlib-ng
Summary:        %{summary}

%description -n python3-zlib-ng %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n python-zlib-ng-%{version} -p1
rm -rvf src/zlib_ng/zlib-ng

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
export CFLAGS="${CFLAGS} $(pkgconf --cflags zlib-ng)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs zlib-ng)"
export PYTHON_ZLIB_NG_LINK_DYNAMIC='1'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l zlib_ng

%check
# Note that it is *not* safe to run tests in parallel (pytest-xdist, -n auto)
# due to filesystem race conditions.
%pytest -v -k "${k-}" tests/

%files -n python3-zlib-ng -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst

%changelog
%autochangelog
