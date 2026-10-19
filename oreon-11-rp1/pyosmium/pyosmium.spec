%global source0_hash 864a3b5a0b4fc2cf2d2eb309d5bc5bd9f133f00f140111d0d954cfd5b1ad1a96
%global libosmium_version 2.20.0
Name:           pyosmium
Version:        4.3.1
Release:        1%{?dist}
Summary:        Python bindings for libosmium
License:        BSD-2-Clause
URL:            https://osmcode.org/pyosmium/
Source0:        https://github.com/osmcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          pyosmium-run-parallel.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pybind11) >= 2.9
BuildRequires:  python3dist(scikit-build-core) >= 0.10
Requires:       python3-pyosmium = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyosmium+tests
Summary:        Metapackage for python3-pyosmium tests extras
Requires:       python3-pyosmium = %{version}-%{release}
Provides:       python3dist(pyosmium[tests]) = %{version}-%{release}

%description -n python3-pyosmium+tests
Metapackage for python3-pyosmium tests extras.

%package -n       python3-pyosmium+docs
Summary:        Metapackage for python3-pyosmium docs extras
Requires:       python3-pyosmium = %{version}-%{release}
Provides:       python3dist(pyosmium[docs]) = %{version}-%{release}

%description -n python3-pyosmium+docs
Metapackage for python3-pyosmium docs extras.

%description
Provides Python bindings for the Libosmium C++ library, a library
for working with OpenStreetMap data in a fast and flexible manner.

%package -n python3-osmium
Summary:        Python bindings for libosmium
%description -n python3-osmium
Provides Python bindings for the Libosmium C++ library, a library
for working with OpenStreetMap data in a fast and flexible manner.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel -Ccmake.build-type=RelWithDebInfo
%install
%pyproject_install
PYTHONPATH=%{buildroot}%{python3_sitearch} %make_build -C docs man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m644 docs/man/*.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles python3-osmium usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-osmium -f %{oreon_filedir}/python3-osmium.list

%changelog

%autochangelog
