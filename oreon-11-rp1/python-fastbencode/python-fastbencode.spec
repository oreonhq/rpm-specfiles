%global source0_hash 7e2be45bfe81167cd79986698a2cf270eaf61add5b1bc711378c2bb3f05396d5
Name:           python-fastbencode
Version:        0.3.11
Release:        1%{?dist}
Summary:        Implementation of bencode with optional fast Rust extensions
License:        Apache-2.0
URL:            https://github.com/breezy-team/fastbencode
Source0:        https://files.pythonhosted.org/packages/source/f/fastbencode/fastbencode-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-rust) >= 1.0.0
Requires:       python3-fastbencode = %{version}-%{release}
# /oreon:deps
%package -n       python3-fastbencode+rust
Summary:        Metapackage for python3-fastbencode rust extras
Requires:       python3-fastbencode = %{version}-%{release}
Requires:       python3dist(setuptools-rust) >= 1.0.0
Provides:       python3dist(fastbencode[rust]) = %{version}-%{release}

%description -n python3-fastbencode+rust
Metapackage for python3-fastbencode rust extras.

%package -n       python3-fastbencode+dev
Summary:        Metapackage for python3-fastbencode dev extras
Requires:       python3-fastbencode = %{version}-%{release}
Requires:       python3dist(ruff) == 0.16.0
Provides:       python3dist(fastbencode[dev]) = %{version}-%{release}

%description -n python3-fastbencode+dev
Metapackage for python3-fastbencode dev extras.

%description

%package -n     python3-fastbencode
Summary:        Implementation of bencode with optional fast Rust extensions
%description -n python3-fastbencode

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fastbencode-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fastbencode usr/lib/python3*/site-packages/fastbencode* usr/lib64/python3*/site-packages/fastbencode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastbencode* usr/lib64/python3*/site-packages/fastbencode* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fastbencode -f %{oreon_filedir}/python3-fastbencode.list

%changelog

%autochangelog
