# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 4f7a55408e439741b74e18f81fe34a7dc4e4e5126cef47ca5e9e093a5a82e01c
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Breaks the circular dependency with ruamel.yaml.clib.
%bcond_with bootstrap

Name:           python-ruamel-yaml
Version:        0.19.1
Release:        %autorelease
Summary:        YAML 1.2 loader/dumper package for Python

# SPDX
License:        MIT
URL:            https://sourceforge.net/projects/ruamel-yaml
# The PyPI sdist does not contain tests, so we use a snapshot from SourceForge
Source:         https://yaml.dev/ruamel-dl-tagged-releases/ruamel.yaml-%{version}.tar.xz

BuildArch:      noarch

%global _description %{expand:
ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of
comments, seq/map flow style, and map key order.}

%description %{_description}

%package -n     python3-ruamel-yaml
Summary:        YAML 1.2 loader/dumper package for Python

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%py_provides python3-ruamel.yaml

%if !%{with bootstrap}
# ruamel.yaml.clibz is not available in Fedora (and probably never will
# be), so require the old clib backend
Requires:       python3-ruamel-yaml+oldlibyaml = %{version}-%{release}
%endif

%description -n python3-ruamel-yaml %{_description}

%prep
%oreon_verify_sources
%autosetup -n ruamel.yaml-%{version}

%generate_buildrequires
%pyproject_buildrequires %{!?with_bootstrap:-x oldlibyaml}

%build
%pyproject_wheel

%install
%pyproject_install
# RFE: Add option for namespace packages to %%pyproject_save_files
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%pyproject_save_files -l ruamel

%check
%if %{with bootstrap}
k="${k-}${k+ and }not test_load_cyaml"
k="${k-}${k+ and }not test_load_cyaml_1_2"
k="${k-}${k+ and }not test_dump_cyaml_1_2"
%endif
%pytest -k "${k-}" _test/test_*.py

%files -n python3-ruamel-yaml -f %{pyproject_files}
%doc README.md

%pyproject_extras_subpkg -n python3-ruamel-yaml oldlibyaml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.1-1
- Prepare for Oreon 11 (RP1)
