%global source0_hash f2b0fa67769051a406020d2fa4d247d16967080aae407139f888c196eb23de6b

%global srcname textile

Name:           python-%{srcname}
Version:        4.0.3
Release:        8%{?dist}
Summary:        A Humane Web Text Generator
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.io/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%global _description %{expand:
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.}

%description %_description

%package -n python3-%{srcname}
Summary:        A Humane Web Text Generator

%description -n python3-%{srcname} %_description

%pyproject_extras_subpkg -n python3-%{srcname} imagesize

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x imagesize

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

for f in README CHANGELOG ; do
  PYTHONPATH=%{buildroot}%{python3_sitelib} \
  PATH=%{buildroot}%{_bindir}:${PATH} \
    pytextile < ${f}.textile > ${f}.html
done

%check
%pytest -k 'not test_imagesize'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.* CONTRIBUTORS.txt CHANGELOG.*
%license LICENSE.txt
%{_bindir}/pytextile

%changelog
%autochangelog
