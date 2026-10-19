%global source0_hash 9f3986aa960419041aba9c76191746bdf2c342c95892acfbf6edb500ab006d31
Name:           python-stripe
Version:        15.6.1
Release:        1%{?dist}
Summary:        Python bindings for the Stripe API
License:        MIT
URL:            https://stripe.com/
Source0:        https://files.pythonhosted.org/packages/source/s/stripe/stripe-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-stripe = %{version}-%{release}
# /oreon:deps
%package -n       python3-stripe+async
Summary:        Metapackage for python3-stripe async extras
Requires:       python3-stripe = %{version}-%{release}
Provides:       python3dist(stripe[async]) = %{version}-%{release}

%description -n python3-stripe+async
Metapackage for python3-stripe async extras.

%description

%package -n     python3-stripe
Summary:        Python bindings for the Stripe API
# oreon:reqs
Requires:       python3dist(requests) >= 2.20
Requires:       python3dist(typing-extensions) >= 4.7.0
# /oreon:reqs
%description -n python3-stripe

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir stripe-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-stripe usr/lib/python3*/site-packages/stripe* usr/lib64/python3*/site-packages/stripe* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/stripe* usr/lib64/python3*/site-packages/stripe* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-stripe -f %{oreon_filedir}/python3-stripe.list

%changelog

%autochangelog
