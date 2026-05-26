%bcond tests %{undefined rhel}

Name:           python-fasteners
Version:        0.20
Release:        %autorelease
Summary:        A python package that provides useful locks

License:        Apache-2.0
URL:            https://github.com/harlowja/fasteners
# We need to use the GitHub archive instead of the PyPI sdist to get tests.
Source:        https://github.com/harlowja/fasteners/archive/0.20/fasteners-0.20.tar.gz
# oreon url source checksums begin
%global source0_sha256 393f0d516af101304390da79f702e2a4e03da50d0b0c5bacdb17e81ddc816148
%global source0_file fasteners-0.20.tar.gz
# oreon url source checksums end

BuildSystem:            pyproject
%if %{with tests}
BuildOption(generate_buildrequires): -g test
%endif
BuildOption(install):   -l fasteners
BuildOption(check):     -e 'fasteners.pywin32*'

BuildRequires:  tomcli

BuildArch:      noarch

%global common_description %{expand:
Cross platform locks for threads and processes}

%description %{common_description}


%package -n python3-fasteners
Summary:        A python package that provides useful locks

%description -n python3-fasteners %{common_description}


%prep -a
# Omit eventlet integration tests: retired since Fedora 41
tomcli set pyproject.toml lists delitem dependency-groups.test eventlet


%check -a
%if %{with tests}
# See notes in %%prep:
ignore="${ignore-} --ignore=tests/test_eventlet.py"

%pytest ${ignore-} -rs -v
%endif


%files -n python3-fasteners -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20-1
- Import
