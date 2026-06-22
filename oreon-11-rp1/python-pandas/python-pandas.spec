%global source0_hash 1e262a8eedefc1a258f6009554fca7153f1af9dcce1bae5d7f06ce10bf1bda37

# We need to break some cycles with optional dependencies for bootstrapping;
# given that a conditional is needed, we take the opportunity to omit as many
# optional dependencies as possible for bootstrapping.
%bcond_with bootstrap

# When not bootstrapping, run tests?
%bcond_without tests
%{?with_bootstrap:%undefine with_tests}
# Upstream excludes the following markers:
# 'not slow and not network and not clipboard and not single_cpu'
# Let's follow suit
# When running tests, run ones that are marked as slow?
%bcond_with slow_tests
# When running tests, run ones that cannot be run in parallel?
%bcond_with single_tests

Name:           python-pandas
Version:        2.3.3
Release:        1%{?dist}
Summary:        Python library providing high-performance data analysis tools

# Drop support for i686 in preparation for `libarrow`
# https://bugzilla.redhat.com/show_bug.cgi?id=2263999
ExcludeArch:    %{ix86}

# The entire source is BSD-3-Clause and covered by LICENSE, except:
#
# - pandas/util/version/__init__.py is (Apache-2.0 OR BSD-2-Clause): see
#   LICENSES/PACKAGING_LICENSE
# - pandas/_libs/src/headers/portable.h is (BSD-3-Clause AND MIT), because it
#   contains some trivial content under the overall BSD-3-Clause license but
#   also some macros from MUSL libc under the MIT license: see
#   LICENSES/MUSL_LICENSE
# - pandas/_libs/src/parser/tokenizer.c is (BSD-3-Clause AND Python-2.0.1): see
#   LICENSES/PSF_LICENSE
# - pandas/io/sas/sas7bdat.py is (BSD-3-Clause and MIT), because it is mostly
#   under the overall BSD-3-Clause license but is also based on
#   https://bitbucket.org/jaredhobbs/sas7bdat: see LICENSES/SAS7BDAT_LICENSE
# - pandas/core/accessor.py is (BSD-3-Clause AND Apache-2.0), because it is
#   partially under the overall BSD-3-Clause license but is also based on
#   xarray: see LICENSES/XARRAY_LICENSE
# - pandas/_libs/src/klib/khash.h is MIT: see LICENSES/KLIB_LICENSE
# - pandas/_libs/window/aggregations.pyx is (BSD-3-Clause AND BSD-2-Clause):
#   see “Bottleneck license” in LICENSES/OTHER
#
# In the python3-pandas+test subpackage:
#
# - pandas/tests/io/data/spss/*.sav are MIT: see LICENSES/HAVEN_LICENSE and
#   LICENSES/HAVEN_MIT
# - pandas/tests/window/test_rolling.py is (BSD-3-Clause AND BSD-2-Clause)
#   since test_rolling_std_neg_sqrt is from Bottleneck: see “Bottleneck license”
#   in LICENSES/OTHER
#
# Additionally:
#
# - pandas/_libs/tslibs/parsing.pyx is BSD-3-Clause rather than
#   (BSD-3-Clause AND (BSD-3-Clause OR Apache-2.0)), because it appears that at
#   least some trivial content in the code copied from dateutil in the
#   dateutil_parse() function (as of
#   https://github.com/dateutil/dateutil/pull/732) is by dateutil contributors
#   who have not agreed to re-license their previously submitted code: see
#   LICENSES/DATEUTIL_LICENSE.
# - LICENSES/OTHER suggests that some code may be derived from
#   google-api-python-client under Apache-2.0, but a search for attribution
#   comments did not turn up anything specific
# - pandas/_libs/tslibs/src/datetime/np_datetime.{h,c} are still BSD-3-Clause,
#   but see also LICENSES/NUMPY_LICENSE
# - pandas/io/clipboard/ is still BSD-3-Clause, but see also “Pyperclip v1.3
#   license” in LICENSES/OTHER
# - pandas/_testing/__init__.py is still BSD-3-Clause, but see also
#   LICENSES/SCIPY_LICENSE
# - pandas/_libs/src/ujson/lib/ is still BSD-3-Clause, but under
#   LICENSES/ULTRAJSON_LICENSE
#
# Additionally, the following are not packaged and so do not affect the overall
# License field:
#
# - scripts/no_bool_in_generic.py is MIT: see LICENSES/PYUPGRADE_LICENSE
License:        BSD-3-Clause AND (Apache-2.0 OR BSD-2-Clause) AND (BSD-3-Clause AND Apache-2.0) AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause AND Python-2.0.1) AND MIT AND (BSD-3-Clause AND BSD-2-Clause)
URL:            https://pandas.pydata.org/
# The GitHub archive contains tests; the PyPI sdist does not.
Source0:        https://github.com/pandas-dev/pandas/archive/v%{version}/pandas-%{version}.tar.gz
# https://github.com/pandas-dev/pandas/pull/57389
Patch:          0001-TST-Ensure-Matplotlib-is-always-cleaned-up.patch
# Fix big-endian issues:
# https://github.com/pandas-dev/pandas/pull/57393
Patch:          0003-TST-Fix-IntervalIndex-constructor-tests-on-big-endia.patch
# https://github.com/pandas-dev/pandas/issues/57373
# https://github.com/pandas-dev/pandas/pull/57394
Patch:          0004-TST-Fix-test_str_encode-on-big-endian-machines.patch
# Patches for fixing tests due to changes/bugs in dependencies
# (not yet submitted upstream)
Patch:          0005-Use-zoneinfo-instead-of-pytz.patch
Patch:          0006-Adjust-test-to-accomodate-changes-in-Python.patch
Patch:          0007-Replace-deprecated-xarray.cftime_range.patch
# Fix build with Cython 3.2
# Resolved upstream: https://github.com/pandas-dev/pandas/pull/62832
Patch:          0008-Fix-Cython-3.2-build.patch

