%global source0_hash 926376fdab2e1ca8eec05698c457d17718ed1458fa574b67e815c43ae52b377a
%global sum Entity Relation Diagrams generation tool
%global desc \
ERAlchemy generates Entity Relation (ER) diagram (like the one below) from \
databases or from SQLAlchemy models.
Name:           eralchemy
Version:        1.7.0
Release:        1%{?dist}
Summary:        Entity Relation Diagrams generation tool
License:        Apache-2.0
URL:            https://github.com/eralchemy/eralchemy
Source0:        https://files.pythonhosted.org/packages/source/e/%{name}/%{name}-%{version}.tar.gz
Requires:       python3-%name = %version-%release
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-eralchemy = %{version}-%{release}
# /oreon:deps
%package -n       python3-eralchemy+test
Summary:        Metapackage for python3-eralchemy test extras
Requires:       python3-eralchemy = %{version}-%{release}
Requires:       python3dist(flask-sqlalchemy) >= 2.5.1
Requires:       python3dist(psycopg2-binary) >= 2.9.3
Requires:       python3dist(pytest) >= 7.4.3
Requires:       python3dist(pygraphviz) >= 1.9
Requires:       python3dist(graphviz) >= 0.20.3
Provides:       python3dist(eralchemy[test]) = %{version}-%{release}

%description -n python3-eralchemy+test
Metapackage for python3-eralchemy test extras.

%package -n       python3-eralchemy+graphviz
Summary:        Metapackage for python3-eralchemy graphviz extras
Requires:       python3-eralchemy = %{version}-%{release}
Requires:       python3dist(graphviz) >= 0.20.3
Provides:       python3dist(eralchemy[graphviz]) = %{version}-%{release}

%description -n python3-eralchemy+graphviz
Metapackage for python3-eralchemy graphviz extras.

%package -n       python3-eralchemy+pygraphviz
Summary:        Metapackage for python3-eralchemy pygraphviz extras
Requires:       python3-eralchemy = %{version}-%{release}
Requires:       python3dist(pygraphviz) >= 1.9
Provides:       python3dist(eralchemy[pygraphviz]) = %{version}-%{release}

%description -n python3-eralchemy+pygraphviz
Metapackage for python3-eralchemy pygraphviz extras.

%package -n       python3-eralchemy+dev
Summary:        Metapackage for python3-eralchemy dev extras
Requires:       python3-eralchemy = %{version}-%{release}
Provides:       python3dist(eralchemy[dev]) = %{version}-%{release}

%description -n python3-eralchemy+dev
Metapackage for python3-eralchemy dev extras.

%package -n       python3-eralchemy+docs
Summary:        Metapackage for python3-eralchemy docs extras
Requires:       python3-eralchemy = %{version}-%{release}
Requires:       python3dist(sphinx) >= 6.2.1
Provides:       python3dist(eralchemy[docs]) = %{version}-%{release}

%description -n python3-eralchemy+docs
Metapackage for python3-eralchemy docs extras.

%description
%desc

%package -n python3-%name
Summary:        %sum
%description -n python3-%name
%desc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i 's/graphviz >= 0.20.3/graphviz/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/eralchemy* usr/lib64/python3*/site-packages/eralchemy* usr/bin/*

%check

%files
%files -n python3-eralchemy -f %{oreon_filedir}/python3-eralchemy.list

%changelog

%autochangelog
