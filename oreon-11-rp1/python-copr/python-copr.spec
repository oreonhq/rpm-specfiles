%global source0_hash f371edf2474c9eb6e3f573a97d4df0a363d543d93e8a9bd1de6d96a4bb18a7e5

%global srcname copr

Name:       python-copr
Version:    2.5
Release:    2%{?dist}
Summary:    Python interface for Copr

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch:  noarch

BuildRequires: libxslt
BuildRequires: util-linux

#doc
BuildRequires: make

%global _description\
COPR is lightweight build system. It allows you to create new project in WebUI,\
and submit new builds and COPR will create yum repository from latest builds.\
\
This package contains python interface to access Copr service. Mostly useful\
for developers only.\

%description %_description

%package -n python3-copr
Summary:        Python interface for Copr

# for recent distributions the requires are generated dynamically
%if 0%{?rhel} && 0%{?rhel} <= 8

BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: python3-munch
BuildRequires: python3-filelock
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-requests
BuildRequires: python3-requests-toolbelt
BuildRequires: python3-sphinx
BuildRequires: python3-requests-gssapi

Requires: python3-munch
Requires: python3-filelock
Requires: python3-requests
Requires: python3-requests-toolbelt
Requires: python3-setuptools
Requires: python3-requests-gssapi

%{?python_provide:%python_provide python3-copr}

%else
# These are not in requirements.txt
Requires: python3-requests-gssapi

BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: python3-pytest
BuildRequires: python3-requests-gssapi
BuildRequires: python3-filelock
BuildRequires: pyproject-rpm-macros

%generate_buildrequires
%pyproject_buildrequires -r
%endif

%description -n python3-copr
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latest builds.

This package contains python interface to access Copr service. Mostly useful
for developers only.

%package -n python-copr-doc
Summary:    Code documentation for python-copr package

%description doc
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latest builds.

This package includes documentation for python-copr. Mostly useful for
developers only.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%if 0%{?rhel} && 0%{?rhel} <= 8
version=%version %py3_build
%else
version=%version %pyproject_wheel
%endif

mv copr/README.rst ./

# build documentation
make -C docs %{?_smp_mflags} html %{?sphinxbuild}

%install
%if 0%{?rhel} && 0%{?rhel} <= 8
version=%version %py3_install
%else
version=%version %pyproject_install
%endif

find %{buildroot} -name '*.exe' -delete

install -d %{buildroot}%{_pkgdocdir}
cp -a docs/_build/html %{buildroot}%{_pkgdocdir}/

%check
%{__python3} -m pytest -vv copr/test

%files -n python3-copr
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%files -n python-copr-doc
%license LICENSE
%doc %{_pkgdocdir}

%changelog
%autochangelog
