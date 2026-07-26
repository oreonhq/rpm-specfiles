%global source0_hash e5e0eb85ea3e6ae2943e491b41cabe9921e46cedf203160c0aaabd20dab30001

Name:           obsctl
Version:        0.7.0
Release:        14%{?dist}
License:        GPL-2.0-or-later
Summary:        Unified high level interface for common actions with the Open Build Service
URL:            https://gitlab.com/datto/engineering/DevOps/obsctl
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core

BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(rpm)
BuildRequires:  python3dist(urlgrabber)
BuildRequires:  python3dist(osc)

Requires:       osc

# For the source services obsctl uses
# For specimport, tarimport, and scratchbuild
Requires:       obs-service-download_files
# For tarimport and scratchbuild
Requires:       obs-service-extract_file
# For scratchbuild
Requires:       obs-service-set_version

%description
This is a command line interface to simplify the packaging and deploy process
for packages built in the openSUSE Open Build Service. This utility functions
in a non-interactive manner allowing it to be utilized in continuous integration
and continuous deployment infrastructure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%build
%py3_build

%install
%py3_install

# Setup obsauth ghost config file
mkdir -p %{buildroot}%{_sysconfdir}/obsctl
touch %{buildroot}%{_sysconfdir}/obsctl/obsauth.json

%files
%doc README.md TODO contrib obsauth.json.dist
%license COPYING
%dir %{_sysconfdir}/obsctl
%ghost %{_sysconfdir}/obsctl/obsauth.json
%{_bindir}/obsctl
%{python3_sitelib}/obsctl-*.egg-info/
%{python3_sitelib}/obsctl/

%changelog
%autochangelog
