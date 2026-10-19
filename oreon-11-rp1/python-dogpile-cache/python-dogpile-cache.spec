%global source0_hash 849c5573c9a38f155cd4173103c702b637ede0361c12e864876877d0cd125eec
Name:           python-dogpile-cache
Version:        1.5.0
Release:        1%{?dist}
Summary:        A caching front-end based on the Dogpile lock.
License:        MIT
URL:            https://github.com/sqlalchemy/dogpile.cache
Source0:        https://files.pythonhosted.org/packages/source/d/dogpile_cache/dogpile_cache-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-dogpile-cache = %{version}-%{release}
# /oreon:deps
%package -n       python3-dogpile-cache+pifpaf
Summary:        Metapackage for python3-dogpile-cache pifpaf extras
Requires:       python3-dogpile-cache = %{version}-%{release}
Requires:       python3dist(pifpaf) >= 3.3.0
Provides:       python3dist(dogpile-cache[pifpaf]) = %{version}-%{release}

%description -n python3-dogpile-cache+pifpaf
Metapackage for python3-dogpile-cache pifpaf extras.

%package -n       python3-dogpile-cache+pymemcache
Summary:        Metapackage for python3-dogpile-cache pymemcache extras
Requires:       python3-dogpile-cache = %{version}-%{release}
Provides:       python3dist(dogpile-cache[pymemcache]) = %{version}-%{release}

%description -n python3-dogpile-cache+pymemcache
Metapackage for python3-dogpile-cache pymemcache extras.

%package -n       python3-dogpile-cache+memcached
Summary:        Metapackage for python3-dogpile-cache memcached extras
Requires:       python3-dogpile-cache = %{version}-%{release}
Provides:       python3dist(dogpile-cache[memcached]) = %{version}-%{release}

%description -n python3-dogpile-cache+memcached
Metapackage for python3-dogpile-cache memcached extras.

%package -n       python3-dogpile-cache+bmemcached
Summary:        Metapackage for python3-dogpile-cache bmemcached extras
Requires:       python3-dogpile-cache = %{version}-%{release}
Provides:       python3dist(dogpile-cache[bmemcached]) = %{version}-%{release}

%description -n python3-dogpile-cache+bmemcached
Metapackage for python3-dogpile-cache bmemcached extras.

%package -n       python3-dogpile-cache+pylibmc
Summary:        Metapackage for python3-dogpile-cache pylibmc extras
Requires:       python3-dogpile-cache = %{version}-%{release}
Provides:       python3dist(dogpile-cache[pylibmc]) = %{version}-%{release}

%description -n python3-dogpile-cache+pylibmc
Metapackage for python3-dogpile-cache pylibmc extras.

%package -n       python3-dogpile-cache+redis
Summary:        Metapackage for python3-dogpile-cache redis extras
Requires:       python3-dogpile-cache = %{version}-%{release}
Provides:       python3dist(dogpile-cache[redis]) = %{version}-%{release}

%description -n python3-dogpile-cache+redis
Metapackage for python3-dogpile-cache redis extras.

%package -n       python3-dogpile-cache+valkey
Summary:        Metapackage for python3-dogpile-cache valkey extras
Requires:       python3-dogpile-cache = %{version}-%{release}
Provides:       python3dist(dogpile-cache[valkey]) = %{version}-%{release}

%description -n python3-dogpile-cache+valkey
Metapackage for python3-dogpile-cache valkey extras.

%description

%package -n     python3-dogpile-cache
Summary:        A caching front-end based on the Dogpile lock.
# oreon:reqs
Requires:       python3dist(decorator) >= 4.0.0
Requires:       python3dist(stevedore) >= 3.0.0
Requires:       python3dist(typing-extensions) >= 4.0.1
# /oreon:reqs
%description -n python3-dogpile-cache

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir dogpile_cache-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dogpile-cache usr/lib/python3*/site-packages/dogpile_cache* usr/lib64/python3*/site-packages/dogpile_cache* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dogpile_cache* usr/lib64/python3*/site-packages/dogpile_cache* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dogpile-cache -f %{oreon_filedir}/python3-dogpile-cache.list

%changelog

%autochangelog
