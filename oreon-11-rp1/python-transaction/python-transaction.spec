%global source0_hash f6ca8639a3e54f6991de0d9c0983a7cd91acb21a825cb544c168269be956bd41
Name:           python-transaction
Version:        5.1
Release:        1%{?dist}
Summary:        Transaction management for Python
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/transaction
Source0:        https://files.pythonhosted.org/packages/source/t/transaction/transaction-%{version}.tar.gz
BuildArch:      noarch
Patch1:         transaction-no-explicit-setuptools-req.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 81
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-transaction = %{version}-%{release}
# /oreon:deps
%package -n       python3-transaction+docs
Summary:        Metapackage for python3-transaction docs extras
Requires:       python3-transaction = %{version}-%{release}
Provides:       python3dist(transaction[docs]) = %{version}-%{release}

%description -n python3-transaction+docs
Metapackage for python3-transaction docs extras.

%package -n       python3-transaction+testing
Summary:        Metapackage for python3-transaction testing extras
Requires:       python3-transaction = %{version}-%{release}
Provides:       python3dist(transaction[testing]) = %{version}-%{release}

%description -n python3-transaction+testing
Metapackage for python3-transaction testing extras.

%description

%package -n     python3-transaction
Summary:        Transaction management for Python
%description -n python3-transaction

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir transaction-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-transaction usr/lib/python3*/site-packages/transaction* usr/lib64/python3*/site-packages/transaction* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/transaction* usr/lib64/python3*/site-packages/transaction* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-transaction -f %{oreon_filedir}/python3-transaction.list

%changelog

%autochangelog
