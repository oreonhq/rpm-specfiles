%global source0_hash 461b0286c57c5453cad8e715df0c7ea2055ca465b303afb878e46a44de81418e

%global srcname uv-dynamic-versioning

Name:           python-uv-dynamic-versioning
Version:        0.12.0
Release:        %autorelease
Summary:        Dynamic versioning based on VCS tags

License:        MIT
URL:            https://github.com/ninoseki/uv-dynamic-versioning
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
# For autosetup -S git:
BuildRequires:  git-core
BuildRequires:  %{py3_dist gitpython}
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Dynamic versioning based on VCS tags for uv/hatch project.}

%description %_description

%package -n python3-uv-dynamic-versioning
Summary:        %{summary}

%description -n python3-uv-dynamic-versioning %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# -S git: tests need to run in a git repository:
%autosetup -p1 -n %{srcname}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l uv_dynamic_versioning

%check
%pyproject_check_import
%pytest

%files -n python3-uv-dynamic-versioning -f %{pyproject_files}
%doc README.md
%{_bindir}/uv-dynamic-versioning

%changelog
%autochangelog
