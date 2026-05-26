# tests are enabled by default
%bcond_without tests

Name:           python-six
Version:        1.17.0
Release:        %autorelease
Summary:        Python 2 and 3 compatibility utilities

# SPDX
License:        MIT
URL:            https://github.com/benjaminp/six
Source0:        https://files.pythonhosted.org/packages/source/s/six/six-1.17.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81
%global source0_file six-1.17.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-tkinter
%endif

%global _description %{expand:
Six is a Python 2 and 3 compatibility library. It provides utility functions
for smoothing over the differences between the Python versions with the goal
of writing Python code that is compatible on both Python versions.}

%description %{_description}


%package -n python%{python3_pkgversion}-six
Summary:        %{summary}

%description -n python%{python3_pkgversion}-six %{_description}


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/six-1.17.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81" || { echo "oreon: Source0 SHA256 mismatch for six-1.17.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n six-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l six


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-six -f %{pyproject_files}
%doc README.rst documentation/index.rst


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-1
- Import
