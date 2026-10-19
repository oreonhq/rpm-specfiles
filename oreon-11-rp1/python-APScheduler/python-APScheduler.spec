%global source0_hash cd2fcc9330039a81a5893472ad49facf23a6d5604cbe1d918c835c6de7834d5a
Name:           python-apscheduler
Version:        3.11.3
Release:        1%{?dist}
Summary:        In-process task scheduler with Cron-like capabilities
License:        MIT
URL:            https://github.com/agronholm/apscheduler
Source0:        https://files.pythonhosted.org/packages/source/a/apscheduler/apscheduler-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 6.4
Requires:       python3-apscheduler = %{version}-%{release}
# /oreon:deps
%package -n       python3-apscheduler+etcd
Summary:        Metapackage for python3-apscheduler etcd extras
Requires:       python3-apscheduler = %{version}-%{release}
Requires:       python3dist(protobuf) <= 3.21.0
Provides:       python3dist(apscheduler[etcd]) = %{version}-%{release}

%description -n python3-apscheduler+etcd
Metapackage for python3-apscheduler etcd extras.

%package -n       python3-apscheduler+gevent
Summary:        Metapackage for python3-apscheduler gevent extras
Requires:       python3-apscheduler = %{version}-%{release}
Provides:       python3dist(apscheduler[gevent]) = %{version}-%{release}

%description -n python3-apscheduler+gevent
Metapackage for python3-apscheduler gevent extras.

%package -n       python3-apscheduler+mongodb
Summary:        Metapackage for python3-apscheduler mongodb extras
Requires:       python3-apscheduler = %{version}-%{release}
Requires:       python3dist(pymongo) >= 3.0
Provides:       python3dist(apscheduler[mongodb]) = %{version}-%{release}

%description -n python3-apscheduler+mongodb
Metapackage for python3-apscheduler mongodb extras.

%package -n       python3-apscheduler+redis
Summary:        Metapackage for python3-apscheduler redis extras
Requires:       python3-apscheduler = %{version}-%{release}
Requires:       python3dist(redis) >= 3.0
Provides:       python3dist(apscheduler[redis]) = %{version}-%{release}

%description -n python3-apscheduler+redis
Metapackage for python3-apscheduler redis extras.

%package -n       python3-apscheduler+rethinkdb
Summary:        Metapackage for python3-apscheduler rethinkdb extras
Requires:       python3-apscheduler = %{version}-%{release}
Requires:       python3dist(rethinkdb) >= 2.4.0
Provides:       python3dist(apscheduler[rethinkdb]) = %{version}-%{release}

%description -n python3-apscheduler+rethinkdb
Metapackage for python3-apscheduler rethinkdb extras.

%package -n       python3-apscheduler+sqlalchemy
Summary:        Metapackage for python3-apscheduler sqlalchemy extras
Requires:       python3-apscheduler = %{version}-%{release}
Requires:       python3dist(sqlalchemy) >= 1.4
Provides:       python3dist(apscheduler[sqlalchemy]) = %{version}-%{release}

%description -n python3-apscheduler+sqlalchemy
Metapackage for python3-apscheduler sqlalchemy extras.

%package -n       python3-apscheduler+tornado
Summary:        Metapackage for python3-apscheduler tornado extras
Requires:       python3-apscheduler = %{version}-%{release}
Requires:       python3dist(tornado) >= 4.3
Provides:       python3dist(apscheduler[tornado]) = %{version}-%{release}

%description -n python3-apscheduler+tornado
Metapackage for python3-apscheduler tornado extras.

%package -n       python3-apscheduler+twisted
Summary:        Metapackage for python3-apscheduler twisted extras
Requires:       python3-apscheduler = %{version}-%{release}
Provides:       python3dist(apscheduler[twisted]) = %{version}-%{release}

%description -n python3-apscheduler+twisted
Metapackage for python3-apscheduler twisted extras.

%package -n       python3-apscheduler+zookeeper
Summary:        Metapackage for python3-apscheduler zookeeper extras
Requires:       python3-apscheduler = %{version}-%{release}
Provides:       python3dist(apscheduler[zookeeper]) = %{version}-%{release}

%description -n python3-apscheduler+zookeeper
Metapackage for python3-apscheduler zookeeper extras.

%package -n       python3-apscheduler+test
Summary:        Metapackage for python3-apscheduler test extras
Requires:       python3-apscheduler = %{version}-%{release}
Requires:       python3dist(anyio) >= 4.5.2
Provides:       python3dist(apscheduler[test]) = %{version}-%{release}

%description -n python3-apscheduler+test
Metapackage for python3-apscheduler test extras.

%package -n       python3-apscheduler+doc
Summary:        Metapackage for python3-apscheduler doc extras
Requires:       python3-apscheduler = %{version}-%{release}
Requires:       python3dist(sphinx-rtd-theme) >= 1.3.0
Provides:       python3dist(apscheduler[doc]) = %{version}-%{release}

%description -n python3-apscheduler+doc
Metapackage for python3-apscheduler doc extras.

%description

%package -n     python3-apscheduler
Summary:        In-process task scheduler with Cron-like capabilities
# oreon:reqs
Requires:       python3dist(tzlocal) >= 3.0
# /oreon:reqs
%description -n python3-apscheduler

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir apscheduler-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-apscheduler usr/lib/python3*/site-packages/apscheduler* usr/lib64/python3*/site-packages/apscheduler* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/apscheduler* usr/lib64/python3*/site-packages/apscheduler* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-apscheduler -f %{oreon_filedir}/python3-apscheduler.list

%changelog

%autochangelog
