%global source0_hash 66b07ef7315a31bfe1089cd3d71a7de781c9dca986762d0b4fe7c0ef17465d10
%bcond_with extras
Name:           python-pandas
Version:        3.0.6
Release:        1%{?dist}
Summary:        Powerful data structures for data analysis, time series, and statistics
License:        ...
URL:            https://pandas.pydata.org
Source0:        https://files.pythonhosted.org/packages/source/p/pandas/pandas-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 4
BuildRequires:  python3dist(cython) > 3.1.0
BuildRequires:  python3dist(meson) < 2
BuildRequires:  python3dist(meson) >= 1.2.1
BuildRequires:  python3dist(meson-python) < 1
BuildRequires:  python3dist(meson-python) >= 0.17.1
BuildRequires:  python3dist(numpy) >= 2.0.0
Requires:       python3-pandas = %{version}-%{release}
# /oreon:deps
%package -n       python3-pandas+test
Summary:        Metapackage for python3-pandas test extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(hypothesis) >= 6.116.0
Requires:       python3dist(pytest) >= 8.3.4
Requires:       python3dist(pytest) < 9.1
Requires:       python3dist(pytest-xdist) >= 3.6.1
Provides:       python3dist(pandas[test]) = %{version}-%{release}

%description -n python3-pandas+test
Metapackage for python3-pandas test extras.

%package -n       python3-pandas+pyarrow
Summary:        Metapackage for python3-pandas pyarrow extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(pyarrow) >= 13.0.0
Provides:       python3dist(pandas[pyarrow]) = %{version}-%{release}

%description -n python3-pandas+pyarrow
Metapackage for python3-pandas pyarrow extras.

%package -n       python3-pandas+performance
Summary:        Metapackage for python3-pandas performance extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(bottleneck) >= 1.4.2
Requires:       python3dist(numba) >= 0.60.0
Requires:       python3dist(numexpr) >= 2.10.2
Provides:       python3dist(pandas[performance]) = %{version}-%{release}

%description -n python3-pandas+performance
Metapackage for python3-pandas performance extras.

%package -n       python3-pandas+computation
Summary:        Metapackage for python3-pandas computation extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(scipy) >= 1.14.1
Requires:       python3dist(xarray) >= 2024.10.0
Provides:       python3dist(pandas[computation]) = %{version}-%{release}

%description -n python3-pandas+computation
Metapackage for python3-pandas computation extras.

%package -n       python3-pandas+fss
Summary:        Metapackage for python3-pandas fss extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(fsspec) >= 2024.10.0
Provides:       python3dist(pandas[fss]) = %{version}-%{release}

%description -n python3-pandas+fss
Metapackage for python3-pandas fss extras.

%package -n       python3-pandas+aws
Summary:        Metapackage for python3-pandas aws extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(s3fs) >= 2024.10.0
Provides:       python3dist(pandas[aws]) = %{version}-%{release}

%description -n python3-pandas+aws
Metapackage for python3-pandas aws extras.

%package -n       python3-pandas+gcp
Summary:        Metapackage for python3-pandas gcp extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(gcsfs) >= 2024.10.0
Provides:       python3dist(pandas[gcp]) = %{version}-%{release}

%description -n python3-pandas+gcp
Metapackage for python3-pandas gcp extras.

%package -n       python3-pandas+excel
Summary:        Metapackage for python3-pandas excel extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(odfpy) >= 1.4.1
Requires:       python3dist(openpyxl) >= 3.1.5
Requires:       python3dist(python-calamine) >= 0.3.0
Requires:       python3dist(pyxlsb) >= 1.0.10
Requires:       python3dist(xlrd) >= 2.0.1
Requires:       python3dist(xlsxwriter) >= 3.2.0
Provides:       python3dist(pandas[excel]) = %{version}-%{release}

%description -n python3-pandas+excel
Metapackage for python3-pandas excel extras.

%package -n       python3-pandas+parquet
Summary:        Metapackage for python3-pandas parquet extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(pyarrow) >= 13.0.0
Provides:       python3dist(pandas[parquet]) = %{version}-%{release}

