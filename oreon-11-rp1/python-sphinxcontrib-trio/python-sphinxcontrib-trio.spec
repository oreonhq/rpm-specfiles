%global source0_hash c3b2866bbf10993d10168eaaf54329ce8828b71263ebb06d2f1f02bae67c0bcd
%global srcname sphinxcontrib-trio
%global pkgname sphinxcontrib_trio

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Make Sphinx better at documenting Python functions and methods
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/sphinxcontrib-trio
Source0:        https://files.pythonhosted.org/packages/source/s/%{pkgname}/%{pkgname}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-cssselect
BuildRequires:  python3-lxml
BuildRequires:  python3-pytest
BuildRequires:  %{_bindir}/rst2html
BuildRequires:  make
BuildArch:      noarch

%global desc                                                            \
This sphinx extension helps you document Python code that uses          \
async/await, or abstract methods, or context managers, or generators,   \
or ... you get the idea. It works by making sphinx's regular            \
directives for documenting Python functions and methods smarter and     \
more powerful. The name is because it was originally written for the    \
Trio project, and I'm not very creative. But don't be put off –         \
there's nothing Trio- or async-specific about this extension; any       \
Python project can benefit. (Though projects using async/await          \
probably benefit the most, since sphinx's built-in tools are            \
especially inadequate in this case.)

%description
%desc

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname}
%desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pkgname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
make -C docs html SPHINXBUILD=%{_bindir}/sphinx-build-3
rm -f docs/build/html/.buildinfo
rst2html README.rst README.html

%install
%pyproject_install
%pyproject_save_files -l %{pkgname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst README.html
%doc docs/build/html

%check
%pyproject_check_import
%pytest -k 'not test_end_to_end'

%changelog
%autochangelog
