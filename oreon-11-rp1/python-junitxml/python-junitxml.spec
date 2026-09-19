%global source0_hash a5901127067ab7f3d11df30727368c129c69b3f5595c697daf4f5ed80b1baaa3

%global pypi_name junitxml

Name:           python-%{pypi_name}
Version:        0.7
Release:        44%{?dist}
Summary:        PyJUnitXML, a pyunit extension to output JUnit compatible XML

License:        LGPL-3.0-only
URL:            https://launchpad.net/pyjunitxml
Source0:        https://pypi.python.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel

%global _description\
PyJUnitXML\
==========\
A Python unittest TestResult that outputs JUnit\
compatible XML.

%description %_description

%package -n python3-%{pypi_name}
Summary: PyJUnitXML, a pyunit extension to output JUnit compatible XML
BuildRequires: python3-devel

%description -n python3-%{pypi_name}
PyJUnitXML
==========
A Python unittest TestResult that outputs JUnit
compatible XML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
rm -rf %{py3dir}
cp -a . %{py3dir}

%generate_buildrequires
%pyproject_buildrequires

%build
pushd %{py3dir}
%pyproject_wheel
popd

%install
pushd %{py3dir}
%pyproject_install
popd
mv %{buildroot}%{_bindir}/pyjunitxml %{buildroot}%{_bindir}/pyjunitxml-%{python3_version}
ln -s ./pyjunitxml-%{python3_version} %{buildroot}%{_bindir}/pyjunitxml-3

%files -n python3-%{pypi_name}
%doc COPYING
%{_bindir}/pyjunitxml-3
%{_bindir}/pyjunitxml-%{python3_version}
%{python3_sitelib}/*

%changelog
%autochangelog
