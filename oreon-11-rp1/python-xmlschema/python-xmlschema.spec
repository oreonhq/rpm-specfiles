%global source0_hash f3b33a21a2b2cdc404ddc3fb599d8bc1dee90b155d547370672e6e684746b8d6
Name:           python-xmlschema
Version:        4.3.2
Release:        1%{?dist}
Summary:        An XML Schema validator and decoder
License:        MIT
URL:            https://github.com/sissaschool/xmlschema
Source0:        https://files.pythonhosted.org/packages/source/x/xmlschema/xmlschema-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-xmlschema = %{version}-%{release}
# /oreon:deps
%package -n       python3-xmlschema+codegen
Summary:        Metapackage for python3-xmlschema codegen extras
Requires:       python3-xmlschema = %{version}-%{release}
Provides:       python3dist(xmlschema[codegen]) = %{version}-%{release}

%description -n python3-xmlschema+codegen
Metapackage for python3-xmlschema codegen extras.

%package -n       python3-xmlschema+dev
Summary:        Metapackage for python3-xmlschema dev extras
Requires:       python3-xmlschema = %{version}-%{release}
Provides:       python3dist(xmlschema[dev]) = %{version}-%{release}

%description -n python3-xmlschema+dev
Metapackage for python3-xmlschema dev extras.

%package -n       python3-xmlschema+docs
Summary:        Metapackage for python3-xmlschema docs extras
Requires:       python3-xmlschema = %{version}-%{release}
Provides:       python3dist(xmlschema[docs]) = %{version}-%{release}

%description -n python3-xmlschema+docs
Metapackage for python3-xmlschema docs extras.

%description

%package -n     python3-xmlschema
Summary:        An XML Schema validator and decoder
# oreon:reqs
Requires:       python3dist(elementpath) < 6.0.0
Requires:       python3dist(elementpath) >= 5.1.3
# /oreon:reqs
%description -n python3-xmlschema

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir xmlschema-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xmlschema usr/lib/python3*/site-packages/xmlschema* usr/lib64/python3*/site-packages/xmlschema* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xmlschema* usr/lib64/python3*/site-packages/xmlschema* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xmlschema -f %{oreon_filedir}/python3-xmlschema.list

%changelog

%autochangelog
