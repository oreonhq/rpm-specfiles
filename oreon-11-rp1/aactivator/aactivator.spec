%global source0_hash d312e84201676f8d5c23dc0c590f403b5b40767493d99f020a9dc8707f59b771
Name:           aactivator
Version:        2.0.0
Release:        8%{?dist}
Summary:        Automatically source and unsource a project's environment
License:        MIT
URL:            https://github.com/Yelp/aactivator
Source0:        https://github.com/Yelp/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch0:         %{name}-set-path-in-integration-tests.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aactivator = %{version}-%{release}
# /oreon:deps
%description
aactivator is a simple tool that automatically sources ("activates") and
unsources a project's environment when entering and exiting it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir aactivator-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest -x -k "not test_aactivator_goes_missing_no_output"
%files

%changelog

%autochangelog
