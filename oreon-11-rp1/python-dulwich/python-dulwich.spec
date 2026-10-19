%global source0_hash e98f775601846fb4d44a384003e93c53c42b0c9796c8fe0cc3128b8e2e0bbf88
Name:           python-dulwich
Version:        1.2.15
Release:        1%{?dist}
Summary:        Python Git Library
License:        Apache-2.0 OR GPL-2.0-or-later
URL:            https://www.dulwich.io/
Source0:        https://files.pythonhosted.org/packages/source/d/dulwich/dulwich-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-dulwich = %{version}-%{release}
# /oreon:deps
%package -n       python3-dulwich+fastimport
Summary:        Metapackage for python3-dulwich fastimport extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[fastimport]) = %{version}-%{release}

%description -n python3-dulwich+fastimport
Metapackage for python3-dulwich fastimport extras.

%package -n       python3-dulwich+https
Summary:        Metapackage for python3-dulwich https extras
Requires:       python3-dulwich = %{version}-%{release}
Requires:       python3dist(urllib3) >= 2.2.2
Provides:       python3dist(dulwich[https]) = %{version}-%{release}

%description -n python3-dulwich+https
Metapackage for python3-dulwich https extras.

%package -n       python3-dulwich+pgp
Summary:        Metapackage for python3-dulwich pgp extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[pgp]) = %{version}-%{release}

%description -n python3-dulwich+pgp
Metapackage for python3-dulwich pgp extras.

%package -n       python3-dulwich+paramiko
Summary:        Metapackage for python3-dulwich paramiko extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[paramiko]) = %{version}-%{release}

%description -n python3-dulwich+paramiko
Metapackage for python3-dulwich paramiko extras.

%package -n       python3-dulwich+colordiff
Summary:        Metapackage for python3-dulwich colordiff extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[colordiff]) = %{version}-%{release}

%description -n python3-dulwich+colordiff
Metapackage for python3-dulwich colordiff extras.

%package -n       python3-dulwich+dev
Summary:        Metapackage for python3-dulwich dev extras
Requires:       python3-dulwich = %{version}-%{release}
Requires:       python3dist(ruff) == 0.16.5
Requires:       python3dist(mypy) == 2.3.1
Requires:       python3dist(dissolve) >= 0.1.1
Requires:       python3dist(codespell) == 2.4.3
Provides:       python3dist(dulwich[dev]) = %{version}-%{release}

%description -n python3-dulwich+dev
Metapackage for python3-dulwich dev extras.

%package -n       python3-dulwich+hypothesis
Summary:        Metapackage for python3-dulwich hypothesis extras
Requires:       python3-dulwich = %{version}-%{release}
Requires:       python3dist(hypothesis) >= 6
Provides:       python3dist(dulwich[hypothesis]) = %{version}-%{release}

%description -n python3-dulwich+hypothesis
Metapackage for python3-dulwich hypothesis extras.

%package -n       python3-dulwich+merge
Summary:        Metapackage for python3-dulwich merge extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[merge]) = %{version}-%{release}

%description -n python3-dulwich+merge
Metapackage for python3-dulwich merge extras.

%package -n       python3-dulwich+fuzzing
Summary:        Metapackage for python3-dulwich fuzzing extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[fuzzing]) = %{version}-%{release}

%description -n python3-dulwich+fuzzing
Metapackage for python3-dulwich fuzzing extras.

%package -n       python3-dulwich+patiencediff
Summary:        Metapackage for python3-dulwich patiencediff extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[patiencediff]) = %{version}-%{release}

%description -n python3-dulwich+patiencediff
Metapackage for python3-dulwich patiencediff extras.

%package -n       python3-dulwich+range_diff
Summary:        Metapackage for python3-dulwich range_diff extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[range_diff]) = %{version}-%{release}

%description -n python3-dulwich+range_diff
Metapackage for python3-dulwich range_diff extras.

%package -n       python3-dulwich+aiohttp
Summary:        Metapackage for python3-dulwich aiohttp extras
Requires:       python3-dulwich = %{version}-%{release}
Provides:       python3dist(dulwich[aiohttp]) = %{version}-%{release}

%description -n python3-dulwich+aiohttp
Metapackage for python3-dulwich aiohttp extras.

%description

%package -n     python3-dulwich
Summary:        Python Git Library
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.6.0
Requires:       python3dist(urllib3) >= 2.2.2
# /oreon:reqs
%description -n python3-dulwich

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir dulwich-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dulwich usr/lib/python3*/site-packages/dulwich* usr/lib64/python3*/site-packages/dulwich* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dulwich* usr/lib64/python3*/site-packages/dulwich* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dulwich -f %{oreon_filedir}/python3-dulwich.list

%changelog

%autochangelog
