%global source0_hash b45774fae6298c40851e8cfa459c2d630683f47730209adc90963c1aaa181f9b

%global srcname docstring-parser

Name:           python-%{srcname}
Version:        0.17.0
Release:        4%{?dist}
Summary:        Parse Python docstrings
License:        MIT
URL:            https://github.com/rr-/docstring_parser
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Parse Python docstrings. Currently support ReST, Google, Numpydoc-style and Epydoc docstrings.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n docstring_parser-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files docstring_parser

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
%autochangelog
