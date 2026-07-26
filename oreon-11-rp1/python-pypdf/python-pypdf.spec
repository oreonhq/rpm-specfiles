%global source0_hash 4096459bdb19df0231360617f2266d8068a40b9eb202bbea9c54274a320f0c55

%global srcname pypdf
%global forgeurl https://github.com/py-pdf/pypdf

Name:           python-%{srcname}
Version:        4.2.0
Release:        %autorelease
Summary:        Pure-Python PDF library

License:        BSD-3-Clause
URL:            https://pypdf.readthedocs.io
# PyPI tarball doesn't include tests
Source:         %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  sed

%global _description %{expand:
pypdf is a free and open-source pure-python PDF library capable of splitting,
merging, cropping, and transforming the pages of PDF files. It can also add
custom data, viewing options, and passwords to PDF files. pypdf can retrieve
text and metadata from PDFs as well.}

%description %_description

%package -n     python3-pypdf
Summary:        %{summary}

%description -n python3-pypdf %_description

%pyproject_extras_subpkg -n python3-pypdf crypto,full,image

%package        doc
Summary:        Documentation for %{name}
Requires:       python3-docs

%description    doc
This package provides additional documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Fix test dependencies
sed -i tox.ini \
  -e 's/pycryptodome/pycryptodomex/' \
  -e '/pytest-socket/d'

# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/\{python_version\}|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py

%generate_buildrequires
%pyproject_buildrequires -t -x crypto,docs,full,image

%build
%pyproject_wheel

# Build docs
sphinx-build-3 docs html
rm -rf html/{.buildinfo,.doctrees}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
# https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/thread/4Y2VRLVAR3DJXBSFVDYJMU3G4ZNPGEU6/
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTORS.md

%files doc
%license LICENSE
%doc html

%changelog
%autochangelog
