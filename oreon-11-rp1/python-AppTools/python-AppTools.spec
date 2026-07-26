%global source0_hash 7dd8f3a95ca02fc1c03f82cebbe6bed0f74e74fb93e4f66987fa4d8e606ff167

%global srcname apptools
%global forgeurl https://github.com/enthought/%{srcname}

Name:    python-AppTools
Version: 5.3.1
%forgemeta

Release: %autorelease
Summary: Enthought Tool Suite Application Tools
# Automatically converted from old format: BSD and LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+

URL:     %{forgeurl}
Source0: %{pypi_source}
Source1: README.fedora.%{name}

BuildArch: noarch

%global common_description %{expand:
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications. They implement
functionality that is commonly needed by many applications

    * enthought.appscripting: Framework for scripting applications.

    * enthought.help: Provides a plugin for displaying documents and
      examples and running demos in Envisage Workbench applications.

    * enthought.io: Provides an abstraction for files and folders in a
      file system.

    * enthought.naming: Manages naming contexts, supporting non-string
      data types and scoped preferences

    * enthought.permissions: Supports limiting access to parts of an
      application unless the user is appropriately authorised (not
      full-blown security).

and many more.
}

%description %{common_description}

%package -n python-%{srcname}-doc
Summary: Documentation for %{name}

BuildRequires: make

Provides:  python-AppTools-doc = %{version}-%{release}
Obsoletes: python-AppTools-doc < 4.4.0-1

%description -n python-%{srcname}-doc
Documentation and examples for %{name}.

%package -n python%{python3_pkgversion}-%{srcname}
Summary: %summary
BuildRequires: python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %{common_description}

%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} gui
%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} h5
%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} persistence
%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} preferences

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}
# Drop pinning numpy version
sed -i -e 's/numpy < 2.0/numpy/' setup.py
# remove exec permission
find examples -type f -exec chmod 0644 {} ";"
cp -p %{SOURCE1} README.fedora

%generate_buildrequires
%pyproject_buildrequires -x docs,test,gui,h5,persistence,preferences

%build
%pyproject_wheel

pushd docs
PYTHONPATH=../build/lib make html SPHINXBUILD=%{_bindir}/sphinx-build-3
popd

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGES.txt

%files -n python-%{srcname}-doc
%license *LICENSE*.txt
%doc docs/build/html examples README.fedora

%changelog
%autochangelog
