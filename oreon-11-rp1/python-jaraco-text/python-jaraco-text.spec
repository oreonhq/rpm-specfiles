%global source0_hash ddd5eb6259d0701e08cb642c8d6b63bcc73947d03df9239ea67bbef911b3e4e1
Name:           python-jaraco-text
Version:        4.3.0
Release:        1%{?dist}
Summary:        Module for text manipulation
License:        MIT
URL:            https://github.com/jaraco/jaraco.text
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco_text/jaraco_text-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/29.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-jaraco-text = %{version}-%{release}
# /oreon:deps
%package -n       python3-jaraco-text+test
Summary:        Metapackage for python3-jaraco-text test extras
Requires:       python3-jaraco-text = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(jaraco-text[test]) = %{version}-%{release}

%description -n python3-jaraco-text+test
Metapackage for python3-jaraco-text test extras.

%package -n       python3-jaraco-text+doc
Summary:        Metapackage for python3-jaraco-text doc extras
Requires:       python3-jaraco-text = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Provides:       python3dist(jaraco-text[doc]) = %{version}-%{release}

%description -n python3-jaraco-text+doc
Metapackage for python3-jaraco-text doc extras.

%package -n       python3-jaraco-text+inflect
Summary:        Metapackage for python3-jaraco-text inflect extras
Requires:       python3-jaraco-text = %{version}-%{release}
Provides:       python3dist(jaraco-text[inflect]) = %{version}-%{release}

%description -n python3-jaraco-text+inflect
Metapackage for python3-jaraco-text inflect extras.

%package -n       python3-jaraco-text+check
Summary:        Metapackage for python3-jaraco-text check extras
Requires:       python3-jaraco-text = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.14
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(jaraco-text[check]) = %{version}-%{release}

%description -n python3-jaraco-text+check
Metapackage for python3-jaraco-text check extras.

%package -n       python3-jaraco-text+cover
Summary:        Metapackage for python3-jaraco-text cover extras
Requires:       python3-jaraco-text = %{version}-%{release}
Provides:       python3dist(jaraco-text[cover]) = %{version}-%{release}

%description -n python3-jaraco-text+cover
Metapackage for python3-jaraco-text cover extras.

%package -n       python3-jaraco-text+enabler
Summary:        Metapackage for python3-jaraco-text enabler extras
Requires:       python3-jaraco-text = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(jaraco-text[enabler]) = %{version}-%{release}

%description -n python3-jaraco-text+enabler
Metapackage for python3-jaraco-text enabler extras.

%package -n       python3-jaraco-text+type
Summary:        Metapackage for python3-jaraco-text type extras
Requires:       python3-jaraco-text = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Provides:       python3dist(jaraco-text[type]) = %{version}-%{release}

%description -n python3-jaraco-text+type
Metapackage for python3-jaraco-text type extras.

%description

%package -n     python3-jaraco-text
Summary:        Module for text manipulation
# oreon:reqs
Requires:       python3dist(jaraco.context) >= 4.1
# /oreon:reqs
%description -n python3-jaraco-text

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jaraco_text-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jaraco-text usr/lib/python3*/site-packages/jaraco_text* usr/lib64/python3*/site-packages/jaraco_text* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jaraco_text* usr/lib64/python3*/site-packages/jaraco_text* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jaraco-text -f %{oreon_filedir}/python3-jaraco-text.list

%changelog

%autochangelog