%description -n python3-pandas+parquet
Metapackage for python3-pandas parquet extras.

%package -n       python3-pandas+feather
Summary:        Metapackage for python3-pandas feather extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(pyarrow) >= 13.0.0
Provides:       python3dist(pandas[feather]) = %{version}-%{release}

%description -n python3-pandas+feather
Metapackage for python3-pandas feather extras.

%package -n       python3-pandas+iceberg
Summary:        Metapackage for python3-pandas iceberg extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(pyiceberg) >= 0.8.1
Provides:       python3dist(pandas[iceberg]) = %{version}-%{release}

%description -n python3-pandas+iceberg
Metapackage for python3-pandas iceberg extras.

%package -n       python3-pandas+hdf5
Summary:        Metapackage for python3-pandas hdf5 extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(tables) >= 3.10.1
Provides:       python3dist(pandas[hdf5]) = %{version}-%{release}

%description -n python3-pandas+hdf5
Metapackage for python3-pandas hdf5 extras.

%package -n       python3-pandas+spss
Summary:        Metapackage for python3-pandas spss extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(pyreadstat) >= 1.2.8
Provides:       python3dist(pandas[spss]) = %{version}-%{release}

%description -n python3-pandas+spss
Metapackage for python3-pandas spss extras.

%package -n       python3-pandas+postgresql
Summary:        Metapackage for python3-pandas postgresql extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(sqlalchemy) >= 2.0.36
Requires:       python3dist(psycopg2) >= 2.9.10
Requires:       python3dist(adbc-driver-postgresql) >= 1.2.0
Provides:       python3dist(pandas[postgresql]) = %{version}-%{release}

%description -n python3-pandas+postgresql
Metapackage for python3-pandas postgresql extras.

%package -n       python3-pandas+mysql
Summary:        Metapackage for python3-pandas mysql extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(sqlalchemy) >= 2.0.36
Requires:       python3dist(pymysql) >= 1.1.1
Provides:       python3dist(pandas[mysql]) = %{version}-%{release}

%description -n python3-pandas+mysql
Metapackage for python3-pandas mysql extras.

%package -n       python3-pandas+sql-other
Summary:        Metapackage for python3-pandas sql-other extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(sqlalchemy) >= 2.0.36
Requires:       python3dist(adbc-driver-postgresql) >= 1.2.0
Requires:       python3dist(adbc-driver-sqlite) >= 1.2.0
Provides:       python3dist(pandas[sql-other]) = %{version}-%{release}

%description -n python3-pandas+sql-other
Metapackage for python3-pandas sql-other extras.

%package -n       python3-pandas+html
Summary:        Metapackage for python3-pandas html extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(beautifulsoup4) >= 4.12.3
Requires:       python3dist(html5lib) >= 1.1
Requires:       python3dist(lxml) >= 5.3.0
Provides:       python3dist(pandas[html]) = %{version}-%{release}

%description -n python3-pandas+html
Metapackage for python3-pandas html extras.

%package -n       python3-pandas+xml
Summary:        Metapackage for python3-pandas xml extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(lxml) >= 5.3.0
Provides:       python3dist(pandas[xml]) = %{version}-%{release}

%description -n python3-pandas+xml
Metapackage for python3-pandas xml extras.

%package -n       python3-pandas+plot
Summary:        Metapackage for python3-pandas plot extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(matplotlib) >= 3.9.3
Provides:       python3dist(pandas[plot]) = %{version}-%{release}

%description -n python3-pandas+plot
Metapackage for python3-pandas plot extras.

%package -n       python3-pandas+output-formatting
Summary:        Metapackage for python3-pandas output-formatting extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(jinja2) >= 3.1.5
Requires:       python3dist(tabulate) >= 0.9.0
Provides:       python3dist(pandas[output-formatting]) = %{version}-%{release}

%description -n python3-pandas+output-formatting
Metapackage for python3-pandas output-formatting extras.

%package -n       python3-pandas+clipboard
Summary:        Metapackage for python3-pandas clipboard extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(pyqt5) >= 5.15.9
Requires:       python3dist(qtpy) >= 2.4.2
Provides:       python3dist(pandas[clipboard]) = %{version}-%{release}

