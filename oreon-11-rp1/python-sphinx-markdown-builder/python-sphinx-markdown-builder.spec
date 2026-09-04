%global source0_hash 3a5175543fd68371f96aca9806a3b6e62c407a51a23802ef9a0863eec1f42b20

Summary:        Sphinx extension for rendering markdown builder
Name:           python-sphinx-markdown-builder
Version:        0.6.11
Release:        %autorelease
License:        MIT
URL:            https://github.com/liran-funaro/sphinx-markdown-builder
Source0:        https://github.com/liran-funaro/sphinx-markdown-builder/archive/%{version}/sphinx-markdown-builder-%{version}.tar.gz
Patch:          0001-Relax-setuptools-req.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-sphinxcontrib-httpdomain
%description
A Sphinx extension for rendering builder written in markdown.

%package     -n python3-sphinx-markdown-builder
Summary:        Sphinx extension for rendering markdown builder

%description -n python3-sphinx-markdown-builder
A Sphinx extension for rendering builder written in markdown.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sphinx-markdown-builder-%{version}
%if 0%{fedora} < 43
sed -i -e 's/license = "MIT"/license = { text = "MIT" }/' pyproject.toml
%endif
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L sphinx_markdown_builder

%check
%pyproject_check_import
%pytest

%files -n python3-sphinx-markdown-builder -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