%global _description %{expand:
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data
analysis tools for the Python programming language.}

%description %_description


%package -n python3-pandas
Summary:        %{summary}

# pandas/_libs/window/aggregations.pyx:
#
#   Moving maximum / minimum code taken from Bottleneck under the terms
#   of its Simplified BSD license
#   https://github.com/pydata/bottleneck
#
# These snippets are extracted from Bottleneck’s internals and cannot be
# replaced by calling the public Bottleneck API, so there is no reasonable path
# to unbundling.
Provides:       bundled(python3dist(bottleneck))

# pandas/_libs/tslibs/parsing.pyx:
#
# Contains a routine, dateutil_parse(), from an unspecified version of dateutil
#
# Cannot be unbundled because the function is forked and compiled as Cython
Provides:       bundled(python3dist(dateutil))

# pandas/_libs/src/klib/khash.h:
#
# From klib (https://github.com/attractivechaos/klib); it is not practical to
# package all of klib separately because it is designed as a copylib, and many
# of its components are not header-only.
Provides:       bundled(klib-khash) = 0.2.6

# pandas/_libs/src/headers/portable.h:
#
# Contains several preprocessor macros from an unspecified version of MUSL libc
#
# Cannot be unbundled because the macros are not directly exposed in the libc
Provides:       bundled(musl-libc)

# pandas/_libs/tslibs/src/datetime/np_datetime.{h,c}:
#
# Derived from Numpy 1.7
#
# Cannot be unbundled because the routines are forked.
Provides:       bundled(python3dist(numpy)) = 1.7

