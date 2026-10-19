%global source0_hash b590666c08f9ae7d134a669e57680a11cdfb1f506ad24deef171119dee902868
ExcludeArch: %{ix86}
%global giturl  https://github.com/vincenthz/ocaml-dbus
Name:           ocaml-dbus
Version:        0.30
Release:        1%{?dist}
Summary:        OCaml library for using D-Bus
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://projects.snarc.org/ocaml-dbus/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
D-Bus is a project that permits programs to communicate with each
other, using a simple IPC protocol.  This is an OCaml binding for
D-Bus.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Explicitly depend on the Unix module for OCaml 5.x
sed -i 's/ -o / -I +unix&/' Makefile

%build

make \
%ifarch %{ocaml_native_compiler}
OCAMLC="ocamlc.opt -g" OCAMLOPT="ocamlopt.opt -g" OCAMLMKLIB="ocamlmklib -g"
%else
  all-byte
%endif
if ! test -f "README"; then
cat > README <<_EOF
OCaml D-BUS bindings version %{version}.
Please see the main website for documentation:
https://projects.snarc.org/ocaml-dbus/
_EOF
fi
%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
%ifarch %{ocaml_native_compiler}
make OCAMLDESTDIR=$OCAMLFIND_DESTDIR install
%else
make OCAMLDESTDIR=$OCAMLFIND_DESTDIR install-byte
%endif
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-dbus-devel -f %{oreon_filedir}/ocaml-dbus-devel.list

%changelog

%autochangelog
