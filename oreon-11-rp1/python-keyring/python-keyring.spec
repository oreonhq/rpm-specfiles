%global source0_hash fe01bd85eb3f8fb3dd0405defdeac9a5b4f6f0439edbb3149577f244a2e8245b
%bcond tests 1
%bcond desktop_tests 1
Name:           python-keyring
Version:        25.7.0
Release:        1%{?dist}
Summary:        Store and access your passwords safely
License:        MIT
URL:            https://github.com/jaraco/keyring
Source0:        https://files.pythonhosted.org/packages/source/k/keyring/keyring-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%if %{with desktop_tests}
%endif
%endif
%global desc %{expand:
The Python keyring library provides an easy way to access the system keyring
service from python. It can be used in any application that needs safe password
storage.
These recommended keyring backends are supported:
  • macOS Keychain
  • Freedesktop Secret Service supports many DE including GNOME (requires
    secretstorage)
  • KDE4 & KDE5 KWallet (requires dbus)
  • Windows Credential Locker
Other keyring implementations are available through third-party backends.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-keyring = %{version}-%{release}
# /oreon:deps
%package -n       python3-keyring+test
Summary:        Metapackage for python3-keyring test extras
Requires:       python3-keyring = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(keyring[test]) = %{version}-%{release}

%description -n python3-keyring+test
Metapackage for python3-keyring test extras.

%package -n       python3-keyring+doc
Summary:        Metapackage for python3-keyring doc extras
Requires:       python3-keyring = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Provides:       python3dist(keyring[doc]) = %{version}-%{release}

%description -n python3-keyring+doc
Metapackage for python3-keyring doc extras.

%package -n       python3-keyring+check
Summary:        Metapackage for python3-keyring check extras
Requires:       python3-keyring = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(keyring[check]) = %{version}-%{release}

%description -n python3-keyring+check
Metapackage for python3-keyring check extras.

%package -n       python3-keyring+cover
Summary:        Metapackage for python3-keyring cover extras
Requires:       python3-keyring = %{version}-%{release}
Provides:       python3dist(keyring[cover]) = %{version}-%{release}

%description -n python3-keyring+cover
Metapackage for python3-keyring cover extras.

%package -n       python3-keyring+enabler
Summary:        Metapackage for python3-keyring enabler extras
Requires:       python3-keyring = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(keyring[enabler]) = %{version}-%{release}

%description -n python3-keyring+enabler
Metapackage for python3-keyring enabler extras.

%package -n       python3-keyring+type
Summary:        Metapackage for python3-keyring type extras
Requires:       python3-keyring = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Provides:       python3dist(keyring[type]) = %{version}-%{release}

%description -n python3-keyring+type
Metapackage for python3-keyring type extras.

%package -n       python3-keyring+completion
Summary:        Metapackage for python3-keyring completion extras
Requires:       python3-keyring = %{version}-%{release}
Requires:       python3dist(shtab) >= 1.1.0
Provides:       python3dist(keyring[completion]) = %{version}-%{release}

%description -n python3-keyring+completion
Metapackage for python3-keyring completion extras.

%description %desc

%package -n python3-keyring
Summary:        Python 3 library to access the system keyring service
Recommends:     python3-keyring+completion = %{version}-%{release}
# oreon:reqs
Requires:       python3dist(importlib-metadata) >= 4.11.4
Requires:       python3dist(jeepney) >= 0.4.2
Requires:       python3dist(pywin32-ctypes) >= 0.2.0
Requires:       python3dist(secretstorage) >= 3.2
# /oreon:reqs
%description -n python3-keyring %desc

# We don’t use “%%pyproject_extras_subpkg -n python3-keyring completion”
# because we want to add the completion scripts to the files list and provide a
# custom summary and description.
%package -n python3-keyring+completion
Summary:        Shell completion support for the keyring command
Requires:       python3-keyring = %{version}-%{release}
%description -n python3-keyring+completion
This package:

• Makes sure the “completion” extra dependencies are installed
• Installs the actual shell completion scripts

There may be additional requirements to enable completion support *in general*
for a particular shell. For example, bash needs the bash-completion package to
be installed.

%prep

%autosetup -p1
# This will be installed in site-packages without the executable bit set, so
# the shebang should be removed.
sed --regexp-extended --in-place '1{/^#!/d}' keyring/cli.py

# The coherent.licensed build dependency copies a license file from outside the
# repository; see https://github.com/jaraco/skeleton/issues/174 for an overview
# of how this is supposed to work. This would need some sort of workaround if
# we were building from a GitHub source archive, since its normal operation
# requires network access. Fortunately, we’re using the PyPI sdist, so the
# LICENSE file is already copied in, and we can simply omit the dependency.
%pyproject_patch_dependency coherent.licensed:ignore

%install
%pyproject_install
install --directory '%{buildroot}%{bash_completions_dir}'
%{py3_test_envvars} keyring --print-completion bash |
    tee '%{buildroot}%{bash_completions_dir}/keyring'
install --directory '%{buildroot}%{zsh_completions_dir}'
%{py3_test_envvars} keyring --print-completion zsh |
    tee '%{buildroot}%{zsh_completions_dir}/_keyring'
install --directory '%{buildroot}%{_sysconfdir}/profile.d'
%{py3_test_envvars} keyring --print-completion tcsh |
    tee '%{buildroot}%{_sysconfdir}/profile.d/keyring.csh'
install --directory '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man --no-info --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/keyring.1' keyring
%oreon_autofiles python3-keyring usr/lib/python3*/site-packages/keyring* usr/lib64/python3*/site-packages/keyring* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/keyring* usr/lib64/python3*/site-packages/keyring* usr/bin/*

%build

%pyproject_wheel
%check

%if %{with tests}
%if %{with desktop_tests}
%global __pytest xwfb-run -- pytest
%endif
%pytest -k "${k-}" ${ignore-} -rs
%endif
%files
%files -n python3-keyring -f %{oreon_filedir}/python3-keyring.list

%changelog

%autochangelog

