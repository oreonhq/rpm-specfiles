%global source0_hash 3dc19cb1c4941550219d2824b40c565a536736ef315098c898d2fee1196136b8

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-perl4caml
Version:        0.9.5
Release:        118%{?dist}
Summary:        OCaml library for calling Perl libraries and code
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            http://git.annexia.org/?p=perl4caml.git;a=summary
VCS:            git:git://git.annexia.org/perl4caml.git
# There is currently no website hosting the tarballs.
Source0:        perl4caml-%{version}.tar.gz

# Include upstream patch for Perl 5.12:
# http://git.annexia.org/?p=perl4caml.git;a=commitdiff_plain;h=4cb12aa05bd5aa69ccfa1c6d41ab10bc79a3c3a3
Patch:          perl4caml-0.9.5-svtrv.patch

# Upstream patch to fix build for OCaml 4.04.
Patch:          perl4caml-0.9.5-fix-use-of-camlparam-etc-macros.patch

# Upstream patch to fix argv declaration for GCC 14:
Patch:          0001-perl_c.c-Fix-declaration-of-argv.patch

# Upstream patch to avoid warning from coreutils:
Patch:          0002-Makefile.config-Avoid-annoying-coreutils-warning.patch

BuildRequires:  make
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  perl-devel >= 5.8
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Embed)

# Perl4caml provides type-safe wrappers for these Perl modules:
#Requires:  perl-Date-Calc
##Requires:  perl-Date-Format
##Requires:  perl-Date-Parse
##Requires:  perl-Net-Google
##Requires:  perl-HTML-Element
#Requires:  perl-HTML-Parser
#Requires:  perl-HTML-Tree
#Requires:  perl-libwww-perl
#Requires:  perl-Template-Toolkit
#Requires:  perl-URI
#Requires:  perl-WWW-Mechanize

Requires: perl-libs%{?_isa}

# We're also going to pick up a versioned dependency, to help track things:

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
# Parallel builds don't work:
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
# Parallel builds don't work:
unset MAKEFLAGS

# Set the library path used by ocamlrun so it uses the library
# we just built in the current directory.
CAML_LD_LIBRARY_PATH=$PWD make test
%endif

%install
export DESTDIR=$RPM_BUILD_ROOT
mkdir -p $DESTDIR/%{_libdir}/ocaml/stublibs

%ifarch %{ocaml_native_compiler}
make install
chmod 0755 $DESTDIR/%{_libdir}/ocaml/stublibs/dllperl4caml.so
%else
# Install by hand so we don't try to install *.cmx{,a} files on bytecode arch.
install -c -m 0755 -d $DESTDIR/%{_libdir}/ocaml/perl
install -c -m 0755 -d $DESTDIR/%{_libdir}/ocaml/stublibs
install -c -m 0644 perl.cmi perl.mli perl4caml.cma \
	libperl4caml.a META \
	wrappers/*.ml wrappers/*.cmi \
	$DESTDIR/%{_libdir}/ocaml/perl
install -c -m 0755 dllperl4caml.so $DESTDIR/%{_libdir}/ocaml/stublibs
%endif

%ocaml_files

%files -f .ofiles
%license COPYING.LIB

%files devel -f .ofiles-devel
%doc AUTHORS doc/* examples html README
%license COPYING.LIB

%changelog
%autochangelog
