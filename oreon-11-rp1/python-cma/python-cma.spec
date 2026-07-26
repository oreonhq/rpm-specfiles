%global source0_hash edd1d1f22d11ebf7a2ccae713bc3838931e31002410d19910d9d7ca9c4911fe1

%global srcname cma
Name:           python-cma
Version:        4.4.2
Release:        %autorelease
Summary:        Covariance Matrix Adaptation Evolution Strategy numerical optimizer

License:        BSD-3-Clause
URL:            https://cma-es.github.io/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildArch:      noarch

%global _description %{expand:
A stochastic numerical optimization algorithm for difficult (non-convex,
ill-conditioned, multi-modal, rugged, noisy) optimization problems in continuous
search spaces, implemented in Python.}

%description %_description

%package -n     python3-cma
Summary:        %{summary}

%description -n python3-cma %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cma-%{version}
#Fix line-endings
sed -i 's/\r//' README.rst
#Remove unneeded shebang
sed -i '1d' cma/{bbobbenchmarks.py,purecma.py,test.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l cma

%files -n python3-cma -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
