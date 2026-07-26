%global source0_hash 3b80eee58788a1119574239c1997957579d2573c00982fb869e282093422e787

%global commit 54cb3fcf1bc4eae1bfdd941745b79da2cd8c9cbe
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250922
# Documentation contains javascript, using
# python-mkdocs-print-site-plugin allows one to have
# a single page with fewer unnecessary web assets
%bcond builddocs 0

Name:           python-tamilstring
Version:        1.5.31^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Manage tamil unicode characters

License:        MIT
URL:            https://gitlab.com/boopalan-dev/tamilstring
# PyPI source does not have documentation
Source:         %{url}/-/archive/%{commit}/tamilstring-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with builddocs}
# Documentation
BuildRequires:  python3dist(mkdocs)
BuildRequires:  python3dist(mkdocs-material)
%endif

%global _description %{expand:
TamilString is a Python library designed to simplify the handling and
manipulation of Tamil Unicode characters, enabling developers to
process Tamil text more efficiently in their applications.}

%description %_description

%package -n     python3-tamilstring
Summary:        %{summary}

%description -n python3-tamilstring %_description

%if %{with builddocs}
%package doc
Summary: Documentation for TamilString

%description doc
%_description
Documentation files
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tamilstring-%{commit}

%generate_buildrequires
%pyproject_buildrequires -x dev

%build
%pyproject_wheel
%if %{with builddocs}
mkdocs build --site-dir public
%endif

%install
%pyproject_install
%pyproject_save_files -l tamilstring

%check
%pyproject_check_import
%pytest

%files -n python3-tamilstring -f %{pyproject_files}

%if %{with builddocs}
%files doc
%doc public
%endif

%changelog
%autochangelog
