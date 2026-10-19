%global source0_hash ac1b1e23a0de93a57f15e4b4d802a539c524df483504cee5055d15c4dd6049e6
Name:           cmake-fedora
Version:        2.9.3
Release:        25%{?dist}
Summary:        CMake helper modules for fedora developers
License:        BSD-2-Clause-FreeBSD
URL:            https://pagure.io/%{name}/
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}-Source.tar.gz
Requires:       cmake >= 2.6.2
Requires:       git
Requires:       bodhi-client
Requires:       koji
Requires:       rpm-build
Requires:       fedpkg
Requires:       fedora-packager
Requires:       curl
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  koji
# /oreon:deps
%description
cmake-fedora consist a set of cmake modules that provides
helper macros and targets for fedora developers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-Source

%build

%cmake -DCMAKE_FEDORA_ENABLE_FEDORA_BUILD=1 .
%cmake_build
%install
%cmake_install
rm -fr %{buildroot}%{_docdir}/*
%oreon_autofiles main

%check

ctest --output-on-failure
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
