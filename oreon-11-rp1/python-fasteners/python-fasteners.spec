%global source0_hash 393f0d516af101304390da79f702e2a4e03da50d0b0c5bacdb17e81ddc816148

%bcond_without tests

Name:           python-fasteners
Version:        0.20
Release:        %autorelease
Summary:        A python package that provides useful locks

License:        Apache-2.0
URL:            https://github.com/harlowja/fasteners
Source0:        https://github.com/harlowja/fasteners/archive/0.20/fasteners-0.20.tar.gz#/python-fasteners-0.20.tar.gz

BuildRequires:  pyproject-rpm-macros
BuildRequires:  tomcli

BuildArch:      noarch

%global common_description %{expand:
Cross platform locks for threads and processes}

%description %{common_description}


%package -n python3-fasteners
Summary:        A python package that provides useful locks

%description -n python3-fasteners %{common_description}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n fasteners-%{version}
tomcli set pyproject.toml lists delitem dependency-groups.test eventlet


%generate_buildrequires
%pyproject_buildrequires -g test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fasteners


%check -a
%if %{with tests}
ignore="${ignore-} --ignore=tests/test_eventlet.py"

%pytest ${ignore-} -rs -v
%endif


%files -n python3-fasteners -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20-1
- Import