%description -n python3-pandas+clipboard
Metapackage for python3-pandas clipboard extras.

%package -n       python3-pandas+compression
Summary:        Metapackage for python3-pandas compression extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(zstandard) >= 0.23.0
Provides:       python3dist(pandas[compression]) = %{version}-%{release}

%description -n python3-pandas+compression
Metapackage for python3-pandas compression extras.

%package -n       python3-pandas+timezone
Summary:        Metapackage for python3-pandas timezone extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(pytz) >= 2020.1
Provides:       python3dist(pandas[timezone]) = %{version}-%{release}

%description -n python3-pandas+timezone
Metapackage for python3-pandas timezone extras.

%package -n       python3-pandas+all
Summary:        Metapackage for python3-pandas all extras
Requires:       python3-pandas = %{version}-%{release}
Requires:       python3dist(adbc-driver-postgresql) >= 1.2.0
Requires:       python3dist(adbc-driver-sqlite) >= 1.2.0
Requires:       python3dist(beautifulsoup4) >= 4.12.3
Requires:       python3dist(bottleneck) >= 1.4.2
Requires:       python3dist(fastparquet) >= 2024.11.0
Requires:       python3dist(fsspec) >= 2024.10.0
Requires:       python3dist(gcsfs) >= 2024.10.0
Requires:       python3dist(html5lib) >= 1.1
Requires:       python3dist(hypothesis) >= 6.116.0
Requires:       python3dist(jinja2) >= 3.1.5
Requires:       python3dist(lxml) >= 5.3.0
Requires:       python3dist(matplotlib) >= 3.9.3
Requires:       python3dist(numba) >= 0.60.0
Requires:       python3dist(numexpr) >= 2.10.2
Requires:       python3dist(odfpy) >= 1.4.1
Requires:       python3dist(openpyxl) >= 3.1.5
Requires:       python3dist(psycopg2) >= 2.9.10
Requires:       python3dist(pyarrow) >= 13.0.0
Requires:       python3dist(pyiceberg) >= 0.8.1
Requires:       python3dist(pymysql) >= 1.1.1
Requires:       python3dist(pyqt5) >= 5.15.9
Requires:       python3dist(pyreadstat) >= 1.2.8
Requires:       python3dist(pytest) >= 8.3.4
Requires:       python3dist(pytest-xdist) >= 3.6.1
Requires:       python3dist(python-calamine) >= 0.3.0
Requires:       python3dist(pytz) >= 2020.1
Requires:       python3dist(pyxlsb) >= 1.0.10
Requires:       python3dist(qtpy) >= 2.4.2
Requires:       python3dist(scipy) >= 1.14.1
Requires:       python3dist(s3fs) >= 2024.10.0
Requires:       python3dist(sqlalchemy) >= 2.0.36
Requires:       python3dist(tables) >= 3.10.1
Requires:       python3dist(tabulate) >= 0.9.0
Requires:       python3dist(xarray) >= 2024.10.0
Requires:       python3dist(xlrd) >= 2.0.1
Requires:       python3dist(xlsxwriter) >= 3.2.0
Requires:       python3dist(zstandard) >= 0.23.0
Provides:       python3dist(pandas[all]) = %{version}-%{release}

%description -n python3-pandas+all
Metapackage for python3-pandas all extras.

%description

%package -n     python3-pandas
Summary:        Powerful data structures for data analysis, time series, and statistics
# oreon:reqs
Requires:       python3dist(numpy) >= 1.26.0
Requires:       python3dist(numpy) >= 2.3.3
Requires:       python3dist(python-dateutil) >= 2.8.2
# /oreon:reqs
%description -n python3-pandas

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%if %{with extras}
%endif

%prep
%global oreon_srcdir pandas-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pandas usr/lib/python3*/site-packages/pandas* usr/lib64/python3*/site-packages/pandas* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pandas* usr/lib64/python3*/site-packages/pandas* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pandas -f %{oreon_filedir}/python3-pandas.list

%changelog

%autochangelog
