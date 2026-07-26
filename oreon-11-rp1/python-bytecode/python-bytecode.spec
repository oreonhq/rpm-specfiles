%global source0_hash 0c37efa5bd158b1b873f530cceea2c645611d55bd2dc2a4758b09f185749b6fd

Name:           python-bytecode
Version:        0.17.0
Release:        %autorelease
Summary:        Python module to generate and modify bytecode

License:        MIT
URL:            https://github.com/MatthieuDartiailh/bytecode
Source:         %{pypi_source bytecode}

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(pytest)
# Documentation
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-tabs)

%global _description %{expand:
bytecode is a Python module to generate and modify bytecode.}

%description %_description

%package -n     python3-bytecode
Summary:        %{summary}
Requires:       python3-libs

%description -n python3-bytecode %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n bytecode-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd doc
make texinfo
pushd build
pushd texinfo
makeinfo --docbook bytecode.texi
popd	
popd	
popd

%install
%pyproject_install
%pyproject_save_files -l bytecode

mkdir -p %{buildroot}%{_datadir}/help/en/python-bytecode
install -m644 doc/build/texinfo/bytecode.xml %{buildroot}%{_datadir}/help/en/python-bytecode

%check
%pyproject_check_import
%pytest

%files -n python3-bytecode -f %{pyproject_files}
%doc README.rst
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-bytecode

%changelog
%autochangelog