# pandas/util/version/__init__.py:
#
# Vendored from https://github.com/pypa/packaging/blob/main/packaging/_structures.py
# and https://github.com/pypa/packaging/blob/main/packaging/_structures.py
# changeset ae891fd74d6dd4c6063bb04f2faeadaac6fc6313
# 04/30/2021
#
# Cannot be (reasonably) unbundled because the vendored file is not part of
# packaging’s public API.
Provides:       bundled(python3dist(packaging)) = 20.10.dev0^20210430gitae891fd

# pandas/io/clipboard/:
#
# In https://github.com/pandas-dev/pandas/pull/28471, upstream considered and
# rejected the idea of de-vendoring pyperclip. Furthermore,
# https://github.com/pandas-dev/pandas/commits/main/pandas/io/clipboard and
# https://github.com/pandas-dev/pandas/commits/main/pandas/io/clipboard/__init__.py
# show that the vendored library has accrued Pandas-specific changes.
#
# Version number from:
# https://github.com/pandas-dev/pandas/pull/28471/commits/33cd2d72e0c007c460e59105efda9211441b2ce4
# “Updated internal pyperclip 1.5.27 -> 1.7.0”
Provides:       bundled(python3dist(pyperclip)) = 1.7.0

# pandas/_libs/src/parser/tokenizer.c:
#
# Combines some elements from Python's built-in csv module and Warren
# Weckesser's textreader project on GitHub.
#
# Elements from these are both forked and cannot be unbundled. The textreader
# project is a Python extension but is not on PyPI, and is not the same as
# python3dist(textreader).
Provides:       bundled(python3-libs)
Provides:       bundled(textreader)

# scripts/no_bool_in_generic.py:
#
# The function `visit` is adapted from a function by the same name in pyupgrade:
# https://github.com/asottile/pyupgrade/blob/5495a248f2165941c5d3b82ac3226ba7ad1fa59d/pyupgrade/_data.py#L70-L113
#
# Not packaged (pre-commit hook) therefore not bundled
# Provides:       bundled(python3dist(pyupgrade)) = 2.11.0^20210201git5495a24

# pandas/io/sas/sas7bdat.py
#
# Based on code written by Jared Hobbs:
#   https://bitbucket.org/jaredhobbs/sas7bdat
#
# Cannot be unbundled because the code is modified, not directly copied
Provides:       bundled(python3dist(sas7bdat))

# pandas/_testing/__init__.py: in _create_missing_idx():
#
#   below is cribbed from scipy.sparse
#
# Cannot be unbundled because only a few lines are copied, not a standalone
# function that we can call
Provides:       bundled(python3dist(scipy))

# pandas/_libs/src/ujson/lib/:
#
# This is a stripped-down copy of UltraJSON. It would be an obvious target for
# unbundling, except:
#
# - Pandas uses the C library API, but UltraJSON upstream does not support
#   building and installing it separately from the Python package.
# - In https://github.com/pandas-dev/pandas/issues/24711 it is suggested that
#   Pandas might rely on features of the particular vendored version of
#   UltraJSON. It’s not immediately clear whether this is still true or not.
Provides:       bundled(python3dist(ujson))

# pandas/core/accessor.py
#
#   Ported with modifications from xarray
#   https://github.com/pydata/xarray/blob/master/xarray/core/extensions.py
#   1. We don't need to catch and re-raise AttributeErrors as RuntimeErrors
#   2. We use a UserWarning instead of a custom Warning
#
# Cannot be unbundled because the copied code is forked.
Provides:       bundled(python3dist(xarray))

BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  python3-devel

# Runtime dependencies
BuildRequires:  python3dist(numpy) >= 1.26
BuildRequires:  python3dist(python-dateutil) >= 2.8.2

%if %{with tests}
# From the [test] extra
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
%endif

%if %{without bootstrap}

# doc/source/getting_started/install.rst “Recommended dependencies”
# Since these provide large speedups, we make them hard dependencies except
# during bootstrapping.
BuildRequires:  python3dist(numexpr) >= 2.8.4
Requires:       python3dist(numexpr) >= 2.8.4
BuildRequires:  python3dist(bottleneck) >= 1.3.6
Requires:       python3dist(bottleneck) >= 1.3.6

