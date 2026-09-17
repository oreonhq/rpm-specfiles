%global source0_hash bd09adb4feac11fe49d1604f296618866702be610c86e2d513b561d877de6b18

# -*- sh-shell: rpm -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

%bcond_without use_flight
%bcond_with use_plasma
%bcond_with use_gandiva
%bcond_with use_mimalloc
%bcond_without use_ninja
# TODO: Enable this. This works on local but is fragile on GitHub Actions and
# Travis CI.
%bcond_with use_s3
%bcond_without have_rapidjson
%bcond_without have_re2
%bcond_without have_utf8proc

Name:		libarrow
Version:	23.0.1
Release:	2%{?dist}
Summary:	A toolbox for accelerated data interchange and in-memory processing
License:	Apache-2.0
URL:		https://arrow.apache.org/
Requires:	%{name}-doc = %{version}-%{release}
Source0:	https://archive.apache.org/dist/arrow/arrow-%{version}/apache-arrow-%{version}.tar.gz
Patch:		0001-python-pyarrow-tests-read_record_patch.py.patch
Patch:		0002-python-pyarrow-tests-test_ipc.py.patch

# Apache ORC (liborc) has numerous compile errors and apparently assumes
# a 64-bit build and runtime environment. This is only consumer of the liborc
# package, and in turn the only consumers of this and liborc are Ceph, which
# is also 64-bit only, and rdal.
ExcludeArch:	%{ix86} %{arm}
BuildRequires:	bison
BuildRequires:	boost-devel
BuildRequires:	brotli-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
%if %{with use_ninja}
BuildRequires:	ninja-build
%endif
BuildRequires:	meson
%if %{with use_s3}
BuildRequires:	curl-devel
%endif
BuildRequires:	flex
BuildRequires:	gcc-c++
BuildRequires:	gflags-devel
BuildRequires:	glog-devel
BuildRequires:	grpc-devel
BuildRequires:	grpc-plugins
BuildRequires:	libzstd-devel
BuildRequires:	lz4-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-numpy
BuildRequires:	python%{python3_pkgversion}-Cython
BuildRequires:	python%{python3_pkgversion}-pandas
BuildRequires:	python%{python3_pkgversion}-pytest
BuildRequires:	python%{python3_pkgversion}-hypothesis
BuildRequires:	python%{python3_pkgversion}-pytzdata
BuildRequires:	xsimd-devel
BuildRequires:	abseil-cpp-devel
BuildRequires:	c-ares-devel
BuildRequires:	thrift-devel
%if %{with have_rapidjson}
BuildRequires:	rapidjson-devel
%endif
%if %{with have_re2}
BuildRequires:	re2-devel
%endif
BuildRequires:	snappy-devel
%if %{with have_utf8proc}
BuildRequires:	utf8proc-devel
%endif
BuildRequires:	zlib-devel
BuildRequires:	liborc-devel
%if %{with use_gandiva}
BuildRequires:	llvm-devel
BuildRequires:	ncurses-devel
%endif
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc

# Additional pyarrow build requirements; see also %%generate_buildrequires
BuildRequires:  python3dist(cffi)

# python3-pyarrow provides bogus library SONAME provides
# https://bugzilla.redhat.com/show_bug.cgi?id=2326774
%global __provides_exclude (^libarrow_python(_[^.]+)?|.cpython-.*)\\.so.*$
%global __requires_exclude ^libarrow_python(_[^.]+)?\\.so.*$

%description
Apache Arrow defines a language-independent columnar memory
format for flat and hierarchical data, organized for efficient
analytic operations on modern hardware like CPUs and GPUs. The
Arrow memory format also supports zero-copy reads for lightning-
fast data access without serialization overhead

%files
%{_libdir}/libarrow.so.*

#--------------------------------------------------------------------

%package doc
Summary:	Documentation files for Apache Arrow C++
BuildArch:	noarch

