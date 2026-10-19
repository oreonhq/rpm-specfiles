%global source0_hash 6c5822b7b756a99a356b915dd1267f52ab8a4efaa135963bd7f4bd5d368f71d7
Name:           python-expandvars
Version:        1.1.2
Release:        1%{?dist}
Summary:        Expand system variables Unix style
License:        MIT
URL:            https://github.com/sayanarijit/expandvars
Source0:        https://files.pythonhosted.org/packages/source/e/expandvars/expandvars-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This module is inspired by GNU bash’s variable expansion features. It can be
used as an alternative to Python’s os.path.expandvars function.
A good use case is reading config files with the flexibility of reading values
from environment variables using advanced features like returning a default
value if some variable is not defined.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-expandvars = %{version}-%{release}
# /oreon:deps
%package -n       python3-expandvars+tests
Summary:        Metapackage for python3-expandvars tests extras
Requires:       python3-expandvars = %{version}-%{release}
Provides:       python3dist(expandvars[tests]) = %{version}-%{release}

%description -n python3-expandvars+tests
Metapackage for python3-expandvars tests extras.

%description %{common_description}

%package -n python3-expandvars
Summary:        Expand system variables Unix style
%description -n python3-expandvars %{common_description}

%prep

%autosetup -n expandvars-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i "s/--cov[^[:blank:]'\"]*[[:blank:]]*//g" pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-expandvars usr/lib/python3*/site-packages/expandvars* usr/lib64/python3*/site-packages/expandvars* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/expandvars* usr/lib64/python3*/site-packages/expandvars* usr/bin/*

%check

%pytest
%files
%files -n python3-expandvars -f %{oreon_filedir}/python3-expandvars.list

%changelog

%autochangelog
