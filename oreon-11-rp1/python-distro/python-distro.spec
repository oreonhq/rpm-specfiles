%global source0_hash 6ede051357868ed427ea71d16fc27f4d63cc0d9c8a32788aa11c450ecefcc76f
%global pypi_name distro
Name:           python-%{pypi_name}
Version:        1.9.0
Release:        11%{?dist}
Summary:        Linux Distribution - a Linux OS platform information API
License:        Apache-2.0
URL:            https://github.com/python-distro/distro
Source0:        https://github.com/python-distro/distro/archive/refs/tags/v1.9.0.tar.gz#/distro-1.9.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-distro = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{pypi_name}
Summary:        Linux Distribution - a Linux OS platform information API
%if 0%{?fedora} || (0%{?oreon} >= 11)
Suggests:       /usr/bin/lsb_release
%endif
%description -n python3-%{pypi_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/distro* usr/lib64/python3*/site-packages/distro* usr/bin/*

%check

%pytest
%files
%files -n python3-distro -f %{oreon_filedir}/python3-distro.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.0-11
- Import
