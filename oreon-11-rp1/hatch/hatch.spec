%global source0_hash 4117c61a1c3c1f53c42c95bbd71d266719441813927685a2e66d082ff6c85e5c
%bcond tests 1
Name:           hatch
Version:        1.16.4%{?commit:^%{snapdate}.%{sub %{commit} 1 7}}
Release:        1%{?dist}
Summary:        A modern project, package, and virtual env manager
%if %{undefined commit}
%global tag hatch-v%{version}
%else
%global tag %{commit}
%endif
%global archivename hatch-%{tag}
License:        MIT
URL:            https://github.com/pypa/hatch
Source0:        https://github.com/pypa/%{name}/archive/%{name}-v1.16.4/%{name}-%{name}-v1.16.4.tar.gz
Source100:      hatch.1
Source200:      hatch-build.1
Source300:      hatch-clean.1
Source400:      hatch-config.1
Source410:      hatch-config-explore.1
Source420:      hatch-config-find.1
Source430:      hatch-config-restore.1
Source440:      hatch-config-set.1
Source450:      hatch-config-show.1
Source460:      hatch-config-update.1
Source500:      hatch-dep.1
Source510:      hatch-dep-hash.1
Source520:      hatch-dep-show.1
Source521:      hatch-dep-show-requirements.1
Source522:      hatch-dep-show-table.1
Source600:      hatch-env.1
Source610:      hatch-env-create.1
Source620:      hatch-env-find.1
Source630:      hatch-env-prune.1
Source640:      hatch-env-remove.1
Source650:      hatch-env-run.1
Source660:      hatch-env-show.1
Source700:      hatch-new.1
Source800:      hatch-project.1
Source810:      hatch-project-metadata.1
Source900:      hatch-publish.1
Source1000:     hatch-run.1
Source1100:     hatch-shell.1
Source1200:     hatch-status.1
Source1300:     hatch-version.1
Source1400:     hatch-fmt.1
Source1500:     hatch-python.1
Source1510:     hatch-python-find.1
Source1520:     hatch-python-install.1
Source1530:     hatch-python-remove.1
Source1540:     hatch-python-show.1
Source1550:     hatch-python-update.1
Source1600:     hatch-self.1
Source1610:     hatch-self-report.1
Source1620:     hatch-self-restore.1
Source1630:     hatch-self-update.1
Source1700:     hatch-test.1
%if %{with tests}
%endif
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       git-core
# oreon:deps
BuildRequires:  git-core
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-randomly)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(pytest-xdist[psutil])
BuildRequires:  tomcli
# /oreon:deps
%description
Hatch is a modern, extensible Python project manager.

Features:

  • Standardized build system with reproducible builds by default
  • Robust environment management with support for custom scripts and UV
  • Test execution with known best practices
  • Static analysis with sane defaults
  • Built-in Python script runner
  • Easy publishing to PyPI or other indices
  • Version management
  • Best practice project generation
  • Responsive CLI, ~2-3x faster than equivalent tools

%if %{defined commit}
%prep

%autosetup -p1
# https://hatch.pypa.io/latest/config/environment/
tomcli get hatch.toml -F newline-list envs.hatch-test.extra-dependencies |
  tee _envs.hatch-test.extra-dependencies.txt

%if %{defined commit}
%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%(echo '%{version}' | cut -d '^' -f 1)'
%endif
%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE100}' \
    '%{SOURCE200}' \
    '%{SOURCE300}' \
    '%{SOURCE400}' '%{SOURCE410}' '%{SOURCE420}' '%{SOURCE430}' \
      '%{SOURCE440}' '%{SOURCE450}' '%{SOURCE460}' \
    '%{SOURCE500}' '%{SOURCE510}' '%{SOURCE520}' '%{SOURCE521}' \
      '%{SOURCE522}' \
    '%{SOURCE600}' '%{SOURCE610}' '%{SOURCE620}' '%{SOURCE630}' \
      '%{SOURCE640}' '%{SOURCE650}' '%{SOURCE660}' \
    '%{SOURCE700}' \
    '%{SOURCE800}' '%{SOURCE810}' \
    '%{SOURCE900}' \
    '%{SOURCE1000}' \
    '%{SOURCE1100}' \
    '%{SOURCE1200}' \
    '%{SOURCE1300}' \
    '%{SOURCE1400}' \
    '%{SOURCE1500}' '%{SOURCE1510}' '%{SOURCE1520}' '%{SOURCE1530}' \
      '%{SOURCE1540}' '%{SOURCE1550}'
%oreon_autofiles main

%check

%if %{with tests}
ignore="${ignore-} --ignore=tests/backend/"
k="${k-}${k+ and }not (TestCustomScripts and test_single)"
missing_dists='3.7 3.8 pypy2.7 pypy3.9 pypy3.10 pypy3.11'
for param in ${missing_dists}
do
  k="${k-}${k+ and }not test_custom_source[${param}]"
  k="${k-}${k+ and }not test_installation[${param}]"
done
k="${k-}${k+ and }not (TestDistributionPaths and test_pypy_custom)"
k="${k-}${k+ and }not (TestDistributionVersions and test_pypy_custom)"
k="${k-}${k+ and }not test_project_location_basic_set_first_project"
k="${k-}${k+ and }not test_project_location_complex_set_first_project"
ignore="${ignore-} --ignore=tests/cli/build/test_build.py"
ignore="${ignore-} --ignore=tests/cli/project/test_metadata.py"
ignore="${ignore-} --ignore=tests/workspaces/test_config.py"
ignore="${ignore-} --ignore=tests/cli/clean/test_clean.py"
k="${k-}${k+ and }not test_other_backend_show"
k="${k-}${k+ and }not test_plugin_dependencies_unmet"
k="${k-}${k+ and }not test_set_dynamic"
k="${k-}${k+ and }not test_set_dynamic_downgrade"
k="${k-}${k+ and }not test_show_dynamic"
k="${k-}${k+ and }not test_verbose_output_to_stderr"
k="${k-}${k+ and }not (TestUserAgent and test_user_agent_header_format)"
k="${k-}${k+ and }not (TestDependencies and test_project_dependencies_context_formatting)"
k="${k-}${k+ and }not (TestDependencies and test_context_formatting)"
k="${k-}${k+ and }not test_context_formatting"
%pytest -k "${k-}" ${ignore-} -vv
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
