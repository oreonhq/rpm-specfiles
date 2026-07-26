%global source0_hash d4193f3d9dc3f6f79aaed0e5637f45d98850ebf01f7ca20e69457f3e8946b66a

%global srcname kiwisolver

Name:           python-%{srcname}
Version:        1.5.0
Release:        %autorelease
Summary:        A fast implementation of the Cassowary constraint solver

# The entire source is BSD-3-Clause, except:
# - kiwi/AssocVector.h is HPND-sell-variant
#   (https://gitlab.com/fedora/legal/fedora-license-data/-/issues/96)
#
# Additionally, the following do not contribute to the binary RPMs:
# - benchmarks/nanobench.h is MIT
License:        BSD-3-Clause AND HPND-sell-variant
URL:            https://github.com/nucleic/kiwi
Source:         %pypi_source %{srcname}

%global _description %{expand:
Kiwi is an efficient C++ implementation of the Cassowary constraint solving
algorithm. Kiwi is an implementation of the algorithm based on the seminal
Cassowary paper. It is *not* a refactoring of the original C++ solver. Kiwi has
been designed from the ground up to be lightweight and fast.}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

# The file kiwi/AssocVector.h is derived from Loki
# (https://sourceforge.net/projects/loki-lib/,
# https://src.fedoraproject.org/rpms/loki-lib [retired]).
#
# Because this file has been modified from the original, and because Loki
# upstream is no longer active, it cannot be unbundled. It is not
# straightforward to determine which version of Loki was used for the fork.
Provides:       bundled(loki-lib)

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{pytest} py/tests/

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
