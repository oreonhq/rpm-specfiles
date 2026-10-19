%global source0_hash 1347f3b6c5522c5c50db5d9e2801257cea86639e87b46c6635f22005ee3ded25
%bcond tests 1
%bcond nibabel 1
Name:           python-indexed_gzip
Version:        1.10.3
Release:        1%{?dist}
Summary:        Fast random access of gzip files in Python
License:        Zlib
URL:            https://github.com/pauldmccarthy/indexed_gzip
Source0:        https://files.pythonhosted.org/packages/source/i/indexed_gzip/indexed_gzip-%{version}.tar.gz
%if %{with tests}
%if %{with nibabel}
%endif
%endif
%global desc %{expand:
The indexed_gzip project is a Python extension which aims to provide a drop-in
replacement for the built-in Python gzip.GzipFile class, the IndexedGzipFile.
indexed_gzip was written to allow fast random access of compressed NIFTI image
files (for which GZIP is the de-facto compression standard), but will work with
any GZIP file. indexed_gzip is easy to use with nibabel.
The standard gzip.GzipFile class exposes a random access-like interface (via
its seek and read methods), but every time you seek to a new point in the
uncompressed data stream, the GzipFile instance has to start decompressing from
the beginning of the file, until it reaches the requested location.
An IndexedGzipFile instance gets around this performance limitation by building
an index, which contains *seek points*, mappings between corresponding
locations in the compressed and uncompressed data streams. Each seek point is
accompanied by a chunk (32KB) of uncompressed data which is used to initialize
the decompression algorithm, allowing us to start reading from any seek point.
If the index is built with a seek point spacing of 1MB, we only have to
decompress (on average) 512KB of data to read from any location in the file.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-indexed_gzip = %{version}-%{release}
# /oreon:deps
%package -n       python3-indexed_gzip+test
Summary:        Metapackage for python3-indexed_gzip test extras
Requires:       python3-indexed_gzip = %{version}-%{release}
Provides:       python3dist(indexed_gzip[test]) = %{version}-%{release}

%description -n python3-indexed_gzip+test
Metapackage for python3-indexed_gzip test extras.

%description %{desc}

%package -n python3-indexed-gzip
Summary:        Fast random access of gzip files in Python
%py_provides python3-indexed_gzip
Obsoletes:      python3-indexed_gzip < 1.7.0-4
%description -n python3-indexed-gzip %{desc}

%prep

%autosetup -p1
# Remove shebangs from non-script sources
find indexed_gzip -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'
# Make sure Cythonized C source files are not present in the tarball; they must
# be regenerated. Retain “hand-written” C sources.
find indexed_gzip -type f -name '*.pyx' | sed -r 's/\.pyx$/.c/' | xargs -r rm -vf

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-indexed-gzip usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%pytest %{buildroot}%{python3_sitearch}/indexed_gzip -n auto -k "${k-}"
%endif
%files
%files -n python3-indexed-gzip -f %{oreon_filedir}/python3-indexed-gzip.list

%changelog

%autochangelog
