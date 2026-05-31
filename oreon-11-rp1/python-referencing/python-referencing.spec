%global source0_hash 44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8

%global srcname referencing

Name:           python-%{srcname}
Version:        0.37.0
Release:        %autorelease
Summary:        An implementation-agnostic implementation of JSON reference resolution
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source:        https://files.pythonhosted.org/packages/source/r/referencing/referencing-0.37.0.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-subtests)

%global _description %{expand:
An implementation-agnostic implementation of JSON reference resolution.
In other words, a way for e.g. JSON Schema tooling to resolve the $ref
keyword across all drafts without needing to implement support themselves.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
%pyproject_check_import -e referencing.tests*
%pytest referencing/tests


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.37.0-1
- Prepare for Oreon 11 (RP1)
