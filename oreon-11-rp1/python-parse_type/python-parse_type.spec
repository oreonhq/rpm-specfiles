%global source0_hash 513a3784104839770d690e04339a8b4d33439fcd5dd99f2e4580f9fc1097bfb2
Name:           python-parse-type
Version:        0.6.6
Release:        1%{?dist}
Summary:        Simplifies to build parse types based on the parse module
License:        MIT
URL:            https://github.com/jenisys/parse_type
Source0:        https://files.pythonhosted.org/packages/source/p/parse_type/parse_type-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-parse-type = %{version}-%{release}
# /oreon:deps
%package -n       python3-parse-type+develop
Summary:        Metapackage for python3-parse-type develop extras
Requires:       python3-parse-type = %{version}-%{release}
Requires:       python3dist(build) >= 0.5.1
Requires:       python3dist(twine) >= 1.13.0
Requires:       python3dist(coverage) >= 4.4
Requires:       python3dist(pytest) < 5.0
Requires:       python3dist(pytest) >= 5.0
Requires:       python3dist(pytest-html) >= 1.19.0
Requires:       python3dist(tox) >= 2.8
Requires:       python3dist(tox) < 4.0
Requires:       python3dist(virtualenv) < 20.22.0
Requires:       python3dist(virtualenv) >= 20.0.0
Provides:       python3dist(parse-type[develop]) = %{version}-%{release}

%description -n python3-parse-type+develop
Metapackage for python3-parse-type develop extras.

%package -n       python3-parse-type+docs
Summary:        Metapackage for python3-parse-type docs extras
Requires:       python3-parse-type = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.6
Requires:       python3dist(sphinx-bootstrap-theme) >= 0.6.0
Provides:       python3dist(parse-type[docs]) = %{version}-%{release}

%description -n python3-parse-type+docs
Metapackage for python3-parse-type docs extras.

%package -n       python3-parse-type+testing
Summary:        Metapackage for python3-parse-type testing extras
Requires:       python3-parse-type = %{version}-%{release}
Requires:       python3dist(pytest) < 5.0
Requires:       python3dist(pytest) >= 5.0
Requires:       python3dist(pytest-html) >= 1.19.0
Provides:       python3dist(parse-type[testing]) = %{version}-%{release}

%description -n python3-parse-type+testing
Metapackage for python3-parse-type testing extras.

%description

%package -n     python3-parse-type
Summary:        Simplifies to build parse types based on the parse module
# oreon:reqs
Requires:       python3dist(parse) >= 1.13.1
Requires:       python3dist(parse) >= 1.18.0
Requires:       python3dist(six) >= 1.15
# /oreon:reqs
%description -n python3-parse-type

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir parse_type-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-parse-type usr/lib/python3*/site-packages/parse_type* usr/lib64/python3*/site-packages/parse_type* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/parse_type* usr/lib64/python3*/site-packages/parse_type* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-parse-type -f %{oreon_filedir}/python3-parse-type.list

%changelog

%autochangelog
