%global source0_hash 2916f788564faa87470a7bd0e96e76b35feeb7495cc00665b3ffd60326d05991

# hatchling is not supported in Python 3.6 releases (epel8)
%if 0%{?rhel} == 8
%global with_hatchling 0
%else
%global with_hatchling 1
%endif

Name:           fedpkg
Version:        1.47
Release:        5%{?dist}
Summary:        Fedora utility for working with dist-git

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pagure.io/fedpkg
Source0:        https://pagure.io/releases/fedpkg/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  pkgconfig
BuildRequires:  bash-completion
BuildRequires:  git

Requires:       koji
Requires:       redhat-rpm-config

# This package redefines __python and can use the python_ macros
%global __python %{__python3}

BuildRequires:  python3-devel
BuildRequires:  python3-rpkg >= 1.69-2
BuildRequires:  python3-distro
%if 0%{?with_hatchling}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
%else
BuildRequires:  python3-setuptools
%endif
# For testing
BuildRequires:  python3-pytest
BuildRequires:  python3-bugzilla
BuildRequires:  python3-freezegun
BuildRequires:  python3-bodhi-client

Requires:       python3-bugzilla
Requires:       python3-rpkg >= 1.69-2
Requires:       python3-distro
Requires:       python3-openidc-client >= 0.6.0
Requires:       python3-bodhi-client
%if !0%{?with_hatchling}
Requires:       python3-setuptools
%endif
Recommends:     fedora-packager
Recommends:     fedpkg-completion

Patch0:         0001-request-unretirement-fix-unittests.patch
Patch1:         0002-Check-the-correct-sorting-of-imports-from-now-on.patch

%description
Provides the fedpkg command for working with dist-git

%package        -n fedpkg-stage
Summary:        Fedora utility for working with dist-git
Requires:       %{name} = %{version}-%{release}

%description    -n fedpkg-stage
Provides the fedpkg command for working with dist-git

%package        -n fedpkg-completion
Summary:        The command-line completion support for fedpkg based on python-argcomplete
Requires:       %{name} = %{version}-%{release}

%description    -n fedpkg-completion
This subpackage provides the command-line completion for the fedpkg CLI
via the python-argcomplete framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if 0%{?with_hatchling}
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?with_hatchling}
%pyproject_wheel
%else
%py_build
%endif
%{python3} doc/fedpkg_man_page.py > fedpkg.1
register-python-argcomplete --shell bash fedpkg > fedpkg.bash
%if 0%{?with_hatchling}
# argcomplete version in EPEL8 does not have support for fish
register-python-argcomplete --shell fish fedpkg > fedpkg.fish
%if 0%{?rhel} != 9
register-python-argcomplete --shell zsh fedpkg > fedpkg.zsh
%endif
%endif

%install
%if 0%{?with_hatchling}
%pyproject_install
%pyproject_save_files -l %{name}
%else
%py_install
%endif
%{__install} -d %{buildroot}%{_mandir}/man1
%{__install} -p -m 0644 fedpkg.1 %{buildroot}%{_mandir}/man1
%{__install} -D -p -m 0644 fedpkg.bash -t %{buildroot}%{bash_completions_dir}
%if 0%{?with_hatchling}
%{__install} -D -p -m 0644 fedpkg.fish -t %{buildroot}%{fish_completions_dir}
%if 0%{?rhel} != 9
%{__install} -D -p -m 0644 fedpkg.zsh %{buildroot}%{zsh_completions_dir}/_fedpkg
%endif
# config file /etc/rpkg/fedpkg.conf is extracted to %{buildroot}/usr/etc/... by pyproject_install
%{__install} -d %{buildroot}%{_sysconfdir}
mv %{buildroot}/usr/etc/* %{buildroot}%{_sysconfdir}
%endif

%check
%if 0%{?with_hatchling}
%pyproject_check_import
%endif
%pytest

%if 0%{?with_hatchling}
%files -f %{pyproject_files}
%else
%files
# For noarch packages: sitelib
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py*.egg-info
%endif
%license COPYING
%doc README.rst CONTRIBUTING.md CHANGELOG.rst
%config(noreplace) %{_sysconfdir}/rpkg/fedpkg.conf
%{_bindir}/%{name}
%{_mandir}/*/*

%files -n fedpkg-stage
%{_bindir}/%{name}-stage
%config(noreplace) %{_sysconfdir}/rpkg/fedpkg-stage.conf

%files -n fedpkg-completion
%config(noreplace) %{bash_completions_dir}/fedpkg.bash
%if 0%{?with_hatchling}
%config(noreplace) %{fish_completions_dir}/fedpkg.fish
%if 0%{?rhel} != 9
%config(noreplace) %{zsh_completions_dir}/_fedpkg
%endif
%endif

%changelog
%autochangelog
