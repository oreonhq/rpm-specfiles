%bcond_without tests

Name:           python-more-itertools
Version:        10.5.0
Release:        %autorelease
Summary:        More routines for operating on Python iterables, beyond itertools
License:        MIT
URL:            https://github.com/more-itertools/more-itertools
Source0:        https://files.pythonhosted.org/packages/source/m/more-itertools/more-itertools-10.5.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 5482bfef7849c25dc3c6dd53a6173ae4795da2a41a80faea6700d9f5846c5da6
%global source0_file more-itertools-10.5.0.tar.gz
# oreon url source checksums end
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Python's itertools library is a gem - you can compose elegant solutions for
a variety of problems with the functions it provides. In more-itertools we
collect additional building blocks, recipes, and routines for working with
Python iterables.}

%description %_description

%package -n python3-more-itertools
Summary:        %{summary}

%description -n python3-more-itertools %_description

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/more-itertools-10.5.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5482bfef7849c25dc3c6dd53a6173ae4795da2a41a80faea6700d9f5846c5da6" || { echo "oreon: Source0 SHA256 mismatch for more-itertools-10.5.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n more-itertools-%{version}

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests: -t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files more_itertools

%if %{with tests}
%check
%tox
%endif

%files -n python3-more-itertools -f %pyproject_files
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.5.0-1
- Prepare for Oreon 11 (RP1)
