%global source0_hash 875ecb79cada5ae4c5d26bad1eb3f82f003c3d1d22451363a01c98644a5bf20e

Name:           python-multiregex
Version:        2.0.3
Release:        %autorelease
Summary:        Quickly match many regexes against a string

License:        BSD-3-Clause
URL:            https://github.com/quantco/multiregex
Source:         %{pypi_source multiregex}

# https://github.com/Quantco/multiregex/pull/100
# Fix pyproject.toml build-system configuration (#100)
Patch:          https://github.com/Quantco/multiregex/pull/100.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Quickly match many regexes against a string.
Provides 2-10x speedups over naïve regex matching.}

%description %_description

%package -n     python3-multiregex
Summary:        %{summary}

%description -n python3-multiregex %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n multiregex-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l multiregex

%check
%pytest

%files -n python3-multiregex -f %{pyproject_files}
%doc README.md CHANGELOG.rst

%changelog
%autochangelog
