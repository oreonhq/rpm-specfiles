%global source0_hash a27df6835de352b6ad06e0781c83105037069b99350c0ed294e8a5c7fd379aba

Name:           python-productmd
Version:        1.50
Release:        2%{?dist}
Summary:        Library providing parsers for metadata related to OS installation

License:        LGPL-2.1-only
URL:            https://github.com/release-engineering/productmd
Source:        https://files.pythonhosted.org/packages/source/p/productmd/productmd-1.50.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description \
Python library providing parsers for metadata related to composes\
and installation media.

%description %_description

%package -n python3-productmd
Summary:        %{summary}

%description -n python3-productmd %_description

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n productmd-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files productmd

%check
%pytest

%files -n python3-productmd -f %{pyproject_files}
%license LICENSE
%doc AUTHORS

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.50-2
- Prepare for Oreon 11 (RP1)
