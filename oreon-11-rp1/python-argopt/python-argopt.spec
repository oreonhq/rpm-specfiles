%global source0_hash 29780679f4ff620ffbc897c74415bf99a80fb61c26afdb10fe7aac887efb770e

%{?python_enable_dependency_generator}
%global srcname argopt
%global _description \
Define your command line interface (CLI) from a docstring\
(rather than the other way around). Because it’s easy. It’s quick.\
Painless. Then focus on what’s actually important - using the arguments\
in the rest of your program.

Name:           python-%{srcname}
Version:        0.9.1
Release:        %autorelease
Summary:        Doc to argparse driven by docopt

License:        MPL-2.0
URL:            https://github.com/casperdcl/argopt
Source0:        %{pypi_source}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENCE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
