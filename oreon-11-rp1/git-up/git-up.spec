%global source0_hash 4a771b9cae8bc6c95e2916bfb120a6ffc76c80fc3f5c91af61f91c21e5980f2e

%global pypi_name git_up

Name:           git-up
Version:        2.3.0
Release:        5%{?dist}
Summary:        A more friendly "git pull" in Python

License:        MIT
URL:            https://github.com/msiemens/PyGitUp
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/msiemens/PyGitUp/v%{version}/LICENCE

# pytest 8 compatibility
# https://github.com/msiemens/PyGitUp/commit/eb7b155e3396ac645dc075665e87b16bc34e6827.patch
Patch:          135.patch
# termcolor 3 compatibility
# https://github.com/msiemens/PyGitUp/pull/141
Patch:          141.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
PyGitUp is a Python port of aanand/git-up. It not only fully covers the
abilities of git-up and should be a drop-in replacement, but also extends it
slightly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files PyGitUp

%check
if ! git config user.name ; then
  git config --global user.name "user"
fi
if ! git config user.email ; then
  git config --global user.email "user@example.com"
fi
%pytest

%files -f %{pyproject_files}
%license LICENCE
%doc README.rst
%{_bindir}/git-up
%exclude %{python3_sitelib}/PyGitUp/tests

%changelog
%autochangelog
