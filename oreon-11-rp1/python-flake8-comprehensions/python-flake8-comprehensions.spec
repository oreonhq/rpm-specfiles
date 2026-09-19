%global source0_hash 4fb7f5b9d4333128222860d59956d14d994f6a0e32d2abb82e7b29305e50b888

%global srcname flake8-comprehensions

Name:           python-%{srcname}
Version:        3.17.0
Release:        3%{?dist}
Summary:        Flake8 plugin that helps you write better list/set/dict comprehensions

License:        MIT
URL:            https://github.com/adamchainz/flake8-comprehensions
Source0:        https://github.com/adamchainz/flake8-comprehensions/archive/%{version}/%{srcname}-%{version}.tar.gz

# Revert upstream change for better setuptools compatibility
Patch100:       pep639.patch

BuildArch:      noarch

%global _description %{expand:
A flake8 plugin to identify the following patterns:

- C400-402: Unnecessary generator - rewrite as a <list/set/dict> comprehension.
- C403-404: Unnecessary list comprehension - rewrite as a <set/dict>
  comprehension.
- C405-406: Unnecessary <list/tuple> literal - rewrite as a <set/dict> literal.
- C408: Unnecessary <dict/list/tuple> call - rewrite as a literal.
- C409-410: Unnecessary <list/tuple> passed to <list/tuple>() - (remove the
  outer call to <list/tuple>``()/rewrite as a ``<list/tuple> literal).
- C411: Unnecessary list call - remove the outer call to list().
- C412: Unnecessary <dict/list/set> comprehension - in can take a generator.
- C413: Unnecessary <list/reversed> call around sorted().
- C414: Unnecessary <list/reversed/set/sorted/tuple> call within
  <list/set/sorted/tuple>().
- C415: Unnecessary subscript reversal of iterable within
  <reversed/set/sorted>().
- C416: Unnecessary <list/set> comprehension - rewrite using <list/set>().
- C417: Unnecessary map usage - rewrite using a generator
  expression/<list/set/dict> comprehension.
- C418: Unnecessary <dict/dict comprehension> passed to dict() - remove the
  outer call to dict().
- C419 Unnecessary list comprehension in <any/all>() prevents short-
  circuiting - rewrite as a generator.
- C420: Unnecessary dict comprehension - rewrite using dict.fromkeys().}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -N -n %{srcname}-%{version}

%if 0%{?rhel}
%patch 100 -p1 -R
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l flake8_comprehensions

%check
%pyproject_check_import flake8_comprehensions

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc HISTORY.rst README.rst

%changelog
%autochangelog
