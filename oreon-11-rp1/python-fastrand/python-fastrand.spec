%global source0_hash b105c156bec612f92eb9638f90949af271071e00cc64a556d40852697400e3bf

Name:           python-fastrand
Version:        3.0.8
Release:        %autorelease
Summary:        Fast random number generation in Python

License:        Apache-2.0
URL:            https://github.com/lemire/fastrand
Source:         %{url}/archive/v%{version}/fastrand-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc

%global _description %{expand:
Fast random number generation in an interval in Python using PCG: Up to 10x
faster than random.randint.}

%description %_description

%package -n     python3-fastrand
Summary:        %{summary}

%description -n python3-fastrand %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n fastrand-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fastrand

%check
%pyproject_check_import
%py3_test_envvars %python3 -m timeit -s 'import fastrand' 'fastrand.pcg32bounded(1001)'
%py3_test_envvars %python3 -m timeit -s 'import fastrand' 'fastrand.pcg32randint(100,1000)'

%files -n python3-fastrand -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
