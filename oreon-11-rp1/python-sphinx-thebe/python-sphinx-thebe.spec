%global source0_hash 576047f45560e82f64aa5f15200b1eb094dcfe1c5b8f531a8a65bd208e25a493
Name:           python-sphinx-thebe
Version:        0.3.1
Release:        1%{?dist}
Summary:        Integrate interactive code blocks into your documentation
License:        MIT
BuildArch:      noarch
URL:            https://sphinx-thebe.readthedocs.io/
VCS:            git:https://github.com/executablebooks/sphinx-thebe.git
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_thebe/sphinx_thebe-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinx-thebe = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-thebe+sphinx
Summary:        Metapackage for python3-sphinx-thebe sphinx extras
Requires:       python3-sphinx-thebe = %{version}-%{release}
Provides:       python3dist(sphinx-thebe[sphinx]) = %{version}-%{release}

%description -n python3-sphinx-thebe+sphinx
Metapackage for python3-sphinx-thebe sphinx extras.

%package -n       python3-sphinx-thebe+testing
Summary:        Metapackage for python3-sphinx-thebe testing extras
Requires:       python3-sphinx-thebe = %{version}-%{release}
Requires:       python3dist(myst-nb) >= 1.0.0rc0
Provides:       python3dist(sphinx-thebe[testing]) = %{version}-%{release}

%description -n python3-sphinx-thebe+testing
Metapackage for python3-sphinx-thebe testing extras.

%package -n       python3-sphinx-thebe+dev
Summary:        Metapackage for python3-sphinx-thebe dev extras
Requires:       python3-sphinx-thebe = %{version}-%{release}
Provides:       python3dist(sphinx-thebe[dev]) = %{version}-%{release}

%description -n python3-sphinx-thebe+dev
Metapackage for python3-sphinx-thebe dev extras.

%description
Integrate interactive code blocks into your documentation with Thebe and
Binder.

%package     -n python3-sphinx-thebe
Summary:        Integrate interactive code blocks into your documentation
# oreon:reqs
Requires:       python3dist(sphinx) >= 4
# /oreon:reqs
%description -n python3-sphinx-thebe
Integrate interactive code blocks into your documentation with Thebe and
Binder.

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-thebe usr/lib/python3*/site-packages/sphinx_thebe* usr/lib64/python3*/site-packages/sphinx_thebe* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_thebe* usr/lib64/python3*/site-packages/sphinx_thebe* usr/bin/*

%check

%pytest
%files
%files -n python3-sphinx-thebe -f %{oreon_filedir}/python3-sphinx-thebe.list

%changelog

%autochangelog
