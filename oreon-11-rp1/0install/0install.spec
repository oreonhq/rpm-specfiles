%global source0_hash 648c4b318c1a26dfcb44065c226ab8ca723795924ad80a3bf39ae1ce0e9920c3
%global giturl  https://github.com/0install/0install
Name:           0install
Version:        2.18
Release:        1%{?dist}
Summary:        Decentralized cross-distribution software installation system
License:        LGPL-2.1-or-later
SourceLicense:  %{license} AND CC0-1.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://0install.net/
VCS:            git:%{giturl}.git
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tbz
Source1:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tbz.sig
Source2:        5DD58D70899C454A966D6A5175133C8F94F6E0CC.gpg
ExcludeArch:    %{ix86}
%global _desc %{expand:Zero Install is a decentralized cross-distribution software installation
system.  Other features include full support for shared libraries (with a SAT
solver for dependency resolution), sharing between users, and integration with
native platform package managers.  It supports both binary and source
packages, and works on Linux, macOS, Unix and Windows systems.}
# oreon:deps
BuildRequires:  gpgverify
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit2-devel
# /oreon:deps
%description
%_desc

%package -n     ocaml-0install-solver
Summary:        Package dependency solver
%description -n ocaml-0install-solver
%_desc

This package contains a package dependency resolver based on a SAT solver.
This was originally written for the 0install package manager, but is now
generic and is also used as a solver backend for opam.

The SAT solver is based on MiniSat (http://minisat.se/Papers.html) and the
application to package management is based on OPIUM (Optimal Package
Install/Uninstall Manager).  0install-solver uses a (novel?) strategy to find
the optimal solution extremely quickly (even for a SAT-based solver).

%package -n     ocaml-0install-solver-devel
Summary:        Development files for %{name}-solver
Requires:       ocaml-0install-solver%{?_isa} = %{version}-%{release}
%description -n ocaml-0install-solver-devel
The %{name}-solver-devel package contains libraries and signature files for
developing applications that use %{name}-solver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup

%build

%dune_build -p 0install-solver
%install
%dune_install 0install-solver
%oreon_autofiles ocaml-0install-solver usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-0install-solver-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check -p 0install-solver
%files -f %{oreon_filedir}/main.list
%files -n ocaml-0install-solver -f %{oreon_filedir}/ocaml-0install-solver.list
%files -n ocaml-0install-solver-devel -f %{oreon_filedir}/ocaml-0install-solver-devel.list

%changelog

%autochangelog
