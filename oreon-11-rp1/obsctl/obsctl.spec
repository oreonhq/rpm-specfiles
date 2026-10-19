%global source0_hash e5e0eb85ea3e6ae2943e491b41cabe9921e46cedf203160c0aaabd20dab30001
Name:           obsctl
Version:        0.7.0
Release:        1%{?dist}
License:        GPL-2.0-or-later
Summary:        Unified high level interface for common actions with the Open Build Service
URL:            https://gitlab.com/datto/engineering/DevOps/obsctl
Source0:        https://gitlab.com/datto/engineering/DevOps/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       osc
Requires:       obs-service-download_files
Requires:       obs-service-extract_file
Requires:       obs-service-set_version
# oreon:deps
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(osc)
BuildRequires:  python3dist(rpm)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urlgrabber)
# /oreon:deps
%description
This is a command line interface to simplify the packaging and deploy process
for packages built in the openSUSE Open Build Service. This utility functions
in a non-interactive manner allowing it to be utilized in continuous integration
and continuous deployment infrastructure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
%install
%py3_install
mkdir -p %{buildroot}%{_sysconfdir}/obsctl
touch %{buildroot}%{_sysconfdir}/obsctl/obsauth.json
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
