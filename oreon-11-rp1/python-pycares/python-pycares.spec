%global source0_hash 6b80a9824a15eff719d8dca261a90e86e60c57d01dbb941aabbcb4a505152308

# set upstream name variable
%global srcname pycares

Name:           python-pycares
Version:        5.0.1
Release:        2%{?dist}
Summary:        Python interface for c-ares

License:        MIT
URL:            https://github.com/saghul/pycares
Source0:        https://github.com/saghul/%{srcname}/archive/v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  c-ares-devel
# for docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# for tests
#BuildRequires:  python3-pytest

%description
pycares is a Python module which provides an interface to
c-ares. c-ares is a C library that performs DNS requests and name
resolutions asynchronously.

%package     -n python3-%{srcname}
Summary:        Python interface for c-ares

%description -n python3-%{srcname}
pycares is a Python module which provides an interface to
c-ares. c-ares is a C library that performs DNS requests and name
resolutions asynchronously.

%package     -n python-%{srcname}-doc
Summary:        Documentation for python-pycares
BuildArch:      noarch
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n python-%{srcname}-doc
pycares is a Python module which provides an interface to
c-ares. c-ares is a C library that performs DNS requests and name
resolutions asynchronously.

This package contains documentation in reST and HTML formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
export PYCARES_USE_SYSTEM_LIB=1
%pyproject_wheel

# Build sphinx documentation
pushd docs/
make html
popd # docs

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

# Install html docs
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -pr docs/_build/html %{buildroot}%{_pkgdocdir}/

# Move sources
mv -f %{buildroot}%{_pkgdocdir}/html/_sources/ %{buildroot}%{_pkgdocdir}/rst/

# Remove buildinfo sphinx documentation
rm -rf %{buildroot}%{_pkgdocdir}/html/.buildinfo

%check
%pyproject_check_import

# no tests to run with pytest: Disabling.

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst ChangeLog
# For arch-specific packages: sitearch

%files -n python-%{srcname}-doc
%doc examples/
%{_pkgdocdir}/

%changelog
%autochangelog
