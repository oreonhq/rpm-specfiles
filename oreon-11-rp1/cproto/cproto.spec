%global source0_hash beb121e08c0d47b5bd719071c32a77edcc31dff992a84e3d9a59c0f7ec9fadd3
Summary:        Generates function prototypes and variable declarations from C code
Name: cproto
Version: 4.8a
Release:        1%{?dist}
License: LicenseRef-Fedora-Public-Domain
Source0:        https://invisible-island.net/archives/cproto/cproto-%{version}.tgz
URL: http://invisible-island.net/
# oreon:deps
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Cproto generates function prototypes and variable declarations from C
source code. Cproto can also convert function definitions between the
old style and the ANSI C style. This conversion will overwrite the
original files, however, so be sure to make a backup copy of your
original files in case something goes wrong. Cproto uses a Yacc
generated parser, so it should not be confused by complex function
definitions as much as other prototype generators.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
