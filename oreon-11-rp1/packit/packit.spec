%global source0_hash 336a5bd853f99cc2b70147450ecfac09636acc26013d2cf73e732eb1c1a75acd

# Testing dependencies: deepdiff, flexmock are missing on EPEL 9. Cannot use testing environment
%if 0%{?el9}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           packit
Version:        1.15.1
Release:        1%{?dist}
Summary:        A tool for integrating upstream projects with Fedora operating system

License:        MIT
URL:            https://github.com/packit/packit
Source0:        %{pypi_source packitos}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(click-man)
Requires:       python3-packit = %{version}-%{release}

%description
This project provides tooling and automation to integrate upstream open source
projects into Fedora operating system.

%package -n     python3-packit
Summary:        %{summary}
# new-sources
Requires:       fedpkg
Requires:       git-core
# kinit
Requires:       krb5-workstation
# rpmbuild
Requires:       rpm-build
# bumpspec
Requires:       rpmdevtools
# Copying files between repositories
Requires:       rsync

Recommends:       osh-cli

%description -n python3-packit
Python library for Packit,
check out packit package for the executable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n packitos-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x testing}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files packit
PYTHONPATH="%{buildroot}%{python3_sitelib}" click-man packit --target %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{bash_completions_dir}
cp files/bash-completion/packit %{buildroot}%{bash_completions_dir}/packit

%files
%license LICENSE
%{_bindir}/packit
%{_mandir}/man1/packit*.1*
%{bash_completions_dir}/packit

%files -n python3-packit -f %{pyproject_files}
# Epel9 does not tag the license file in pyproject_files as a license. Manually install it in this case
%if 0%{?el9}
%license LICENSE
%endif
%doc README.md

%changelog
%autochangelog
