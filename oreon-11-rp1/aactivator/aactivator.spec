%global source0_hash d312e84201676f8d5c23dc0c590f403b5b40767493d99f020a9dc8707f59b771

Name:           aactivator
Version:        2.0.0
Release:        8%{?dist}
Summary:        Automatically source and unsource a project's environment

License:        MIT
URL:            https://github.com/Yelp/aactivator
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
# The patch is necessary to get most integration tests passing in Fedora's
# build infrastructure.
Patch0:         %{name}-set-path-in-integration-tests.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# required to run the test suite
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(pytest)
BuildRequires:  zsh

%global _description %{expand:
aactivator is a simple tool that automatically sources ("activates") and
unsources a project's environment when entering and exiting it.}

%description %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n aactivator-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l aactivator

%check
# Using pytest-xdist here ("-n auto") leads to DeprecationWarnings from Python:
#   DeprecationWarning: This process (pid=...) is multi-threaded, use of
#   forkpty() may lead to deadlocks in the child.
# "test_aactivator_goes_missing_no_output" removes the executable "aactivator"
# as part of the test. In addition, getting that test to pass in Fedora's build
# process requires more code changes because the test assumes "aactivator" is
# located in the same directory as the Python executable.
%pytest -x -k "not test_aactivator_goes_missing_no_output"

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/aactivator

%changelog
%autochangelog
