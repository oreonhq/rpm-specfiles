%global source0_hash 8535a88f74a34dfdb51c4539e4a965b84204273bd04e539a5d729f2536da6c9f
ExcludeArch: %{ix86}
%global giturl  https://github.com/ygrek/ocaml-mysql
Name:           ocaml-mysql
Version:        1.2.4
Release:        1%{?dist}
Summary:        OCaml library for accessing MySQL databases
License:        LGPL-2.1-or-later
URL:            https://ygrek.org/p/ocaml-mysql/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{giturl}/releases/download/v%{version}/ocaml-mysql-%{version}.tar.gz.asc
Source2:        KEYS
Patch0:         %{name}-custom-fixed-length.patch
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
ocaml-mysql is a package for ocaml that provides access to mysql
databases. It consists of low level functions implemented in C and a
module Mysql intended for application development.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1

%build

unset MAKEFLAGS
%configure
make all
%ifarch %{ocaml_native_compiler}
make opt
%endif
%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
%make_install
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-mysql-devel -f %{oreon_filedir}/ocaml-mysql-devel.list

%changelog

%autochangelog
