%global source0_hash 2fdbcdead6f169f3a6f6beabe1d664a1c01ced9a7f34dd1622a7e9612e66a194

# Created by pyp2rpm-3.3.5
%global pypi_name wcmatch

Name:           python-%{pypi_name}
Version:        10.0
Release:        7%{?dist}
Summary:        Wildcard/glob file name matcher

License:        MIT
URL:            https://github.com/facelessuser/wcmatch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(bracex)
BuildRequires:  python3dist(setuptools)

%description
Wildcard Match provides an enhanced fnmatch, glob, and pathlib library in order
to provide file matching and globbing that more closely follows the features
found in Bash. In some ways these libraries are similar to Python's builtin
libraries as they provide a similar interface to match, filter, and glob the
file system. But they also include a number of features found in Bash's
globbing such as backslash escaping, brace expansion, extended glob pattern
groups, etc. They also add a number of new useful functions as well, such as
globmatch which functions like fnmatch, but for paths.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Wildcard Match provides an enhanced fnmatch, glob, and pathlib library in order
to provide file matching and globbing that more closely follows the features
found in Bash. In some ways these libraries are similar to Python's builtin
libraries as they provide a similar interface to match, filter, and glob the
file system. But they also include a number of features found in Bash's
globbing such as backslash escaping, brace expansion, extended glob pattern
groups, etc. They also add a number of new useful functions as well, such as
globmatch which functions like fnmatch, but for paths.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -vv -k "not test_tilde_user"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
