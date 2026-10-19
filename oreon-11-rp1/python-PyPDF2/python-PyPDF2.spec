%global source0_hash a74408f69ba6271f71b9352ef4ed03dc53a31aa404d29b5d31f53bfecfee1440
Name:           python-pypdf2
Version:        3.0.1
Release:        1%{?dist}
Summary:        A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files
License:        ...
URL:            https://github.com/py-pdf/PyPDF2
Source0:        https://files.pythonhosted.org/packages/source/P/PyPDF2/PyPDF2-%{version}.tar.gz
BuildArch:      noarch
Patch01:        599.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-pypdf2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-pypdf2+full
Summary:        Metapackage for python3-pypdf2 full extras
Requires:       python3-pypdf2 = %{version}-%{release}
Provides:       python3dist(pypdf2[full]) = %{version}-%{release}

%description -n python3-pypdf2+full
Metapackage for python3-pypdf2 full extras.

%package -n       python3-pypdf2+crypto
Summary:        Metapackage for python3-pypdf2 crypto extras
Requires:       python3-pypdf2 = %{version}-%{release}
Provides:       python3dist(pypdf2[crypto]) = %{version}-%{release}

%description -n python3-pypdf2+crypto
Metapackage for python3-pypdf2 crypto extras.

%package -n       python3-pypdf2+image
Summary:        Metapackage for python3-pypdf2 image extras
Requires:       python3-pypdf2 = %{version}-%{release}
Provides:       python3dist(pypdf2[image]) = %{version}-%{release}

%description -n python3-pypdf2+image
Metapackage for python3-pypdf2 image extras.

%package -n       python3-pypdf2+dev
Summary:        Metapackage for python3-pypdf2 dev extras
Requires:       python3-pypdf2 = %{version}-%{release}
Requires:       python3dist(pre-commit) < 2.18.0
Provides:       python3dist(pypdf2[dev]) = %{version}-%{release}

%description -n python3-pypdf2+dev
Metapackage for python3-pypdf2 dev extras.

%package -n       python3-pypdf2+docs
Summary:        Metapackage for python3-pypdf2 docs extras
Requires:       python3-pypdf2 = %{version}-%{release}
Provides:       python3dist(pypdf2[docs]) = %{version}-%{release}

%description -n python3-pypdf2+docs
Metapackage for python3-pypdf2 docs extras.

%description

%package -n     python3-pypdf2
Summary:        A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 3.10.0.0
# /oreon:reqs
%description -n python3-pypdf2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir PyPDF2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pypdf2 usr/lib/python3*/site-packages/pypdf2* usr/lib64/python3*/site-packages/pypdf2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pypdf2* usr/lib64/python3*/site-packages/pypdf2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pypdf2 -f %{oreon_filedir}/python3-pypdf2.list

%changelog

%autochangelog
