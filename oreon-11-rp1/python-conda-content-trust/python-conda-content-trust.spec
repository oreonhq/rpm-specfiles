%global source0_hash 6d459ca40d3775220ad7a2886a7c367a0d966b47cc0b97f27fb6be0439e361c9

%?python_enable_dependency_generator
%global srcname conda-content-trust
%global pkgname conda_content_trust

Name:           python-%{srcname}
Version:        0.3.2
Release:        1%{?dist}
Summary:        Signing and verification tools for conda

License:        BSD-3-Clause
URL:            https://github.com/conda/%{srcname}
Source0:        https://github.com/conda/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Based on The Update Framework (TUF), conda-content-trust is intended to ensure
that when users in the conda ecosystem obtain a package or data about that
package, they can know whether or not it is trustworthy (e.g. originally comes
from a reliable source and has not been tampered with). A basic library and
basic CLI are included to provide signing, verification, and trust delegation
functionality.

This exists as an alteration of TUF because of the very particular needs of
the conda ecosystem. (Developers are encouraged to just use TUF whenever
possible!)

This tool is general purpose. It is currently used in conda 4.10.1+ to verify
package metadata signatures when they are available.}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
Recommends:     gnupg2

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# do not run coverage in pytest
sed -i -E '/--(no-)?cov/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pkgname}

%check
# securesystemslib is not packaged, skip those tests
%{pytest} -v tests \
  --deselect=tests/test_root.py::test_sign_root_metadata_dict_via_gpg \
  --deselect=tests/test_root.py::test_sign_root_metadata_via_gpg \
  --deselect=tests/test_root.py::test_gpg_pubkey_in_ssl_format

%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc README.md
%{_bindir}/conda-content-trust

%changelog
%autochangelog