# doc/source/getting_started/install.rst “Optional dependencies”
# We BR all weak dependencies to ensure they are installable.

# Timezones
BuildRequires:  tzdata >= 2022g
Recommends:     tzdata >= 2022g

# Visualization
BuildRequires:  python3dist(matplotlib) >= 3.6.3
Recommends:     python3dist(matplotlib) >= 3.6.3
BuildRequires:  python3dist(jinja2) >= 3.1.2
Recommends:     python3dist(jinja2) >= 3.1.2
BuildRequires:  python3dist(tabulate) >= 0.9
Recommends:     python3dist(tabulate) >= 0.9

# Computation
BuildRequires:  python3dist(scipy) >= 1.10
Recommends:     python3dist(scipy) >= 1.10
# python-numba is not currently packaged:
# BuildRequires:  python3dist(numba) >= 0.56.4
# Recommends:     python3dist(numba) >= 0.56.4
# Some tests from generic/test_to_xarray.py fail with xarray > 2024.9.0
# It's an optional dependency. Not build requiring it will skip tests.
# BuildRequires:  python3dist(xarray) >= 2022.12.0
Recommends:     python3dist(xarray) >= 2022.12.0

# Excel files
BuildRequires:  python3dist(xlrd) >= 2.0.1
Recommends:     python3dist(xlrd) >= 2.0.1
BuildRequires:  python3dist(xlsxwriter) >= 3.0.5
Recommends:     python3dist(xlsxwriter) >= 3.0.5
BuildRequires:  python3dist(openpyxl) >= 3.1
Recommends:     python3dist(openpyxl) >= 3.1
# python-calamine is not currently packaged:
# BuildRequires:  python3dist(python-calamine) >= 0.1.7
# Recommends:     python3dist(python-calamine) >= 0.1.7
# python-pyxlsb is not currently packaged:
# BuildRequires:  python3dist(pyxlsb) >= 1.0.10
# Recommends:     python3dist(pyxlsb) >= 1.0.10
# Not in doc/source/getting_started/install.rst, but in environment.yml and in
# some doc-strings:
BuildRequires:  python3dist(odfpy) >= 1.4.1
Recommends:     python3dist(odfpy) >= 1.4.1

# HTML
BuildRequires:  python3dist(beautifulsoup4) >= 4.11.2
Recommends:     python3dist(beautifulsoup4) >= 4.11.2
BuildRequires:  python3dist(html5lib) >= 1.1
Recommends:     python3dist(html5lib) >= 1.1
# lxml handled below:

# XML
BuildRequires:  python3dist(lxml) >= 4.9.2
Recommends:     python3dist(lxml) >= 4.9.2

# SQL databases
BuildRequires:  python3dist(sqlalchemy) >= 2
Recommends:     python3dist(sqlalchemy) >= 2
BuildRequires:  python3dist(psycopg2) >= 2.9.6
Recommends:     python3dist(psycopg2) >= 2.9.6
BuildRequires:  python3dist(pymysql) >= 1.0.2
Recommends:     python3dist(pymysql) >= 1.0.2

# Other data sources
%if 0%{?__isa_bits} != 32
# blosc2 does not support 32-bit architectures:
BuildRequires:  python3dist(tables) >= 3.8
Recommends:     python3dist(tables) >= 3.8
%endif
# Dependencies on blosc and zlib are indirect, via PyTables, so we do not
# encode them here. Note also that the minimum blosc version in the
# documentation seems to be that of the blosc C library, not of the blosc PyPI
# package.
# python-fastparquet is not currently packaged:
# BuildRequires:  python3dist(fastparquet) >= 2022.12.0
# Recommends:     python3dist(fastparquet) >= 2022.12.0
# libarrow does not support 32-bit architectures:
%if 0%{?__isa_bits} != 32
BuildRequires:  python3dist(pyarrow) >= 10.0.1
Recommends:     python3dist(pyarrow) >= 10.0.1
%endif
# python-pyreadstat is not currently packaged:
# BuildRequires:  python3dist(pyreadstat) >= 1.2
# Recommends:     python3dist(pyreadstat) >= 1.2

