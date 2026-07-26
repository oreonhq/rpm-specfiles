%global source0_hash 7269ad6abf0fdf39be14f82c77c5890af42d62cd2b0ce214e85cb3a5fe772365

%global commit f8fcbb080c4bc4ff14bd30876386edd63d8362cb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-sly
Version:        0.4
Release:        0.42.%{shortcommit}%{?dist}
Summary:        An implementation of lex and yacc for Python 3

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://sly.readthedocs.io
Source0:        https://github.com/dabeaz/sly/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)

%global _description %{expand:
SLY is a pure Python implementation of the lex and yacc tools commonly
used to write parsers and compilers. Parsing is based on the same
LALR(1) algorithm used by many yacc tools.}

%description %_description

%package -n python3-sly
Summary:        %{summary}

%description -n python3-sly %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sly-%{commit}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files sly

%check
%pytest

%files -n python3-sly -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
