%global source0_hash f4d117b49697f338769759fa5cacf5197da4888b347b9fda2e50aef5cd8d93bd
Name:           python-rich-rst
Version:        2.1.0
Release:        1%{?dist}
Summary:        A beautiful reStructuredText renderer for rich
License:        MIT
URL:            https://wasi-master.github.io/rich-rst
Source0:        https://files.pythonhosted.org/packages/source/r/rich_rst/rich_rst-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-rich-rst = %{version}-%{release}
# /oreon:deps
%package -n       python3-rich-rst+docs
Summary:        Metapackage for python3-rich-rst docs extras
Requires:       python3-rich-rst = %{version}-%{release}
Provides:       python3dist(rich-rst[docs]) = %{version}-%{release}

%description -n python3-rich-rst+docs
Metapackage for python3-rich-rst docs extras.

%package -n       python3-rich-rst+tests
Summary:        Metapackage for python3-rich-rst tests extras
Requires:       python3-rich-rst = %{version}-%{release}
Provides:       python3dist(rich-rst[tests]) = %{version}-%{release}

%description -n python3-rich-rst+tests
Metapackage for python3-rich-rst tests extras.

%package -n       python3-rich-rst+dev
Summary:        Metapackage for python3-rich-rst dev extras
Requires:       python3-rich-rst = %{version}-%{release}
Provides:       python3dist(rich-rst[dev]) = %{version}-%{release}

%description -n python3-rich-rst+dev
Metapackage for python3-rich-rst dev extras.

%description

%package -n     python3-rich-rst
Summary:        A beautiful reStructuredText renderer for rich
# oreon:reqs
Requires:       python3dist(pygments) >= 2.0.0
Requires:       python3dist(rich) >= 12.0.0
# /oreon:reqs
%description -n python3-rich-rst

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rich_rst-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rich-rst usr/lib/python3*/site-packages/rich_rst* usr/lib64/python3*/site-packages/rich_rst* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rich_rst* usr/lib64/python3*/site-packages/rich_rst* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rich-rst -f %{oreon_filedir}/python3-rich-rst.list

%changelog

%autochangelog
