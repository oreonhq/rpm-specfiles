%global source0_hash cd79f3367bd74b317dda655dc8fcfa304d9eb6e4fb06b7168c5cf27f96e0cd62

Name:           python-lxml
Version:        6.0.2
Release:        %autorelease
Summary:        XML processing library combining libxml2/libxslt with the ElementTree API

# The lxml project is licensed under BSD-3-Clause
# Some code is derived from ElementTree and cElementTree
# thus using the MIT-CMU elementtree license
# .xsl schematron files are under the MIT license
License:        BSD-3-Clause AND MIT-CMU AND MIT
URL:            https://github.com/lxml/lxml

# drop isoschematron rng (bad license), see fedora-license-data #154
Source0:        https://files.pythonhosted.org/packages/source/l/lxml/lxml-6.0.2.tar.gz

BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  python3-devel

# Some of the extras create a build dependency loop.
# - [cssselect] Requires cssselect BuildRequires lxml
# - [html5] Requires html5lib BuildRequires lxml
# - [htmlsoup] Requires beautifulsoup4 Requires lxml
# - [html_clean] Requires lxml-html-clean Requires lxml
# Hence we provide a bcond to disable the extras altogether.
# By default, the extras are disabled in RHEL, to avoid dependencies.
%bcond extras %{undefined rhel}

%global _description \
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries. It\
provides safe and convenient access to these libraries using the ElementTree It\
extends the ElementTree API significantly to offer support for XPath, RelaxNG,\
XML Schema, XSLT, C14N and much more.

%description %{_description}

%package -n     python3-lxml
Summary:        %{summary}
%if %{with extras}
Suggests:       python3-lxml+cssselect
Suggests:       python3-lxml+html5
Suggests:       python3-lxml+htmlsoup
Suggests:       python3-lxml+html_clean
%endif

%description -n python3-lxml %{_description}

Python 3 version.

%if %{with extras}
%pyproject_extras_subpkg -n python3-lxml cssselect html5 htmlsoup html_clean
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n lxml-%{version} -p1
rm -rf src/lxml/isoschematron/resources/rng
# Don't run html5lib tests --without extras
%{!?without_extras:rm src/lxml/html/tests/test_html5parser.py}

# Remove limit for version of Cython
sed -i "s/Cython.*/Cython/" requirements.txt
sed -i 's/"Cython.*",/"Cython",/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x source%{?with_extras:,cssselect,html5,htmlsoup,html_clean}

%build
# Remove pregenerated Cython C sources
# We need to do this after %%pyproject_buildrequires because setup.py errors
# without Cython and without the .c files.
find -type f -name '*.c' -print -delete >&2
export WITH_CYTHON=true
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lxml

%check
# The tests assume inplace build, so we copy the built library to source-dir.
# If not done that, Python can either import the tests or the extension modules, but not both.
cp -a build/lib.%{python3_platform}-*/* src/
# The options are: verbose, unit, functional
%{python3} test.py -vuf

%files -n python3-lxml -f %{pyproject_files}
%license doc/licenses/BSD.txt doc/licenses/elementtree.txt
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.2-1
- Prepare for Oreon 11 (RP1)
