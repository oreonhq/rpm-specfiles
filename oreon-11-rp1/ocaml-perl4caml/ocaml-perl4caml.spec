%global source0_hash 3dc19cb1c4941550219d2824b40c565a536736ef315098c898d2fee1196136b8
ExcludeArch: %{ix86}
Name:           ocaml-perl4caml
Version:        0.9.5
Release:        1%{?dist}
Summary:        OCaml library for calling Perl libraries and code
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            http://git.annexia.org/?p=perl4caml.git;a=summary
VCS:            git:git://git.annexia.org/perl4caml.git
Source0:        perl4caml-%{version}.tar.gz
Patch:          perl4caml-0.9.5-svtrv.patch
Patch:          perl4caml-0.9.5-fix-use-of-camlparam-etc-macros.patch
Patch:          0001-perl_c.c-Fix-declaration-of-argv.patch
Patch:          0002-Makefile.config-Avoid-annoying-coreutils-warning.patch
Requires: perl-libs%{?_isa}
# oreon:deps
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
Perl4caml allows you to use Perl code within Objective CAML (OCaml),
thus neatly side-stepping the (old) problem with OCaml which was that
it lacked a comprehensive set of libraries. Well now you can use any
part of CPAN in your OCaml code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n perl4caml-%{version} -p1
find -name .cvsignore -delete

# Avoid obsolescence warnings
sed -i 's/egrep/grep -E/' Makefile.config

%build

unset MAKEFLAGS
make EXTRA_EXTRA_CFLAGS='%{build_cflags}' \
%ifarch %{ocaml_native_compiler}
     OCAMLC="ocamlc.opt" OCAMLOPT="ocamlopt.opt -g" OCAMLMKLIB="ocamlmklib -g"
%else
     OCAMLC="ocamlc" OCAMLMKLIB="ocamlmklib -g" \
     perl4caml.cma META html
%endif
rm -f examples/*.{cmi,cmo,cmx,o,bc,opt}
%check

%ifarch %{ocaml_native_compiler}
unset MAKEFLAGS
CAML_LD_LIBRARY_PATH=$PWD make test
%endif
%install
export DESTDIR=$RPM_BUILD_ROOT
mkdir -p $DESTDIR/%{_libdir}/ocaml/stublibs
%ifarch %{ocaml_native_compiler}
make install
chmod 0755 $DESTDIR/%{_libdir}/ocaml/stublibs/dllperl4caml.so
%else
install -c -m 0755 -d $DESTDIR/%{_libdir}/ocaml/perl
install -c -m 0755 -d $DESTDIR/%{_libdir}/ocaml/stublibs
install -c -m 0644 perl.cmi perl.mli perl4caml.cma \
	libperl4caml.a META \
	wrappers/*.ml wrappers/*.cmi \
	$DESTDIR/%{_libdir}/ocaml/perl
install -c -m 0755 dllperl4caml.so $DESTDIR/%{_libdir}/ocaml/stublibs
%endif
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-perl4caml-devel -f %{oreon_filedir}/ocaml-perl4caml-devel.list

%changelog

%autochangelog
