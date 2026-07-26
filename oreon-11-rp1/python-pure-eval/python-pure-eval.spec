%global source0_hash 5f4e983f40564c576c7c8635ae88db5956bb2229d7e9237d03b3c0b0190eaf42

Name:           python-pure-eval
Version:        0.2.3
Release:        %autorelease
Summary:        Safely evaluate AST nodes without side effects

License:        MIT
URL:            http://github.com/alexmojaki/pure_eval
Source0:        %{pypi_source pure_eval}
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python package that lets you safely evaluate certain AST nodes
without triggering arbitrary code that may have unwanted side effects.}

%description %_description

%package -n     python3-pure-eval
Summary:        %{summary}

%description -n python3-pure-eval %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pure_eval-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pure_eval

%check
%tox

%files -n python3-pure-eval -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
