%global source0_hash f40f2c71cecb2068c7f06a53825778b674d58d8395b4ea60551a36164d2988e3

%global srcname sphinx-issues
%global srcname_ sphinx_issues

Name:           python-%{srcname}
Version:        6.0.0
Release:        %autorelease
Summary:        Sphinx extension for linking to your project's issue tracker

License:        MIT
URL:            https://github.com/sloria/sphinx-issues
Source0:        %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
A Sphinx extension for linking to your project's issue tracker. Includes roles
for linking to issues, pull requests, user profiles, with built-in support for
GitHub (though this works with other services).

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
A Sphinx extension for linking to your project's issue tracker. Includes roles
for linking to issues, pull requests, user profiles, with built-in support for
GitHub (though this works with other services).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname_}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname_}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
