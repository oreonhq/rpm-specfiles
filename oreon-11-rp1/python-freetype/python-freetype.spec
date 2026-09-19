%global source0_hash 82ba282147b204797484e3b9fbcbc27a4ec3e6aecefa9dcabeab024087b5f722

%global pypi_name freetype-py

Name:           python-freetype
Version:        2.5.1
Release:        %autorelease
Summary:        Python binding for the freetype library
License:        BSD-3-Clause
URL:            https://github.com/rougier/freetype-py
Source0: 	%{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  freetype

%description
Freetype Python provides bindings for the FreeType library. Only the high-level
API is bound.

%package -n     python3-freetype
Summary:        %{summary}
%py_provides python3-freetype

%description -n python3-freetype
%{description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%py3_shebang_fix freetype/*.py
%py3_shebang_fix examples/*.py

sed -i 's/"setuptools_scm\[toml\]>=3.4",//' pyproject.toml
sed -i 's/"certifi",//' pyproject.toml
sed -i 's/"cmake"//' pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -t

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l freetype

%check
%tox

%files -n python3-freetype -f %{pyproject_files}
%doc examples README.rst

%changelog
%autochangelog
