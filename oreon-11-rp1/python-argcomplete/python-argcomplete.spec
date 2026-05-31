%global source0_hash 62e8ed4fd6a45864acc8235409461b72c9a28ee785a2011cc5eb78318786c89c

# Disable check to avoid pulling unwanted package (fish) into RHEL 9
%if 0%{?rhel} >= 9 && !0%{?epel} || (0%{?oreon} >= 11)
%bcond_with check
%else
%bcond_without check
%endif

# Enable all tests (requires check to be true)
%bcond all_tests 1

Name:          python-argcomplete
Summary:       Bash tab completion for argparse
Version:       3.6.3
Release:       %autorelease
License:       Apache-2.0
URL:           https://github.com/kislyuk/argcomplete
Source0:        https://files.pythonhosted.org/packages/source/a/argcomplete/argcomplete-3.6.3.tar.gz

BuildRequires: python3-devel

%if %{with check}
BuildRequires: tcsh
BuildRequires: fish
BuildRequires: zsh
%endif

BuildArch:     noarch

%global _description %{expand:
Tab complete all the things!

Argcomplete provides easy, extensible command line tab completion of
arguments for your Python application.

It makes two assumptions:

 - You're using bash or zsh as your shell
 - You're using argparse to manage your command line arguments/options
 
Argcomplete is particularly useful if your program has lots of options
or subparsers, and if your program can dynamically suggest completions
for your argument/option values (for example, if the user is browsing
resources over the network).}

%description %_description

%package -n python3-argcomplete
Summary:        %{summary}
%description -n python3-argcomplete %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n argcomplete-%{version}
# Remove useless BRs (aka linters)
sed -i -r -e '/test = /s/"(coverage|ruff|mypy)"[, ]*//g' pyproject.toml

# https://github.com/kislyuk/argcomplete/issues/255
# https://github.com/kislyuk/argcomplete/issues/256
sed -i -e "1s|#!.*python.*|#!%{__python3}|" test/prog argcomplete/scripts/*
sed -i -e "s|python |python3 |" test/test.py

# Remove shebang from installed scripts
sed -i '/^#!/d' argcomplete/scripts/*.py

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files argcomplete


# do not attempt to install to %%bash_completions_dir, see https://bugzilla.redhat.com/2211862
install -Dp -m0644 argcomplete/bash_completion.d/_%{name} %{buildroot}%{_sysconfdir}/bash_completion.d/_%{name}

%if %{with check}
%check
# Disable pip build isolation to make the tests work in offline environment
# Fixes https://bugzilla.redhat.com/2417961
export PIP_NO_BUILD_ISOLATION=0

%if %{with all_tests}
%{py3_test_envvars} %{python3} test/test.py -v
%else
# Disable zsh tests. They fail for mysterious reasons.
# https://github.com/kislyuk/argcomplete/issues/447
%{py3_test_envvars} %{python3} test/test.py -v -k "TestArgcomplete"
%{py3_test_envvars} %{python3} test/test.py -v -k "TestBash"
%{py3_test_envvars} %{python3} test/test.py -v -k "TestCheckModule"
%{py3_test_envvars} %{python3} test/test.py -v -k "TestSplitLine"
%endif
%endif

%files -n python3-argcomplete -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst
%{_bindir}/activate-global-python-argcomplete
%{_bindir}/python-argcomplete-check-easy-install-script
%{_bindir}/register-python-argcomplete
%{_sysconfdir}/bash_completion.d/_%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.3-1
- Import
