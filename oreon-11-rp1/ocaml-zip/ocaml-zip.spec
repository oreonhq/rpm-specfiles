%global source0_hash d2ce7ebc4d3b7c029daecd0b491a36163b22f7e1d95e86224d4a27a101f36177
ExcludeArch: %{ix86}
%global giturl  https://github.com/xavierleroy/camlzip
Name:           ocaml-zip
Version:        1.14
Release:        1%{?dist}
Summary:        OCaml library for reading and writing zip, jar and gzip files
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://xavierleroy.org/software.html
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/camlzip-%{version}.tar.gz
Patch:          %{name}-zlib-ng.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  pkgconfig(zlib-ng)
# /oreon:deps
%description
This Objective Caml library provides easy access to compressed files
in ZIP and GZIP format, as well as to Java JAR files. It provides
functions for reading from and writing to compressed files in these
formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-ng-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n camlzip-%{version} -p1

# Do not try to overwrite the system ld.conf
sed -i "s,ocamlfind install,& -ldconf $PWD/ld.conf," Makefile

# Generate debuginfo
sed -i 's/ocamlopt/& -g/;s/ocamlmklib/& -g/' Makefile

%build

make all
%ifarch %{ocaml_native_compiler}
make allopt
%endif
make doc
%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml/zip
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml/stublibs
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
export EXT_DLL=.so
touch ld.conf
%make_install
%ocaml_files
%ifarch %{ocaml_native_compiler}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=$PWD
make -C test
test/testzlib Makefile Makefile.gz
test/testzlib -d Makefile.gz Makefile.uncompressed
cmp Makefile Makefile.uncompressed
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-zip-devel -f %{oreon_filedir}/ocaml-zip-devel.list

%changelog

%autochangelog
