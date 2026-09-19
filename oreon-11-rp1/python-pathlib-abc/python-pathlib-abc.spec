%global source0_hash fcd56f147234645e2c59c7ae22808b34c364bb231f685ddd9f96885aed78a94c

Name:           python-pathlib-abc
Version:        0.5.2
Release:        %autorelease
Summary:        Backport of pathlib ABCs

License:        PSF-2.0
URL:            https://github.com/barneygale/pathlib-abc
Source:         %{pypi_source pathlib_abc}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-test
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Base classes for pathlib.Path-ish objects. This package is a preview of pathlib
functionality planned for a future release of Python; specifically, it provides
three ABCs that can be used to implement path classes for non-local
filesystems, such as archive files and storage servers: JoinablePath,
ReadablePath, and WritablePath.}

%description %_description

%package -n     python3-pathlib-abc
Summary:        %{summary}

%description -n python3-pathlib-abc %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pathlib_abc-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pathlib_abc

%check
%pytest -ra

%files -n python3-pathlib-abc -f %{pyproject_files}
%doc README.rst CHANGES.rst

%changelog
%autochangelog