# Access data in the cloud
BuildRequires:  python3dist(fsspec) >= 2022.11
Recommends:     python3dist(fsspec) >= 2022.11
BuildRequires:  python3dist(gcsfs) >= 2022.11
Recommends:     python3dist(gcsfs) >= 2022.11
# python-pandas-gbq is not currently packaged:
# BuildRequires:  python3dist(pandas-gbq) >= 0.19
# Recommends:     python3dist(pandas-gbq) >= 0.19
# python-s3fs is not currently packaged:
# BuildRequires:  python3dist(s3fs) >= 2022.11
# Recommends:     python3dist(s3fs) >= 2022.11

# Clipboard
BuildRequires:  python3dist(pyqt5)
Recommends:     python3dist(pyqt5)
BuildRequires:  python3dist(qtpy)
Recommends:     python3dist(qtpy)
BuildRequires:  xclip
Recommends:     xclip
BuildRequires:  xsel
Recommends:     xsel

# Compression
BuildRequires:  python3dist(zstandard) >= 0.19
Recommends:     python3dist(zstandard) >= 0.19

# This is just an “ecosystem” package in the upstream documentation, but there
# is an integration test for it. This package historically had a weak
# dependency on it, but this was unnecessary.
BuildRequires:  python3dist(pandas-datareader)

%endif

%description -n python3-pandas %_description


%package -n python3-pandas+test
Summary:        Tests and test extras for Pandas

# See comment above base package License tag for licensing breakdown.
License:        BSD-3-Clause AND MIT

Requires:       python3-pandas%{?_isa} = %{version}-%{release}

%if %{without bootstrap}

# Additional BR’s and weak dependencies below are generally those that don’t
# provide enough added functionality to be weak dependencies of the library
# package, but for which there is some integration support and additional tests
# that can be enabled.

# Additional dependencies from environment.yml: “testing”
# Those not in the “test” extra are treated as weak dependencies for the tests.
BuildRequires:  python3dist(boto3)
Recommends:     python3dist(boto3)
BuildRequires:  python3dist(botocore) >= 1.11
Recommends:     python3dist(botocore) >= 1.11
# Already covered by “test” extra
# BuildRequires:  python3dist(hypothesis) >= 3.82
# Recommends:     python3dist(hypothesis) >= 3.82
# python-moto is not yet packaged
# BuildRequires:  python3dist(moto)
# Recommends:     python3dist(moto)
BuildRequires:  python3dist(flask)
Recommends:     python3dist(flask)
# Already covered by “test” extra
# BuildRequires:  python3dist(pytest) >= 5.0.1
# Requires:       python3dist(pytest) >= 5.0.1
# Already covered by “test” extra
# BuildRequires:  python3dist(pytest-xdist) >= 1.21
# Requires:       python3dist(pytest-xdist) >= 1.21
BuildRequires:  python3dist(pytest-asyncio)
Recommends:     python3dist(pytest-asyncio)
# python-pytest-instafail is not yet packaged
# BuildRequires:  python3dist(pytest-instafail)
# Recommends:     python3dist(pytest-instafail)

# Additional dependencies from environment.yml:
# “Dask and its dependencies (that dont install with dask)”
# Asks for dask-core, but we just have dask
BuildRequires:  python3dist(dask)
Recommends:     python3dist(dask)
BuildRequires:  python3dist(toolz) >= 0.7.3
Recommends:     python3dist(toolz) >= 0.7.3
BuildRequires:  python3dist(partd) >= 0.3.10
Recommends:     python3dist(partd) >= 0.3.10
BuildRequires:  python3dist(cloudpickle) >= 0.2.1
Recommends:     python3dist(cloudpickle) >= 0.2.1

