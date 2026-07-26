%global source0_hash be3ebc611ee9f55d204f209010880b4e5abff19bb4dcc31d55049f05a9fe84b4

Name:           is-it-in-rhel
Version:        1.0
Release:        %autorelease
Summary:        Command line tool to find out if a package is in RHEL
License:        GPL-2.0-or-later
URL:            https://pagure.io/is-it-in-rhel
Source:         https://releases.pagure.org/is-it-in-rhel/is-it-in-rhel-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
is-it-in-rhel is a command line utility to find out if a specific package is
packaged in RHEL or not.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l is_it_in_rhel

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/is-it-in-rhel

%changelog
%autochangelog
