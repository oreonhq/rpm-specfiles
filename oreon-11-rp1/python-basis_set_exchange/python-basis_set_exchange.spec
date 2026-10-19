%global source0_hash bb26ef560cea0ac5631b66bfb46eb3accd5a2ac943738be5d7854c70cc8c2393
%{?!python3_pkgversion:%global python3_pkgversion 3}
Name:           python-basis_set_exchange
Version:        0.12
Release:        1%{?dist}
Summary:        A repository for quantum chemistry basis sets
License:        BSD-3-Clause
URL:            https://github.com/MolSSI-BSE/basis_set_exchange
Source0:        https://files.pythonhosted.org/packages/source/b/basis_set_exchange/basis_set_exchange-%{version}.tar.gz
BuildArch:      noarch
%{?python_enable_dependency_generator}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm) >= 8.0
Requires:       python3-basis_set_exchange = %{version}-%{release}
# /oreon:deps
%package -n       python3-basis_set_exchange+docs
Summary:        Metapackage for python3-basis_set_exchange docs extras
Requires:       python3-basis_set_exchange = %{version}-%{release}
Provides:       python3dist(basis_set_exchange[docs]) = %{version}-%{release}

%description -n python3-basis_set_exchange+docs
Metapackage for python3-basis_set_exchange docs extras.

%package -n       python3-basis_set_exchange+tests
Summary:        Metapackage for python3-basis_set_exchange tests extras
Requires:       python3-basis_set_exchange = %{version}-%{release}
Provides:       python3dist(basis_set_exchange[tests]) = %{version}-%{release}

%description -n python3-basis_set_exchange+tests
Metapackage for python3-basis_set_exchange tests extras.

%package -n       python3-basis_set_exchange+lint
Summary:        Metapackage for python3-basis_set_exchange lint extras
Requires:       python3-basis_set_exchange = %{version}-%{release}
Provides:       python3dist(basis_set_exchange[lint]) = %{version}-%{release}

%description -n python3-basis_set_exchange+lint
Metapackage for python3-basis_set_exchange lint extras.

%package -n       python3-basis_set_exchange+curate
Summary:        Metapackage for python3-basis_set_exchange curate extras
Requires:       python3-basis_set_exchange = %{version}-%{release}
Provides:       python3dist(basis_set_exchange[curate]) = %{version}-%{release}

%description -n python3-basis_set_exchange+curate
Metapackage for python3-basis_set_exchange curate extras.

%description
This project is a library containing basis sets for use in quantum
chemistry calculations. In addition, this library has functionality
for manipulation of basis set data.

The goal of this project is to create a consistent, thoroughly curated
database of basis sets, and to provide a standard nomenclature for
quantum chemistry.

The data contained within this library is being thoroughly evaluated
and checked against relevant literature, software implementations, and
other databases when available. The original data from the PNNL Basis
Set Exchange is also available.

This library is used to form the backend of the new Basis Set Exchange
website.

This project is a collaboration between the Molecular Sciences
Software Institute (https://molssi.org) and the Environmental
Molecular Sciences Laboratory (https://www.emsl.pnl.gov)

When publishing results obtained from use of the Basis Set Exchange
software, please cite:

* A New Basis Set Exchange: An Open, Up-to-date Resource for the
  Molecular Sciences Community Benjamin P. Pritchard, Doaa Altarawy,
  Brett Didier, Tara D. Gibson, and Theresa L. Windus
  J. Chem. Inf. Model. 2019, 59(11), 4814-4820
  doi:10.1021/acs.jcim.9b00725

For citing the previous EMSL/PNNL Basis Set Exchange, please cite the
following references:

* The Role of Databases in Support of Computational Chemistry
  Calculations, Feller, D., J. Comp. Chem. 1996, 17(13), 1571-1586,
  doi:10.1002/(SICI)1096-987X(199610)17:13<1571::AID-JCC9>3.0.CO;2-P
* Basis Set Exchange: A Community Database for Computational Sciences
  Schuchardt, K.L., Didier, B.T., Elsethagen, T., Sun, L.,
  Gurumoorthi, V., Chase, J., Li, J., and Windus,
  T.L. J. Chem. Inf. Model. 2007, 47(3), 1045-1052,
  doi:10.1021/ci600510

%package -n python%{python3_pkgversion}-basis_set_exchange
Summary:        A repository for quantum chemistry basis sets
%{?python_provide:%python_provide python3-basis_set_exchange}
%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
Requires:       python%{python3_pkgversion}-foo
%endif
%description -n python%{python3_pkgversion}-basis_set_exchange
This project is a library containing basis sets for use in quantum
chemistry calculations. In addition, this library has functionality
for manipulation of basis set data.

The goal of this project is to create a consistent, thoroughly curated
database of basis sets, and to provide a standard nomenclature for
quantum chemistry.

The data contained within this library is being thoroughly evaluated
and checked against relevant literature, software implementations, and
other databases when available. The original data from the PNNL Basis
Set Exchange is also available.

This library is used to form the backend of the new Basis Set Exchange
website.

This project is a collaboration between the Molecular Sciences
Software Institute (https://molssi.org) and the Environmental
Molecular Sciences Laboratory (https://www.emsl.pnl.gov)

When publishing results obtained from use of the Basis Set Exchange
software, please cite:

* A New Basis Set Exchange: An Open, Up-to-date Resource for the
  Molecular Sciences Community Benjamin P. Pritchard, Doaa Altarawy,
  Brett Didier, Tara D. Gibson, and Theresa L. Windus
  J. Chem. Inf. Model. 2019, 59(11), 4814-4820
  doi:10.1021/acs.jcim.9b00725

For citing the previous EMSL/PNNL Basis Set Exchange, please cite the
following references:

* The Role of Databases in Support of Computational Chemistry
  Calculations, Feller, D., J. Comp. Chem. 1996, 17(13), 1571-1586,
  doi:10.1002/(SICI)1096-987X(199610)17:13<1571::AID-JCC9>3.0.CO;2-P
* Basis Set Exchange: A Community Database for Computational Sciences
  Schuchardt, K.L., Didier, B.T., Elsethagen, T., Sun, L.,
  Gurumoorthi, V., Chase, J., Li, J., and Windus,
  T.L. J. Chem. Inf. Model. 2007, 47(3), 1045-1052,
  doi:10.1021/ci600510j

%prep

%setup -q -n basis_set_exchange-%{version}
# Remove spurious files
find basis_set_exchange/data/ -name fix_template.py -delete
find basis_set_exchange/data/ -name move.py -delete
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/basis_set_exchange* usr/lib64/python3*/site-packages/basis_set_exchange* usr/bin/*

%check

%pytest
%files
%files -n python3-basis_set_exchange -f %{oreon_filedir}/python3-basis_set_exchange.list

%changelog

%autochangelog