# Additional dependencies from environment.yml: “downstream tests”
BuildRequires:  python3dist(seaborn)
Recommends:     python3dist(seaborn)
BuildRequires:  python3dist(statsmodels)
Recommends:     python3dist(statsmodels)

# environment.yml: Needed for downstream xarray.CFTimeIndex test
BuildRequires:  python3dist(cftime)
Recommends:     python3dist(cftime)

# environment.yml: optional
BuildRequires:  python3dist(ipython) >= 7.11.1
Recommends:     python3dist(ipython) >= 7.11.1

# pandas/tests/io/data/spss/*.sav:
#
# From Haven
Provides:       bundled(R-haven)

# pandas/tests/window/test_rolling.py: test_rolling_std_neg_sqrt()
#
#   unit test from Bottleneck
#
# There is no reasonable path to unbundling a single unit test.
Provides:       bundled(python3dist(bottleneck))

%endif


%description -n python3-pandas+test
These are the tests for python3-pandas. This package:

• Provides the “pandas.tests” package
• Makes sure the “test” extra dependencies are installed
• Carries additonal weak dependencies for running the tests


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n pandas-%{version} -p1

# Let versioneer know what version this is
echo '__version__="%{version}"' > _version_meson.py

# Ensure Cython-generated sources are re-generated
rm -vf $(grep -rl '/\* Generated by Cython')

# We just want to build with the numpy in Fedora:
sed -r -i '/\boldest-supported-numpy\b/d' pyproject.toml

# We don't need the python tzdata package because we have the system tzdata package
sed -i '/tzdata>=2022.7/d' pyproject.toml

# Unpin meson
sed -i 's/meson-python==0.13.1/meson-python>=0.13.1/' pyproject.toml
sed -i 's/meson==1.2.1/meson>=1.2.1/' pyproject.toml

# Unpin Cython
sed -i 's/Cython~=3.0.5/Cython>=3.0.5/' pyproject.toml

%generate_buildrequires
# the build is expensive, so we don't use -w
# we list the runtime and test BuildRequires manually
%pyproject_buildrequires -R


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pandas


%check
%if %{with tests}
m="${m-}${m+ and }not network"
m="${m-}${m+ and }not db"
%if %{without slow_tests}
m="${m-}${m+ and }not slow"
%endif
# Clipboard tests don’t run without a graphical session, and it’s not worth
# using xvfb-run just for them.
m="${m-}${m+ and }not clipboard"
%if %{without single_tests}
m="${m-}${m+ and }not single_cpu"
%endif

# This test allocates a huge amount of memory (~12GB), which causes flaky OOM
# failures on some builders. It’s not worth it.
# https://github.com/pandas-dev/pandas/issues/45223#issuecomment-1250912663
k="${k-}${k+ and }not test_bytes_exceed_2gb"

# This test (only) expects the current working directory to be the
# site-packages directory containing the built pandas. This is not how we run
# the tests, because we don’t want to clutter the buildroot with
# testing-related hidden files and directories. We could run tests from
# %%pyproject_build_lib if this were a problem for a lot of tests, but it’s
# easier just to skip it.
k="${k-}${k+ and }not test_html_template_extends_options"

# Those tests started failing as of 2024-04-12. Not sure why, though.
# Dask wasn't updated at the time.
# > return get(descriptor, obj, type(obj))
# E   TypeError: descriptor '__call__' for 'type' objects doesn't apply to a 'property' object
# and
# [XPASS(strict)] pyarrow doesn't support this
k="${k-}${k+ and }not test_dask"
k="${k-}${k+ and }not test_construct_dask_float_array"
k="${k-}${k+ and }not test_multi_thread_string_io_read_csv[pyarrow]"

