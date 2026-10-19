%global source0_hash d2abfd24652f86501044499bf08c9d639db050f695eefc06b8b8b6f0bb24dbd6
Name:           python-fakeredis
Version:        2.38.0
Release:        1%{?dist}
Summary:        Python implementation of redis API, can be used for testing purposes.
License:        BSD-3-Clause
URL:            https://github.com/cunla/fakeredis-py
Source0:        https://files.pythonhosted.org/packages/source/f/fakeredis/fakeredis-%{version}.tar.gz
BuildArch:      noarch
Patch:          patch-script-mixing-to-use-luaruntime-directly.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fakeredis = %{version}-%{release}
# /oreon:deps
%package -n       python3-fakeredis+lua
Summary:        Metapackage for python3-fakeredis lua extras
Requires:       python3-fakeredis = %{version}-%{release}
Requires:       python3dist(lupa) >= 2.1
Provides:       python3dist(fakeredis[lua]) = %{version}-%{release}

%description -n python3-fakeredis+lua
Metapackage for python3-fakeredis lua extras.

%package -n       python3-fakeredis+json
Summary:        Metapackage for python3-fakeredis json extras
Requires:       python3-fakeredis = %{version}-%{release}
Requires:       python3dist(jsonpath-ng) >= 1.6
Provides:       python3dist(fakeredis[json]) = %{version}-%{release}

%description -n python3-fakeredis+json
Metapackage for python3-fakeredis json extras.

%package -n       python3-fakeredis+bf
Summary:        Metapackage for python3-fakeredis bf extras
Requires:       python3-fakeredis = %{version}-%{release}
Requires:       python3dist(pyprobables) >= 0.6
Provides:       python3dist(fakeredis[bf]) = %{version}-%{release}

%description -n python3-fakeredis+bf
Metapackage for python3-fakeredis bf extras.

%package -n       python3-fakeredis+cf
Summary:        Metapackage for python3-fakeredis cf extras
Requires:       python3-fakeredis = %{version}-%{release}
Requires:       python3dist(pyprobables) >= 0.6
Provides:       python3dist(fakeredis[cf]) = %{version}-%{release}

%description -n python3-fakeredis+cf
Metapackage for python3-fakeredis cf extras.

%package -n       python3-fakeredis+probabilistic
Summary:        Metapackage for python3-fakeredis probabilistic extras
Requires:       python3-fakeredis = %{version}-%{release}
Requires:       python3dist(pyprobables) >= 0.6
Provides:       python3dist(fakeredis[probabilistic]) = %{version}-%{release}

%description -n python3-fakeredis+probabilistic
Metapackage for python3-fakeredis probabilistic extras.

%package -n       python3-fakeredis+valkey
Summary:        Metapackage for python3-fakeredis valkey extras
Requires:       python3-fakeredis = %{version}-%{release}
Requires:       python3dist(valkey) >= 6
Provides:       python3dist(fakeredis[valkey]) = %{version}-%{release}

%description -n python3-fakeredis+valkey
Metapackage for python3-fakeredis valkey extras.

%package -n       python3-fakeredis+vectorset
Summary:        Metapackage for python3-fakeredis vectorset extras
Requires:       python3-fakeredis = %{version}-%{release}
Requires:       python3dist(numpy) >= 2.4.0
Requires:       python3dist(jsonpath-ng) >= 1.6
Provides:       python3dist(fakeredis[vectorset]) = %{version}-%{release}

%description -n python3-fakeredis+vectorset
Metapackage for python3-fakeredis vectorset extras.

%description

%package -n     python3-fakeredis
Summary:        Python implementation of redis API, can be used for testing purposes.
# oreon:reqs
Requires:       python3dist(redis) >= 4.3
Requires:       python3dist(sortedcontainers) >= 2
Requires:       python3dist(typing-extensions) >= 4.7
# /oreon:reqs
%description -n python3-fakeredis

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fakeredis-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fakeredis usr/lib/python3*/site-packages/fakeredis* usr/lib64/python3*/site-packages/fakeredis* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fakeredis* usr/lib64/python3*/site-packages/fakeredis* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fakeredis -f %{oreon_filedir}/python3-fakeredis.list

%changelog

%autochangelog
