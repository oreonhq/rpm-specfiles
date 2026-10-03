%global source0_hash 717e92fcf64e4b7f535ebbf00d0ba21a083fa27031045af2f5040bcd38612187

%global pypi_name resolvelib
%global forgeurl https://github.com/sarugaku/resolvelib
%bcond tests 1

Name:           python-%{pypi_name}
Version:        1.0.1
%global tag %{version}
%forgemeta
Release:        13%{?dist}
Summary:        Resolve abstract dependencies into concrete ones

License:        ISC
URL:            %{forgeurl}
Source:         %{forgesource}
# Avoid commentjson/json5 build dependency just for a couple tests
Patch:        https://github.com/sarugaku/resolvelib/pull/141.patch#/remove-commentjson-dep.patch
# Drop wheel from direct build dependencies
# https://github.com/sarugaku/resolvelib/pull/175 rebased
Patch:          remove-wheel-dep.patch
# Correct PythonInputProvider._iter_matches to fix tests with packaging 26.0
# https://github.com/sarugaku/resolvelib/pull/201 rebased
Patch:          packaging-26-fix.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
ResolveLib at the highest level provides a Resolver class that
includes dependency resolution logic. You give it some things, and a little
information on how it should interact with them, and it will spit out a
resolution result. Intended Usage :: import resolvelib Things I want to
resolve. requirements [...] Implement logic so the resolver understands the
requirement format. class...}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup %{forgesetupargs} -p1


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1-13
- Prepare for Oreon 11 (RP1)