# Two tests started failing with matplotlib >= 3.9.0
# E   matplotlib._api.deprecation.MatplotlibDeprecationWarning:
# The plot_date function was deprecated in Matplotlib 3.9
# and will be removed in 3.11. Use plot instead.
#
# E   UserWarning: No artists with labels found to put in legend.
# Note that artists whose label start with an underscore are ignored
# when legend() is called with no argument.
k="${k-}${k+ and }not test_mpl_nopandas"
k="${k-}${k+ and }not test_plot_scatter_shape"

%ifarch %{ix86}
# These failures are i686-specific; most are likely 32-bit issues. It’s not
# really worth trying to fix them.

# E   AssertionError: DataFrame.iloc[:, 2] (column name="C") are different
# E
# E   DataFrame.iloc[:, 2] (column name="C") values are different (11.66363 %)
# E   [index]: [0, 1, …
# Fails for [left], [right], [outer], and [inner]
k="${k-}${k+ and }not (TestMerge and test_int64_overflow_how_merge)"

# E       AssertionError: DataFrame.index are different
# E
# E       Attribute "dtype" are different
# E       [left]:  int32
# E       [right]: int64
k="${k-}${k+ and }not (TestMerge and test_int64_overflow_sort_false_order)"

# E           AssertionError: Attributes of DataFrame.iloc[:, 1] (column name="b") are different
# E
# E           Attribute "dtype" are different
# E           [left]:  int32
# E           [right]: int64
k="${k-}${k+ and }not test_frame_setitem_dask_array_into_new_col"

# E       IndexError: index 0 is out of bounds for axis 0 with size 0
k="${k-}${k+ and }not (TestPivotTable and test_pivot_number_of_levels_larger_than_int32)"
k="${k-}${k+ and }not (TestStackUnstackMultiLevel and test_unstack_number_of_levels_larger_than_int32)"

# [XPASS(strict)] Floating point error
k="${k-}${k+ and }not (TestTimedeltas and test_to_timedelta_float)"
%endif

%ifarch s390x
# Note that pandas does not test big-endian support but will happily accept
# patches to improve it:
# https://github.com/pandas-dev/pandas/issues/4737#issuecomment-1090931741

# TODO: Why does this fail?
#
# >                   os.fsync(self._handle.fileno())
# E                   OverflowError: Python int too large to convert to C int
k="${k-}${k+ and }not test_flush"

# TODO: Why does this fail? The differences are large!
k="${k-}${k+ and }not test_rolling_var_numerical_issues"

# These are a cluster of similar pyarrow/parquet tests with apparent endianness
# issues. It is not immediately obvious where the bug is—in the library or in
# the tests?
k="${k-}${k+ and }not (TestBasic and test_dtype_backend[pyarrow])"
k="${k-}${k+ and }not (TestBasic and test_multiindex_with_columns)"
k="${k-}${k+ and }not (TestBasic and test_write_column_index_nonstring[pyarrow])"
k="${k-}${k+ and }not (TestBasic and test_write_column_index_string)"
k="${k-}${k+ and }not (TestBasic and test_write_column_multiindex[pyarrow])"
k="${k-}${k+ and }not (TestBasic and test_write_column_multiindex_nonstring[pyarrow])"
k="${k-}${k+ and }not (TestBasic and test_write_column_multiindex_string)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_basic)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_to_bytes_without_path_or_buf_provided)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_categorical)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_additional_extension_arrays)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_pyarrow_backed_string_array[python])"
k="${k-}${k+ and }not (TestParquetPyArrow and test_pyarrow_backed_string_array[pyarrow])"
k="${k-}${k+ and }not (TestParquetPyArrow and test_additional_extension_types)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_infer_string_large_string_type)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_read_dtype_backend_pyarrow_config)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_read_dtype_backend_pyarrow_config_index)"
k="${k-}${k+ and }not (TestParquetPyArrow and test_roundtrip_decimal)"
k="${k-}${k+ and }not test_to_read_gcs[parquet]"

