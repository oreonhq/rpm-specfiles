%global source0_hash ec359850f4f338b607d05200d508736b14eaa30fca8aefdfde980a283afd789d
%global forgeurl https://github.com/rjarry/libecoli
Name: libecoli
Version: 0.11.7
Summary:        Extensible COmmand LIne library
License: BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
%forgemeta
URL: %{forgeurl}
Release:        1%{?dist}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  libedit-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconf
# /oreon:deps
%description
libecoli stands for Extensible COmmand LIne library.

This library provides helpers to build interactive command line interfaces.

What can it be used for?

* Complex interactive command line interfaces in C (e.g.: a router CLI).
* Application arguments parsing, native support for bash completion.
* Generic text parsing.

Main Features

* Dynamic completion.
* Contextual help.
* Integrated with libedit, but can use any readline-like library.
* Modular: the CLI behavior is defined through an assembly of basic nodes.
* Extensible: the user can write its own nodes to provide specific features.
* C API.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libedit-devel
%description devel
This package contains development files for %{name}.

%package doc
BuildArch: noarch
Summary: Documentation for %{name}
%description doc
This package contains the HTML documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%meson -Dexamples=disabled -Dyaml=disabled
%meson_build
%check

%meson_test
%install
%meson_install
for man in "%{buildroot}%{_mandir}"/*/*; do
	read -r so link < "$man"
	if [ "$so" = ".so" ]; then
		rm -f "$man"
		if [ -f "%{buildroot}%{_mandir}/$link" ]; then
			ln -sr "%{buildroot}%{_mandir}/$link" "$man"
		fi
	fi
done
%fdupes "%{buildroot}%{_datadir}/doc/libecoli"
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libecoli-devel -f %{oreon_filedir}/libecoli-devel.list
%files -n libecoli-doc -f %{oreon_filedir}/libecoli-doc.list

%changelog

%autochangelog
