%global source0_hash cf885e8679a3aa9cb5db54674bcf540f11a114e8e87b63bb31522ccdf0bf348c
Name:           tmt
Version:        1.78.0
Release:        1%{?dist}
Summary:        Test Management Tool
License:        MIT
URL:            https://github.com/teemtee/tmt
Source0:        https://files.pythonhosted.org/packages/source/t/tmt/tmt-%{version}.tar.gz
BuildArch:      noarch
Requires:       git-core rsync sshpass
Recommends:     bash-completion
Recommends:     ansible-core
%py_provides    python3-tmt
%global _metapackage_description %{expand:
This is a metapackage bringing in extra dependencies for tmt.
It contains no code, just makes sure the dependencies are installed.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tmt = %{version}-%{release}
# /oreon:deps
%description
The tmt Python module and command line tool implement the test
metadata specification (L1 and L2) and allows easy test execution.

%package -n     tmt+test-convert
Summary:        Dependencies required for tmt test import and export
Provides:       tmt-test-convert == %{version}-%{release}
Requires:       tmt == %{version}-%{release}
Requires:       make
Requires:       python3-bugzilla
Requires:       python3-nitrate
Requires:       python3-html2text
Requires:       python3-markdown
%description -n tmt+test-convert %_metapackage_description

%package -n     tmt+provision-container
Summary:        Dependencies required for tmt container provisioner
Provides:       tmt-provision-container == %{version}-%{release}
Requires:       tmt == %{version}-%{release}
Requires:       podman
Requires:       ansible-collection-containers-podman
%description -n tmt+provision-container %_metapackage_description

%package -n     tmt+provision-virtual
Summary:        Dependencies required for tmt virtual machine provisioner
Provides:       tmt-provision-virtual == %{version}-%{release}
Requires:       tmt == %{version}-%{release}
Requires:       python3-testcloud >= 0.11.7
Requires:       libvirt-daemon-config-network
Requires:       openssh-clients
Recommends:     qemu-kvm-core
%description -n tmt+provision-virtual %_metapackage_description

%package -n     tmt+provision-bootc
Summary:        Dependencies required for tmt bootc machine provisioner
Provides:       tmt-provision-bootc == %{version}-%{release}
Requires:       tmt == %{version}-%{release}
Requires:       tmt+provision-virtual == %{version}-%{release}
Requires:       podman
%description -n tmt+provision-bootc %_metapackage_description

%package -n     tmt+provision-beaker
Summary:        Dependencies required for tmt beaker provisioner
Provides:       tmt-provision-beaker == %{version}-%{release}
Requires:       tmt == %{version}-%{release}
Requires:       python3-mrack-beaker
%description -n tmt+provision-beaker %_metapackage_description

%package -n     tmt+provision-mock
Summary:        Dependencies required for tmt mock provisioner
Provides:       tmt-provision-mock == %{version}-%{release}
Requires:       tmt == %{version}-%{release}
Requires:       mock
%description -n tmt+provision-mock %_metapackage_description

# Replace with pyproject_extras_subpkg at some point
%package -n     tmt+all
Summary:        Extra dependencies for the Test Management Tool
Provides:       tmt-all == %{version}-%{release}
Requires:       tmt+export-polarion == %{version}-%{release}
Requires:       tmt+link-jira == %{version}-%{release}
Requires:       tmt+prepare-artifact == %{version}-%{release}
Requires:       tmt+provision-beaker == %{version}-%{release}
Requires:       tmt+provision-bootc == %{version}-%{release}
Requires:       tmt+provision-container == %{version}-%{release}
Requires:       tmt+provision-mock == %{version}-%{release}
Requires:       tmt+provision-virtual == %{version}-%{release}
Requires:       tmt+report-junit == %{version}-%{release}
Requires:       tmt+report-polarion == %{version}-%{release}
Requires:       tmt+test-convert == %{version}-%{release}
%description -n tmt+all
All extra dependencies of the Test Management Tool. Install this
package to have all available plugins ready for testing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir tmt-%{version}
%oreon_prep
%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
cp docs/header.txt man.rst
tail -n+8 docs/overview.rst >> man.rst
sed '/versionadded::/d' -i man.rst
rst2man man.rst > tmt.1
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 tmt.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -pm 644 completions/bash/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}/etc/%{name}/
install -pm 644 %{name}/steps/provision/mrack/mrack* %{buildroot}/etc/%{name}/
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
