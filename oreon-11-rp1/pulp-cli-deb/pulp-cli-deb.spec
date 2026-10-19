%global source0_hash 3ec974c922a465066a0371e7973d43c0b82f36c65023f3978f52b2ef5c3b9b8e
%bcond tests 1
Name: pulp-cli-deb
Version: 0.5.0
Release:        1%{?dist}
Summary:        Command line interface to talk to the Pulp 3 REST API (deb plugin)
License: GPL-2.0-or-later
BuildArch: noarch
URL: https://github.com/pulp/%{name}
Source0:        https://github.com/pulp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires: pulp-cli >= 0.29.0
Recommends: python3-pygments
Recommends: python3-click-shell
Recommends: python3-secretstorage
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pulp-cli-deb = %{version}-%{release}
# /oreon:deps
%description
pulp-cli provides the "pulp" command, able to communicate with the Pulp3 API in
a more natural way than plain http. Specifically, resources can not only be
referenced by their href, but also their natural key (e.g. name). It also
handles waiting on tasks on behalf of the user.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove the Python version upper bound to enable building with new versions in Fedora
sed -i '/requires-python =/s/,<3\.[0-9]\+//' pyproject.toml

# Remove upper version bound on setuptools to enable building with new versions in Fedora
sed -i '/requires =.*setuptools/s/<[0-9]\+//' pyproject.toml

# Remove upper version bound on packaging to enable building with new versions in Fedora
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml

# Remove all bounds on test dependencies; we must use what we have
sed -r -Ei 's/^([a-zA-Z0-9._-]+).*/\1/' test_requirements.txt

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main
%if %{with tests}
%check

%pyproject_check_import pulpcore
%pytest -m help_page
%endif
%license LICENSE
%doc CHANGES.md
%files

%changelog

%autochangelog
