# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 a27df6835de352b6ad06e0781c83105037069b99350c0ed294e8a5c7fd379aba
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           python-productmd
Version:        1.50
Release:        2%{?dist}
Summary:        Library providing parsers for metadata related to OS installation

License:        LGPL-2.1-only
URL:            https://github.com/release-engineering/productmd
Source:         %{pypi_source productmd}

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
%oreon_verify_sources
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
