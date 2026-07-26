%global source0_hash 5f02ad279a783b305a0e6a28acebd55dd344dc1fd5a9623180f9cbd7d8333fc5

Name:           python-confuse
Version:        2.2.0
Release:        %autorelease
Summary:        A Python module for handling YAML configuration files

License:        MIT
URL:            https://github.com/beetbox/confuse
Source0:        %{url}/archive/v%{version}/confuse-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Confuse is a configuration library for Python that uses YAML. It takes care of
defaults, overrides, type checking, command-line integration, environment
variable support, human-readable errors, and standard OS-specific locations.}

%description %{_description}

%package -n python3-confuse
Summary:        %{summary}

%description -n python3-confuse %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n confuse-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files confuse

%check

%files -n python3-confuse -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
