# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 e234480908f633d2d80fdd97e87699135b2ed2fc9876b7f41d1d4a2d3262a0c4
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           python-semantic_version
Version:        2.10.0
Release:        %autorelease
Summary:        Library implementing the 'SemVer' scheme

License:        BSD-2-Clause
URL:            https://github.com/rbarrois/python-semanticversion
Source:        https://github.com/rbarrois/python-semanticversion/archive/2.10.0/python-semanticversion-2.10.0.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel

# Test dependencies manually cherry-picked from the [dev] extra
# Upstream uses nose2, but pytest works as well
BuildRequires:  python3-pytest
%if %{undefined rhel} || %{defined epel}
# Optional test dependency
BuildRequires:  python3-django
%endif

%global _description %{expand:
This small python library provides a few tools to handle semantic versioning in
Python.}

%description %{_description}

%package -n     python3-semantic_version
Summary:        %{summary}

%description -n python3-semantic_version %{_description}

%prep
%oreon_verify_sources
%autosetup -p1 -n python-semanticversion-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l semantic_version

%check
%pytest

%files -n python3-semantic_version -f %{pyproject_files}
%doc README.rst ChangeLog CREDITS

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10.0-1
- Prepare for Oreon 11 (RP1)