%description doc
Documentation files for Apache Arrow C++.

Obsoletes:	%{name}-glib-doc < %{version}-%{release}
Obsoletes:	%{name}-dataset-glib-doc < %{version}-%{release}
Obsoletes:	%{name}-parquet-glib-doc < %{version}-%{release}
Obsoletes:	plasma-glib-doc < %{version}-%{release}
Obsoletes:	gandiva-glib-doc < %{version}-%{release}

%files doc
%license LICENSE.txt
%doc README.md NOTICE.txt
%exclude %{_docdir}/arrow/

#--------------------------------------------------------------------

%package devel
Summary:	Libraries and header files for Apache Arrow C++
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-compute-devel = %{version}-%{release}
Requires:	brotli-devel
Requires:	bzip2-devel
Requires:	libzstd-devel
Requires:	lz4-devel
Requires:	openssl-devel
%if %{with have_rapidjson}
Requires:	rapidjson-devel
%endif
%if %{with have_re2}
Requires:	re2-devel
%endif
Requires:	snappy-devel
%if %{with have_utf8proc}
Requires:	utf8proc-devel
%endif
Requires:	zlib-devel

%description devel
Libraries and header files for Apache Arrow C++.

%files devel
%dir %{_includedir}/arrow/
     %{_includedir}/arrow/*
%exclude %{_includedir}/arrow/dataset/
%exclude %{_includedir}/arrow/compute/
%if %{with use_flight}
%exclude %{_includedir}/arrow/flight/
%exclude %{_includedir}/arrow-flight-glib
%endif
%exclude %{_libdir}/cmake/Arrow/FindBrotliAlt.cmake
%exclude %{_libdir}/cmake/Arrow/Findlz4Alt.cmake
%exclude %{_libdir}/cmake/Arrow/FindorcAlt.cmake
%exclude %{_libdir}/cmake/Arrow/FindSnappyAlt.cmake
%exclude %{_libdir}/cmake/Arrow/Findre2Alt.cmake
%exclude %{_libdir}/cmake/Arrow/Findutf8proc.cmake
%exclude %{_libdir}/cmake/Arrow/FindzstdAlt.cmake
%exclude %{_libdir}/cmake/Arrow/FindOpenSSLAlt.cmake
%exclude %{_libdir}/cmake/Arrow/FindProtobufAlt.cmake
%dir %{_libdir}/cmake/Arrow/
     %{_libdir}/cmake/Arrow/ArrowConfig*.cmake
     %{_libdir}/cmake/Arrow/ArrowOptions.cmake
     %{_libdir}/cmake/Arrow/ArrowTargets*.cmake
     %{_libdir}/cmake/Arrow/arrow-config.cmake
%{_libdir}/libarrow.so
%{_libdir}/pkgconfig/arrow-csv.pc
%{_libdir}/pkgconfig/arrow-filesystem.pc
%{_libdir}/pkgconfig/arrow-json.pc
%{_libdir}/pkgconfig/arrow-orc.pc
%{_libdir}/pkgconfig/arrow.pc
%{_datadir}/arrow/gdb/gdb_arrow.py
%{_datadir}/gdb/auto-load%{_libdir}/libarrow.so.*-gdb.py

#--------------------------------------------------------------------

%package compute-libs
Summary:	C++ library to read and write semantic datasets
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description compute-libs
This package contains the libraries for Apache Arrow Compute

%files compute-libs
%{_libdir}/libarrow_compute.so.*

#--------------------------------------------------------------------

%package compute-devel
Summary:	Libraries and header files for Apache Arrow compute
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-compute-libs%{?_isa} = %{version}-%{release}

%description compute-devel
Libraries and header files for Apache Arrow Compute

%files compute-devel
%dir %{_includedir}/arrow/compute/
     %{_includedir}/arrow/compute/*
%{_libdir}/cmake/ArrowCompute/*.cmake
%{_libdir}/libarrow_compute.so
%{_libdir}/pkgconfig/arrow-compute.pc

#--------------------------------------------------------------------

%package dataset-libs
Summary:	C++ library to read and write semantic datasets
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description dataset-libs
This package contains the libraries for Apache Arrow dataset.

%files dataset-libs
%{_libdir}/libarrow_dataset.so.*

#--------------------------------------------------------------------

%package dataset-devel
Summary:	Libraries and header files for Apache Arrow dataset
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-dataset-libs%{?_isa} = %{version}-%{release}

%description dataset-devel
Libraries and header files for Apache Arrow dataset.

%files dataset-devel
%dir %{_includedir}/arrow/dataset/
     %{_includedir}/arrow/dataset/*
%{_libdir}/cmake/ArrowDataset/*.cmake
%{_libdir}/libarrow_dataset.so
%{_libdir}/pkgconfig/arrow-dataset.pc

#--------------------------------------------------------------------

%package acero-libs
Summary:	C++ library for fast data transport
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description acero-libs
This package contains the libraries for Apache Arrow Acero.

%files acero-libs
%{_libdir}/libarrow_acero.so.*

#--------------------------------------------------------------------

%package acero-devel
Summary:	Libraries for Apache Arrow Acero
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-flight-libs%{?_isa} = %{version}-%{release}

%description acero-devel
Libraries and header files for Apache Arrow Acero.

%files acero-devel
%{_libdir}/cmake/ArrowAcero/*.cmake
%{_libdir}/libarrow_acero.so
%{_libdir}/pkgconfig/arrow-acero.pc

#--------------------------------------------------------------------

%if %{with use_flight}
%package flight-libs
Summary:	C++ library for fast data transport
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description flight-libs
This package contains the libraries for Apache Arrow Flight.

%files flight-libs
%{_libdir}/libarrow_flight.so.*
%{_libdir}/libarrow-flight-glib.so.*
%dir %{_libdir}/girepository-1.0/
     %{_libdir}/girepository-1.0/ArrowFlight-23.0.typelib

#--------------------------------------------------------------------

%package flight-devel
Summary:	Libraries and header files for Apache Arrow Flight
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-flight-libs%{?_isa} = %{version}-%{release}

%description flight-devel
Libraries and header files for Apache Arrow Flight.

%files flight-devel
%dir %{_includedir}/arrow/flight/
     %{_includedir}/arrow/flight/*
%dir %{_includedir}/arrow-flight-glib/
     %{_includedir}/arrow-flight-glib/*
%{_libdir}/cmake/ArrowFlight/*.cmake
%{_libdir}/libarrow_flight.so
%{_libdir}/libarrow-flight-glib.so
%{_libdir}/pkgconfig/arrow-flight.pc
%{_libdir}/pkgconfig/arrow-flight-glib.pc
%dir %{_datadir}/gir-1.0/
     %{_datadir}/gir-1.0/ArrowFlight-23.0.gir
%endif

#--------------------------------------------------------------------

%if %{with use_gandiva}
%package -n gandiva-libs
Summary:	C++ library for compiling and evaluating expressions
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}
Requires:	ncurses-libs

%description -n gandiva-libs
This package contains the libraries for Gandiva.

%files -n gandiva-libs
%{_libdir}/libgandiva.so.*

#--------------------------------------------------------------------

%package -n gandiva-devel
Summary:	Libraries and header files for Gandiva
Requires:	gandiva-libs%{?_isa} = %{version}-%{release}
Requires:	llvm-devel

%description -n gandiva-devel
Libraries and header files for Gandiva.

%files -n gandiva-devel
%dir %{_includedir}/gandiva/
     %{_includedir}/gandiva/
%{_libdir}/cmake/Gandiva/*.cmake
%{_libdir}/libgandiva.so
%{_libdir}/pkgconfig/gandiva.pc
%endif

#--------------------------------------------------------------------

%package python-libs
Summary:	Python integration library for Apache Arrow
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-numpy

%description python-libs
This package contains the Python integration library for Apache Arrow.

%files python-libs
%{python3_sitearch}/pyarrow/libarrow_python.so

#--------------------------------------------------------------------

%package python-devel
Summary:	Libraries and header files for Python integration library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-python-libs%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-devel

%description python-devel
Libraries and header files for Python integration library for Apache Arrow.

%files python-devel
%dir %{python3_sitearch}/pyarrow/include/arrow/python
     %{python3_sitearch}/pyarrow/include/arrow/python/*
%exclude %{python3_sitearch}/pyarrow/include/arrow/python/flight.h

#--------------------------------------------------------------------

%if %{with use_flight}
%package python-flight-libs
Summary:	Python integration library for Apache Arrow Flight
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-flight-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-python-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description python-flight-libs
This package contains the Python integration library for Apache Arrow Flight.

%files python-flight-libs
%{python3_sitearch}/pyarrow/libarrow_python_flight.so

#--------------------------------------------------------------------

%package python-flight-devel
Summary:	Libraries and header files for Python integration
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-flight-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-python-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-python-flight-libs%{?_isa} = %{version}-%{release}

%description python-flight-devel
Libraries and header files for Python integration library for
Apache Arrow Flight.

%files python-flight-devel
%{python3_sitearch}/pyarrow/include/arrow/python/flight.h
%endif

%if %{with use_plasma}
#--------------------------------------------------------------------

%package -n plasma-libs
Summary:	Runtime libraries for Plasma in-memory object store
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description -n plasma-libs
This package contains the libraries for Plasma in-memory object store.

%files -n plasma-libs
%{_libdir}/libplasma.so.*

#--------------------------------------------------------------------

%package -n plasma-store-server
Summary:	Server for Plasma in-memory object store
Requires:	plasma-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description -n plasma-store-server
This package contains the server for Plasma in-memory object store.

%files -n plasma-store-server
%{_bindir}/plasma-store-server

#--------------------------------------------------------------------

%package -n plasma-libs-devel
Summary:	Libraries and header files for Plasma in-memory object store
Requires:	plasma-libs%{?_isa} = %{version}-%{release}
# plasma-devel a.k.a. kdelibs-devel provides
# conflicts with all versions of plasma-devel %%{_libdir}/libplasma.so
BuildConflicts: plasma-devel
# conflicts with all versions of plasma-workspace-devel %%{_includedir}/*
BuildConflicts: plasma-workspace-devel

%description -n plasma-libs-devel
Libraries and header files for Plasma in-memory object store.

%files -n plasma-libs-devel
%dir %{_includedir}/plasma/
     %{_includedir}/plasma/*
%{_libdir}/cmake/Arrow/Plasma*.cmake
%{_libdir}/libplasma.so
%{_libdir}/pkgconfig/plasma*.pc

%endif
#--------------------------------------------------------------------

%package -n parquet-libs
Summary:	Runtime libraries for Apache Parquet C++
Requires:	boost-program-options
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description -n parquet-libs
This package contains the libraries for Apache Parquet C++.

%files -n parquet-libs
%{_libdir}/libparquet.so.*

#--------------------------------------------------------------------

%package -n parquet-libs-devel
Summary:	Libraries and header files for Apache Parquet C++
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	parquet-libs%{?_isa} = %{version}-%{release}
Requires:	zlib-devel

%description -n parquet-libs-devel
Libraries and header files for Apache Parquet C++.

%files -n parquet-libs-devel
%dir %{_includedir}/parquet/
     %{_includedir}/parquet/*
%{_libdir}/cmake/Parquet/*.cmake
%{_libdir}/libparquet.so
%{_libdir}/pkgconfig/parquet*.pc

#--------------------------------------------------------------------

%package glib-libs
Summary:	Runtime libraries for Apache Arrow GLib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description glib-libs
This package contains the libraries for Apache Arrow GLib.

%files glib-libs
%{_libdir}/libarrow-glib.so.*
%dir %{_libdir}/girepository-1.0/
     %{_libdir}/girepository-1.0/Arrow-23.0.typelib

#--------------------------------------------------------------------

%package glib-devel
Summary:	Libraries and header files for Apache Arrow GLib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-libs%{?_isa} = %{version}-%{release}
Requires:	glib2-devel
Requires:	gobject-introspection-devel

%description glib-devel
Libraries and header files for Apache Arrow GLib.

%files glib-devel
%dir %{_includedir}/arrow-glib/
     %{_includedir}/arrow-glib/*
%{_libdir}/libarrow-glib.so
%{_libdir}/pkgconfig/arrow-glib.pc
%{_libdir}/pkgconfig/arrow-orc-glib.pc
%dir %{_datadir}/arrow-glib/
     %{_datadir}/arrow-glib/*
%dir %{_datadir}/gir-1.0/
     %{_datadir}/gir-1.0/Arrow-23.0.gir

#--------------------------------------------------------------------

%package dataset-glib-libs
Summary:	Runtime libraries for Apache Arrow dataset GLib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-dataset-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description dataset-glib-libs
This package contains the libraries for Apache Arrow dataset GLib.

%files dataset-glib-libs
%{_libdir}/libarrow-dataset-glib.so.*
%dir %{_libdir}/girepository-1.0/
     %{_libdir}/girepository-1.0/ArrowDataset-23.0.typelib

#--------------------------------------------------------------------

%package dataset-glib-devel
Summary:	Libraries and header files for Apache Arrow dataset GLib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-dataset-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-dataset-glib-libs%{?_isa} = %{version}-%{release}

%description dataset-glib-devel
Libraries and header files for Apache Arrow dataset GLib.

%files dataset-glib-devel
%dir %{_includedir}/arrow-dataset-glib/
     %{_includedir}/arrow-dataset-glib/*
%{_libdir}/libarrow-dataset-glib.so
%{_libdir}/pkgconfig/arrow-dataset-glib.pc
%dir %{_datadir}/gir-1.0/
     %{_datadir}/gir-1.0/ArrowDataset-23.0.gir

#--------------------------------------------------------------------

%if %{with use_gandiva}
%package -n gandiva-glib-libs
Summary:	Runtime libraries for Gandiva GLib
Requires:	gandiva-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description -n gandiva-glib-libs
This package contains the libraries for Gandiva GLib.

%files -n gandiva-glib-libs
%{_libdir}/libgandiva-glib.so.*

#--------------------------------------------------------------------

%package -n gandiva-glib-devel
Summary:	Libraries and header files for Gandiva GLib
Requires:	gandiva-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-devel%{?_isa} = %{version}-%{release}

%description -n gandiva-glib-devel
Libraries and header files for Gandiva GLib.

%files -n gandiva-glib-devel
%dir %{_includedir}/gandiva-glib/
     %{_includedir}/gandiva-glib/*
%{_libdir}/libgandiva-glib.so
%{_libdir}/pkgconfig/gandiva-glib.pc
%endif

%if %{with use_plasma}
#--------------------------------------------------------------------

%package -n plasma-glib-libs
Summary:	Runtime libraries for Plasma GLib
Requires:	plasma-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description -n plasma-glib-libs
This package contains the libraries for Plasma GLib.

%files -n plasma-glib-libs
%{_libdir}/libplasma-glib.so.*

#--------------------------------------------------------------------

%package -n plasma-glib-devel
Summary:	Libraries and header files for Plasma GLib
Requires:	plasma-devel%{?_isa} = %{version}-%{release}
Requires:	plasma-glib-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-devel%{?_isa} = %{version}-%{release}

%description -n plasma-glib-devel
Libraries and header files for Plasma GLib.

%files -n plasma-glib-devel
%dir %{_includedir}/plasma-glib/
     %{_includedir}/plasma-glib/*
%{_libdir}/libplasma-glib.so
%{_libdir}/pkgconfig/plasma-glib.pc
%endif

#--------------------------------------------------------------------

%package -n parquet-glib-libs
Summary:	Runtime libraries for Apache Parquet GLib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	parquet-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}

%description -n parquet-glib-libs
This package contains the libraries for Apache Parquet GLib.

%files -n parquet-glib-libs
%{_libdir}/libparquet-glib.so.*
%dir %{_libdir}/girepository-1.0/
     %{_libdir}/girepository-1.0/Parquet-23.0.typelib

#--------------------------------------------------------------------

%package -n parquet-glib-devel
Summary:	Libraries and header files for Apache Parquet GLib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	parquet-libs-devel%{?_isa} = %{version}-%{release}
Requires:	parquet-glib-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib-devel%{?_isa} = %{version}-%{release}

%description -n parquet-glib-devel
Libraries and header files for Apache Parquet GLib.

%files -n parquet-glib-devel
%dir %{_includedir}/parquet-glib/
     %{_includedir}/parquet-glib/*
%{_libdir}/libparquet-glib.so
%{_libdir}/pkgconfig/parquet-glib.pc
%dir %{_datadir}/gir-1.0/
     %{_datadir}/gir-1.0/Parquet-23.0.gir

#--------------------------------------------------------------------

%package -n python3-pyarrow
Summary: Python library for Apache Arrow

%description -n python3-pyarrow
Python library for Apache Arrow

%files -n python3-pyarrow -f %{pyproject_files}
%exclude %{python3_sitearch}/pyarrow/lib_api.h
%exclude %{python3_sitearch}/pyarrow/include

#--------------------------------------------------------------------

%package -n python3-pyarrow-devel
Summary: Development files for python3-pyarrow

Requires:       python3-pyarrow%{?_isa} = %{version}-%{release}

%description -n python3-pyarrow-devel
Development files for python3-pyarrow

%files -n python3-pyarrow-devel
%{python3_sitearch}/pyarrow/lib_api.h
%{python3_sitearch}/pyarrow/include

#--------------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n apache-arrow-%{version}
# We do not need to (nor can we) build for an old version of numpy:
sed -r -i 's/(oldest-supported-)(numpy)/\2/' python/pyproject.toml

%generate_buildrequires
pushd python >/dev/null
export SETUPTOOLS_SCM_VERSION_WRITE_TO_PREFIX="python"
%pyproject_buildrequires
popd >/dev/null

%build
pushd cpp
%cmake \
%if %{with use_flight}
  -DARROW_FLIGHT:BOOL=ON \
%endif
%if %{with use_gandiva}
  -DARROW_GANDIVA:BOOL=ON \
%endif
%if %{with use_mimalloc}
  -DARROW_MIMALLOC:BOOL=ON \
%else
  -DARROW_MIMALLOC:BOOL=OFF \
%endif
  -DARROW_ORC=ON \
  -DARROW_PARQUET:BOOL=ON \
%if %{with use_plasma}
  -DARROW_PLASMA:BOOL=ON \
%endif
  -DARROW_PYTHON:BOOL=ON \
  -DARROW_JEMALLOC:BOOL=OFF \
  -DARROW_SIMD_LEVEL:STRING='NONE' \
  -DGRPC_SOURCE="SYSTEM" \
  -Dxsimd_SOURCE="SYSTEM" \
%if %{with use_s3}
  -DARROW_S3:BOOL=ON \
%endif
  -DARROW_WITH_BROTLI:BOOL=ON \
  -DARROW_WITH_BZ2:BOOL=ON \
  -DARROW_WITH_LZ4:BOOL=ON \
  -DARROW_WITH_SNAPPY:BOOL=ON \
  -DARROW_WITH_ZLIB:BOOL=ON \
  -DARROW_WITH_ZSTD:BOOL=ON \
  -DARROW_USE_XSIMD:BOOL=ON \
  -DARROW_BUILD_STATIC:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
  -DARROW_USE_CCACHE:BOOL=OFF \
  -DCMAKE_UNITY_BUILD:BOOL=ON \
  -DPARQUET_REQUIRE_ENCRYPTION:BOOL=ON \
  -DPythonInterp_FIND_VERSION:BOOL=ON \
  -DPythonInterp_FIND_VERSION_MAJOR=3 \
%if %{with use_ninja}
  -GNinja
%endif

export VERBOSE=1
export GCC_COLORS=
%cmake_build
popd

pushd c_glib
%meson \
  -Darrow_cpp_build_dir=../cpp/%{_vpath_builddir} \
  -Darrow_cpp_build_type=relwithdebinfo \
  -Dgtk_doc=true
%meson_build
popd

# hack alert. install libarrow somewhere (temporary) so that python
# (i.e. pyarrow) can build against it. If someone knows how to invoke
# cmake or # pyproject_wheel using the bits in ../cpp instead, that
# would be preferable to this.
pushd cpp
DESTDIR="/tmp" %__cmake --install "%{__cmake_builddir}"
popd

pushd python
export \
  CMAKE_PREFIX_PATH=/tmp%{_prefix} \
  PYARROW_BUNDLE_ARROW_CPP_HEADERS=1 \
  PYARROW_BUNDLE_PLASMA_EXECUTABLE=0 \
  PYARROW_WITH_DATASET=1 \
  PYARROW_WITH_FLIGHT=1 \
  PYARROW_WITH_PARQUET=1 \
  PYARROW_WITH_PARQUET_ENCRYPTION=1 \
  %{?with_use_plasma:PYARROW_WITH_PLASMA=1} \
  %{?with_use_gandiva:PYARROW_WITH_GANDIVA=1} \
  PYARROW_PARALLEL=%{_smp_build_ncpus} \
  PYARROW_INSTALL_TESTS=0 \
  SETUPTOOLS_SCM_VERSION_WRITE_TO_PREFIX="python"
%pyproject_wheel
popd
rm -rf /tmp%{_prefix}

#--------------------------------------------------------------------

%install

pushd python
export PYARROW_INSTALL_TESTS=0
%pyproject_install
%pyproject_save_files pyarrow
popd

pushd c_glib
%meson_install
popd

pushd cpp
%cmake_install
popd

%check
export LD_LIBRARY_PATH='%{buildroot}%{_libdir}'
# While https://github.com/apache/arrow/pull/13904 partially fixes
# https://issues.apache.org/jira/browse/ARROW-17389, conftest.py is still
# installed. We must skip testing it because it would import pytest.
#
# Additionally, skip subpackages corresponding to missing optional
# functionality.
%{pyproject_check_import \
    -e 'pyarrow.conftest' \
    -e 'pyarrow.orc' -e 'pyarrow._orc' \
    %{?!with_use_plasma:-e 'pyarrow.plasma' -e 'pyarrow._plasma'} \
    -e 'pyarrow.substrait' -e 'pyarrow._substrait' \
    -e 'pyarrow.cuda' \
    -e 'pyarrow.libarrow_python' -e 'pyarrow._libarrow_python' \
    -e 'pyarrow.libarrow_python_flight' -e 'pyarrow._libarrow_python_flight' \
    -e 'pyarrow.libarrow_python_parquet_encryption' \
    -e 'pyarrow.tests.read_record_batch' -e 'pyarrow.tests.test_cuda' \
    -e 'pyarrow.tests.test_cuda_numba_interop' -e 'pyarrow.tests.test_jvm'}

#--------------------------------------------------------------------

%changelog
%autochangelog