# Similarly, there are a cluster of similar stata test failures for which the
# root cause is not immediately obvious.
k="${k-}${k+ and }not (TestStata and test_writer_117)"
k="${k-}${k+ and }not (TestStata and test_convert_strl_name_swap)"
k="${k-}${k+ and }not (TestStata and test_strl_latin1)"
# Fails for [118], [119], and [None]
k="${k-}${k+ and }not (TestStata and test_utf8_writer)"

# These crash, and are probably a blosc2 or PyTables issue.
k="${k-}${k+ and }not test_complibs[blosc2"

# Fails on s390x (rawhide)
k="${k-}${k+ and }not (TestParquetPyArrow and test_unsupported_float16)"
%endif


%ifarch x86_64
# These are brittle and fail with tiny floating-point differences on COPR
# builders but not Koji builders, like:
# >           raise_assert_detail(obj, msg, left, right, index_values=index_values)
# E           AssertionError: numpy array are different
# E
# E           numpy array values are different (16.66667 %)
# E           [left]:  [0.09999999999999999, 1.0, 10.0, 100.0, 1000.0, 10000.0]
# E           [right]: [0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0]
k="${k-}${k+ and }not (TestSeriesPlots and test_bar_log)"
k="${k-}${k+ and }not (TestDataFramePlotsSubplots and test_bar_log_no_subplots)"
k="${k-}${k+ and }not (TestDataFramePlotsSubplots and test_bar_log_subplots)"
%endif

# Ensure pytest doesn’t find the “un-built” library. We can get away with this
# approach because the tests are also in the installed library. We can’t simply
# “cd” to the buildroot’s python3_sitearch because testing leaves files in the
# current working directory.
mkdir -p _empty
cd _empty

# See: test_fast.sh
# Workaround for pytest-xdist flaky collection order
# https://github.com/pytest-dev/pytest/issues/920
# https://github.com/pytest-dev/pytest/issues/1075
export PYTHONHASHSEED="$(
  %{python3} -c 'import random; print(random.randint(1, 4294967295))'
)"

# Previously, we ran tests in parallel. Upstream seems to support this;
# however, in practice, there were still some flaky test failures that seem to
# be fixed by eschewing parallelism (-n 1).
#
# If we start running tests in parallel again in the future, note that on
# 32-bit platforms (%%if 0%%{?__isa_bits} == 32) it may be necessary to limit
# the number of concurrent tests to e.g. 8 in order to prevent memory
# exhaustion.
%pytest -v '%{buildroot}%{python3_sitearch}/pandas' \
    -o cache_dir="$PWD/pytest-cache" \
    --no-strict-data-files \
    -m "${m-}" \
    -k "${k-}" \
    -n 1 \
    -r sxX

%else
# Some imports require optional dependencies, and must be excluded during
# bootstrapping.
%{pyproject_check_import \
  %{?with_bootstrap:-e 'pandas.io.formats.style'} \
  %{?with_bootstrap:-e 'pandas.io.formats.style_render'} \
  %{?with_bootstrap:-e 'pandas.core.arrays.arrow.extension_types'} \
  -e 'pandas.conftest' \
  -e 'pandas.tests.*'}
%endif


%files -n python3-pandas -f %{pyproject_files}
# While pyproject_files automatically handles the LICENSE file in the Python
# package’s dist-info directory, we also want to package the entire LICENSES/
# directory to include third-party license text.  We include a second copy of
# the LICENSE file since it would be surprising to see a license directory for
# the package without the overall license file in it.
%license LICENSE LICENSES/
%doc README.md
%exclude %{python3_sitearch}/pandas/tests


%files -n python3-pandas+test
%{python3_sitearch}/pandas/tests
%ghost %{python3_sitearch}/*.dist-info


%changelog
%autochangelog
