%global source0_hash 8451495265af3e368f794c4dc15c99ce90c771d95560f542bff8c64b5455af3b
%global pypi_name websockets
Name:           python-%{pypi_name}
Version:        15.0.1
Release:        1%{?dist}
Summary:        Implementation of the WebSocket Protocol for Python
License:        BSD-3-Clause
URL:            https://github.com/aaugustin/websockets
Source0:        https://github.com/aaugustin/websockets/archive/refs/tags/15.0.1.tar.gz#/websockets-15.0.1.tar.gz
Patch:          https://github.com/python-websockets/websockets/commit/3128f5619d.patch
Patch:          https://github.com/python-websockets/websockets/pull/1639.patch
Patch:          https://github.com/python-websockets/websockets/commit/036fd45c16afec1b713ae7f37393c76c3ff528a5.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-websockets = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{pypi_name}
Summary:        Implementation of the WebSocket Protocol for Python
BuildRequires:  python3-devel
%description -n python3-%{pypi_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version} -p1

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/websockets* usr/lib64/python3*/site-packages/websockets* usr/bin/*

%check

%pyproject_check_import
%pytest -v
%files
%files -n python3-websockets -f %{oreon_filedir}/python3-websockets.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.0.1-1
- Prepare for Oreon 11 (RP1)
