%global source0_hash 17e12024961e20e361cfd767d54b103f38009904e8e1da97ccfc451435cd4fcb

Name:           rpkg
Version:        1.69
Release:        6%{?dist}

Summary:        Python library for interacting with rpm+git
# Automatically converted from old format: GPLv2+ and LGPLv2 - reviewed
# and converted to SPDX license expression
License:        GPL-2.0-or-later AND LGPL-2.1-only
URL:            https://pagure.io/rpkg
BuildArch:      noarch
Source0:        https://pagure.io/releases/rpkg/%{name}-%{version}.tar.gz

# RHEL7 is currently the only release that is built for Python 2.
%if 0%{?rhel} == 7
%global with_python2 1
%global with_python3 0
# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?__python2: %global __python2 %{__python}}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%else
# Disable python2 build by default
%global with_python2 0
# Enable python3 build by default
%global with_python3 1
%endif

# No support for setup.py since Python 3.12 (RHEL 10)
# hatchling is supported in >Python 3.6 releases (RHEL 8)
%if 0%{?rhel} && 0%{?rhel} <= 8
%global with_hatchling 0
%else
%global with_hatchling 1
%endif

# Fix for bug 1579367
# Due to https://pagure.io/koji/issue/912, python[23]-koji package does not
# have egginfo.
# rpm-py-installer is required as a proxy to install RPM python binding
# library, so rpm is the actual requirement that must be present in the
# requires.txt. But, rpkg has to work in all active Fedora and EPEL releases,
# and there is only old rpm-python package in EL6 and 7, so just simply to
# remove rpm-py-installer for now.
%if !0%{?with_hatchling}
Patch0:         remove-koji-and-rpm-py-installer-from-requires.patch
%endif
%if 0%{?with_python2}
Patch1:         0001-Remove-Environment-Markers-syntax.patch
%endif
Patch2:         0002-Execute-shell-command-Non-interactive-stdin.patch
Patch3:         0003-Use-ruff-code-checker-instead-of-bandit.patch
Patch4:         0004-update-interactive-editor-is-broken.patch
Patch5:         0005-Check-the-correct-sorting-of-imports-from-now-on.patch
Patch6:         0006-_run_command-timeout-is-not-supported-in-Python-2.patch
Patch7:         0007-Submitting-the-module-build-duplicate-timeout.patch

%description
Python library for interacting with rpm+git

%if 0%{?with_python2}
%package -n python2-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{name}}

BuildRequires:  python2-devel

# We br these things for man page generation due to imports
BuildRequires:  rpmlint
BuildRequires:  rpmdevtools
BuildRequires:  python2-koji
BuildRequires:  python2-cccolutils
BuildRequires:  PyYAML
BuildRequires:  GitPython
BuildRequires:  python-pycurl
BuildRequires:  python-requests
BuildRequires:  python-requests-gssapi
BuildRequires:  python-six
BuildRequires:  python2-argcomplete
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools

Requires:       mock
Requires:       redhat-rpm-config
Requires:       rpm-build
Requires:       rpmlint
Requires:       rpmdevtools
Requires:       python2-argcomplete
Requires:       python2-cccolutils
Requires:       python2-koji
Requires:       PyYAML
Requires:       GitPython
Requires:       python-pycurl
Requires:       python-requests
Requires:       python-requests-gssapi
Requires:       python-six
Requires:       rpm-python

Requires:       %{name}-common = %{version}-%{release}

Conflicts:      fedpkg < 1.26

# Backward compatibility with capability pyrpkg
Provides: pyrpkg = %{version}-%{release}
# All old versions before 1.49-1 should not be used anymore
Obsoletes: pyrpkg < 1.49-2

%description -n python2-%{name}
A python library for managing RPM package sources in a git repository.
%endif
# end of python2 section

