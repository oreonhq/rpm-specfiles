%global source0_hash 6db2cd1b5ab7ff52c6fe8df473d5518b29fe5f0e5ec267fc731272a71e46a5ea

Name:           python-comm
Version:        0.2.3
Release:        %autorelease
Summary:        Jupyter Python Comm implementation, for usage in ipykernel, xeus-python etc.
License:        BSD-3-Clause
URL:            https://github.com/ipython/comm
Source:         %{url}/archive/v%{version}/comm-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Comm provides a way to register a Kernel Comm implementation,
as per the Jupyter kernel protocol. It also provides a base Comm
implementation and a default CommManager that can be used.}

%description %_description

%package -n     python3-comm
Summary:        %{summary}

%description -n python3-comm %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n comm-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files comm

%check
%pytest

%files -n python3-comm -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
