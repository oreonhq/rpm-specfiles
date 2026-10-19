%global source0_hash 43e728e12aca2d897c626cf07dc7b4392749b73de050a7d66e086cb3a6e15da9
Name:           python-treq
Version:        26.7.0
Release:        1%{?dist}
Summary:        High-level Twisted HTTP Client API
License:        MIT
URL:            https://github.com/twisted/treq
Source0:        https://files.pythonhosted.org/packages/source/t/treq/treq-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(incremental) >= 24.7.2
Requires:       python3-treq = %{version}-%{release}
# /oreon:deps
%package -n       python3-treq+dev
Summary:        Metapackage for python3-treq dev extras
Requires:       python3-treq = %{version}-%{release}
Requires:       python3dist(httpbin) == 0.10.2
Requires:       python3dist(werkzeug) == 3.1.8
Provides:       python3dist(treq[dev]) = %{version}-%{release}

%description -n python3-treq+dev
Metapackage for python3-treq dev extras.

%package -n       python3-treq+docs
Summary:        Metapackage for python3-treq docs extras
Requires:       python3-treq = %{version}-%{release}
Provides:       python3dist(treq[docs]) = %{version}-%{release}

%description -n python3-treq+docs
Metapackage for python3-treq docs extras.

%description

%package -n     python3-treq
Summary:        High-level Twisted HTTP Client API
# oreon:reqs
Requires:       python3dist(hyperlink) >= 21.0.0
Requires:       python3dist(incremental) >= 24.7.2
Requires:       python3dist(twisted[tls]) >= 22.10.0
Requires:       python3dist(typing-extensions) >= 3.10.0
# /oreon:reqs
%description -n python3-treq

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir treq-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-treq usr/lib/python3*/site-packages/treq* usr/lib64/python3*/site-packages/treq* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/treq* usr/lib64/python3*/site-packages/treq* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-treq -f %{oreon_filedir}/python3-treq.list

%changelog

%autochangelog