%if 0%{?with_python3}
%package -n python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}
# Obsolete python2-rpkg (remove after Fedora29)
%if 0%{?with_python2} == 0
Obsoletes:      python2-rpkg < %{version}-%{release}
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-GitPython
BuildRequires:  python3-koji
%if 0%{?rhel}
BuildRequires:  python3-gobject-base
BuildRequires:  libmodulemd
BuildRequires:  python3-requests-gssapi
%else
BuildRequires:  python3-libmodulemd
%endif
BuildRequires:  python3-argcomplete
BuildRequires:  python3-cccolutils
BuildRequires:  python3-openidc-client
BuildRequires:  python3-pycurl
BuildRequires:  python3-six
BuildRequires:  python3-requests
BuildRequires:  python3-pytest
BuildRequires:  python3-PyYAML
BuildRequires:  rpmlint
BuildRequires:  rpmdevtools
%if 0%{?with_hatchling}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-pip
%else
BuildRequires:  python3-setuptools
%endif

Requires:       mock
Requires:       redhat-rpm-config
Requires:       rpm-build
Requires:       rpmlint
Requires:       rpmdevtools

Requires:       python3-argcomplete
Requires:       python3-GitPython
Requires:       python3-cccolutils
Requires:       python3-koji
%if 0%{?rhel}
Requires:       python3-gobject-base
Requires:       libmodulemd
Requires:       python3-requests-gssapi
%else
Requires:       python3-libmodulemd
Requires:       python3-rpmautospec
%endif
Requires:       python3-rpm
Requires:       python3-pycurl
Requires:       python3-six
Requires:       python3-PyYAML

Requires:       %{name}-common = %{version}-%{release}

Conflicts:      fedpkg < 1.26

%description -n python3-%{name}
A python library for managing RPM package sources in a git repository.
%endif
# end of python3 section

%package common
Summary:        Common files for %{name}

# Files were moved from python2-rpkg in that version
Conflicts:      python2-rpkg < 1.52-2
Conflicts:      pyrpkg < 1.52-2

%description common
Common files for python2-%{name} and python3-%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if 0%{?with_python2}
%{__python2} setup.py build
%endif

%if 0%{?with_python3}
%if 0%{?with_hatchling}
%pyproject_wheel
%else
%py3_build
%endif
%endif

%install
%if 0%{?with_python2}
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%endif

%if 0%{?with_python3}
%if 0%{?with_hatchling}
%pyproject_install
%pyproject_save_files -l pyrpkg
%else
%py3_install
%endif
%endif

# Create configuration directory to holding downstream clients config files
# that are built on top of rpkg
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/rpkg

example_cli_dir=$RPM_BUILD_ROOT%{_datadir}/%{name}/examples/cli
%{__install} -d $example_cli_dir

# Install example CLI to rpkg own data directory
%{__install} -d ${example_cli_dir}%{_bindir}
%{__install} -d ${example_cli_dir}%{_sysconfdir}/bash_completion.d
%{__install} -d ${example_cli_dir}%{_sysconfdir}/rpkg

%{__install} -p -m 0644 bin/rpkg ${example_cli_dir}%{_bindir}
%{__install} -p -m 0644 etc/bash_completion.d/rpkg.bash ${example_cli_dir}%{_sysconfdir}/bash_completion.d
%{__install} -p -m 0644 etc/rpkg/rpkg.conf ${example_cli_dir}%{_sysconfdir}/rpkg

%check
%if 0%{?with_python2}
%{__python2} -m nose tests
%endif

%if 0%{?with_python3}
%if 0%{?with_hatchling}
%pyproject_check_import
%endif
%pytest
%endif

%if 0%{?with_python2}
%files -n python2-%{name}
%doc README.rst CONTRIBUTING.md CHANGELOG.rst
%license COPYING COPYING-koji LGPL
# For noarch packages: sitelib
%{python2_sitelib}/pyrpkg
%{python2_sitelib}/%{name}-%{version}-py*.egg-info
%endif

%if 0%{?with_python3}
%if 0%{?with_hatchling}
%files -n python3-%{name} -f %{pyproject_files}
%else
%files -n python3-%{name}
%{python3_sitelib}/pyrpkg
%{python3_sitelib}/%{name}-%{version}-py*.egg-info
%endif
%doc README.rst CONTRIBUTING.md CHANGELOG.rst
%license COPYING COPYING-koji LGPL
%endif

%files common
%{_datadir}/%{name}
%{_sysconfdir}/rpkg

%changelog
%autochangelog
