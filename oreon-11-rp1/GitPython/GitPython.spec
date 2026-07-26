%global source0_hash 400124c7d0ef4ea03f7310ac2fbf7151e09ff97f2a3288d64a440c584a29c37f

%global srcname GitPython

Name:           %{srcname}
Version:        3.1.46
Release:        3%{?dist}
Summary:        Python Git Library

License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/GitPython
Source:         %{pypi_source gitpython}

BuildArch:      noarch

%global _description %{expand:
GitPython is a python library used to interact with git repositories,
high-level like git-porcelain, or low-level like git-plumbing.

It provides abstractions of git objects for easy access of repository data, and
additionally allows you to access the git repository more directly using either
a pure python implementation, or the faster, but more resource intensive git
command implementation.

The object database implementation is optimized for handling large quantities
of objects and large datasets, which is achieved by using low-level structures
and data streaming.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core
Requires:       git-core

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gitpython-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l git

%check
# The upstream test suite has very specific requirements, such as being run in
# its own git repository and with the dependencies as git submodules.  Upstream
# is aware this makes it nearly impossible for distros to run the upstream test
# suite. For now, we'll just check that the module is importable.
# https://github.com/gitpython-developers/GitPython/issues/914
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES AUTHORS

%changelog
%autochangelog
