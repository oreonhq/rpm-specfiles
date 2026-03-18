# Don't add -Wl,-dT,<build dir>
%undefine _package_note_flags

# OCaml 5.1 broke building with LTO.  A file prims.c is generated with
# primitive function declarations, all with "void" for their parameter
# list.  This does not match the real definitions, leading to lots of
# -Wlto-type-mismatch warnings.  These change the output of the tests,
# leading to many failed tests.  This is still a problem in 5.3.
%global _lto_cflags %{nil}

# OCaml has a bytecode backend that works on anything with a C
# compiler, and a native code backend available on a subset of
# architectures.  A further subset of architectures support native
# dynamic linking.

%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

%ifarch %{ocaml_natdynlink}
%global natdynlink 1
%else
%global natdynlink 0
%endif

%global giturl https://github.com/ocaml/ocaml

# i686 support was dropped in OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# These are all the architectures that the tests run on.  The tests
# take a long time to run, so don't run them on slow machines.
%global test_arches aarch64 %{power64} riscv64 s390x x86_64
# These are the architectures for which the tests must pass otherwise
# the build will fail.
#global test_arches_required aarch64 ppc64le x86_64
%global test_arches_required NONE

# Architectures where parallel builds fail.
#global no_parallel_build_arches aarch64

#global rcver +git
%global rcver %{nil}

Name:           ocaml
Version:        5.4.1
Release:        4%{?dist}

Summary:        OCaml compiler and programming environment

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://www.ocaml.org
VCS:            git:%{giturl}.git

Source0:        %{giturl}/archive/%{version}%{rcver}/%{name}-%{version}%{rcver}.tar.gz
Source1:        macros.ocaml-rpm
Source2:        ocaml_files.py

# IMPORTANT NOTE:
#
# These patches are generated from unpacked sources stored in a
# pagure.io git repository.  If you change the patches here, they will
# be OVERWRITTEN by the next update.  Instead, request commit access
# to the pagure project:
#
# https://pagure.io/fedora-ocaml
#
# Current branch: fedora-45-5.4.1
#
# ALTERNATIVELY add a patch to the end of the list (leaving the
# existing patches unchanged) adding a comment to note that it should
# be incorporated into the git repo at a later time.

# Fedora-specific patches
Patch:          0001-Don-t-add-rpaths-to-libraries.patch
Patch:          0002-configure-Allow-user-defined-C-compiler-flags.patch

# Fix for arm64 frame pointers
# https://github.com/ocaml/ocaml/issues/14574
# https://github.com/ocaml/ocaml/pull/14589
# Upstream 6cda6d8a928ada5dd0f58de229d3cb193cfdff53
Patch:          0003-Merge-pull-request-14589-from-xavierleroy-arm64-addi.patch

BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  gawk
BuildRequires:  hardlink
BuildRequires:  perl-interpreter
BuildRequires:  util-linux
BuildRequires:  /usr/bin/annocheck
BuildRequires:  pkgconfig(libzstd)

# Documentation requirements
BuildRequires:  asciidoc
BuildRequires:  python3-pygments

# ocamlopt runs gcc to link binaries.  Because Fedora includes
# hardening flags automatically, redhat-rpm-config is also required.
# Compressed marshaling requires libzstd-devel.
Requires:       gcc
Requires:       redhat-rpm-config
Requires:       libzstd-devel%{?_isa}

# Because we pass -c flag to ocaml-find-requires (to avoid circular
# dependencies) we also have to explicitly depend on the right version
# of ocaml-runtime.
Requires:       ocaml-runtime%{?_isa} = %{version}-%{release}

# Force ocaml-srpm-macros to be at the latest version, both for builds
# and installs, since OCaml 5.2 has a different set of native code
# generators than previous versions.
BuildRequires:  ocaml-srpm-macros >= 10
Requires:       ocaml-srpm-macros >= 10

Provides:       ocaml(compiler) = %{version}

%if %{native_compiler}
%global __ocaml_requires_opts -c -f '%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte' -i Dynlink_cmo_format -i Dynlink_cmxs_format
%else
%global __ocaml_requires_opts -c -f '%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte' -i Backend_intf -i Inlining_decision_intf -i Simplify_boxed_integer_ops_intf
%endif
%global __ocaml_provides_opts -f '%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte'

%description
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler
and an optimizing native-code compiler), an interactive toplevel system,
parsing tools (Lex,Yacc), a replay debugger, a documentation generator,
and a comprehensive library.


%package runtime
# LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception: the project as a whole
# LicenseRef-Fedora-Public-Domain: the MD5 implementation in runtime/caml/md5.h
#   and runtime/md5.c
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND LicenseRef-Fedora-Public-Domain
Summary:        OCaml runtime environment
Requires:       util-linux
Provides:       ocaml(runtime) = %{version}

# Bundles an MD5 implementation in runtime/caml/md5.h and runtime/md5.c
Provides:       bundled(md5-plumb)

%description runtime
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains the runtime environment needed to run OCaml
bytecode.


%package source
Summary:        Source code for OCaml libraries
Requires:       ocaml%{?_isa} = %{version}-%{release}

%description source
Source code for OCaml libraries.


%package ocamldoc
# LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception: the project as a whole
# LicenseRef-Fedora-Public-Domain: ocamldoc/ocamldoc.sty
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND LicenseRef-Fedora-Public-Domain
Summary:        Documentation generator for OCaml
Requires:       ocaml%{?_isa} = %{version}-%{release}
Provides:       ocamldoc = %{version}

%description ocamldoc
Documentation generator for OCaml.


%package docs
Summary:        Documentation for OCaml
BuildArch:      noarch
Requires:       ocaml = %{version}-%{release}


%description docs
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains man pages.


%package compiler-libs
Summary:        Compiler libraries for OCaml
Requires:       ocaml%{?_isa} = %{version}-%{release}


%description compiler-libs
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains some modules used internally by the OCaml
compilers, useful for the development of some OCaml applications.
Note that this exposes internal details of the OCaml compiler which
may not be portable between versions.


%package rpm-macros
# LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception: the project as a whole
# BSD-3-Clause: ocaml_files.py
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND BSD-3-Clause
Summary:        RPM macros for building OCaml packages
BuildArch:      noarch
Requires:       ocaml = %{version}-%{release}
Requires:       python3


%description rpm-macros
This package contains macros that are useful for building OCaml RPMs.


%prep
%autosetup -S git -n %{name}-%{version}%{rcver}
# Patches touch configure.ac, so rebuild it:
autoconf --force


%build
%ifnarch %{no_parallel_build_arches}
make="%make_build"
%else
unset MAKEFLAGS
make=make
%endif

# Set ocamlmklib default flags to include Fedora linker flags
sed -i '/ld_opts/s|\[\]|["%{build_ldflags}"]|' tools/ocamlmklib.ml

# Expose a dependency on the math library
sed -i '/^EXTRACAMLFLAGS=/aLINKOPTS=-cclib -lm' otherlibs/unix/Makefile

# Don't use %%configure macro because it sets --build, --host which
# breaks some incorrect assumptions made by OCaml's configure.ac
#
# See also:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/2O4HBOK6PTQZAFAVIRDVMZGG2PYB2QHM/
# https://github.com/ocaml/ocaml/issues/8647
#
# We set --libdir to the unusual directory because we want OCaml to
# install its libraries and other files into a subdirectory.
#
# OC_CFLAGS/OC_LDFLAGS control what flags OCaml passes to the linker
# when doing final linking of OCaml binaries.  Setting these is
# necessary to ensure that generated binaries have Fedora hardening
# features.
./configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir}/ocaml \
    --enable-flambda \
%if %{native_compiler}
    --enable-native-compiler \
    --enable-native-toplevel \
%else
    --disable-native-compiler \
    --disable-native-toplevel \
%endif
%ifarch %{x86_64} %{arm64}
%if 0%{?_include_frame_pointers}
    --enable-frame-pointers \
%endif
%endif
%ifarch %{test_arches}
    --enable-ocamltest \
%else
    --disable-ocamltest \
%endif
    OC_CFLAGS='%{build_cflags}' \
    OC_LDFLAGS='%{build_ldflags}' \
    %{nil}
$make world
%if %{native_compiler}
$make opt
$make opt.opt
%endif

# Build the README and fix up references to other doc files
asciidoc -d book README.adoc
for fil in CONTRIBUTING.md HACKING.adoc INSTALL.adoc README.win32.adoc; do
  sed -e "s,\"$fil\",\"https://github.com/ocaml/ocaml/blob/trunk/$fil\"," \
      -i README.html
done


%check
%ifarch %{ocaml_native_compiler}
# For information only, compile a binary and dump the annocheck data
# from it.  Useful so we know if hardening is being enabled, but don't
# fail because not every hardening feature can be enabled here.
echo 'print_endline "hello, world"' > hello.ml
./ocamlopt.opt -verbose -I stdlib hello.ml -o hello ||:
annocheck -v hello ||:
%endif

%ifarch %{test_arches}
%ifarch %{test_arches_required}
make -j1 tests
%else
make -j1 tests ||:
%endif
%endif


%install
%make_install
perl -pi -e "s|^$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT%{_libdir}/ocaml/ld.conf

echo %{version} > $RPM_BUILD_ROOT%{_libdir}/ocaml/fedora-ocaml-release

# Remove the installed documentation.  We will install it using %%doc
rm -rf $RPM_BUILD_ROOT%{_docdir}/ocaml

mkdir -p $RPM_BUILD_ROOT%{rpmmacrodir}
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{rpmmacrodir}/macros.ocaml-rpm

mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/redhat
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_rpmconfigdir}/redhat

# Link, rather than copy, identical binaries
hardlink -t $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs


%files
%license LICENSE
%{_bindir}/ocaml

%{_bindir}/ocamlcmt
%{_bindir}/ocamlcp
%{_bindir}/ocamldebug
%{_bindir}/ocamlmklib
%{_bindir}/ocamlmktop
%{_bindir}/ocamlprof
%{_bindir}/ocamlyacc

# symlink to either .byte or .opt version
%{_bindir}/ocamlc
%{_bindir}/ocamldep
%{_bindir}/ocamllex
%{_bindir}/ocamlobjinfo

# bytecode versions
%{_bindir}/ocamlc.byte
%{_bindir}/ocamldep.byte
%{_bindir}/ocamllex.byte
%{_bindir}/ocamlobjinfo.byte

%if %{native_compiler}
# native code versions
%{_bindir}/ocamlc.opt
%{_bindir}/ocamldep.opt
%{_bindir}/ocamllex.opt
%{_bindir}/ocamlobjinfo.opt
%endif

%if %{native_compiler}
%{_bindir}/ocamlnat
%{_bindir}/ocamlopt
%{_bindir}/ocamlopt.byte
%{_bindir}/ocamlopt.opt
%{_bindir}/ocamloptp
%endif

%{_libdir}/ocaml/expunge
%{_libdir}/ocaml/ld.conf
%{_libdir}/ocaml/Makefile.config

%{_libdir}/ocaml/*.a
%if %{native_compiler}
%{_libdir}/ocaml/*.cmxa
%{_libdir}/ocaml/*.cmx
%{_libdir}/ocaml/*.o
%{_libdir}/ocaml/libasmrun_shared.so
%endif
%{_libdir}/ocaml/*.mli
%{_libdir}/ocaml/sys.ml.in
%{_libdir}/ocaml/libcamlrun_shared.so

%{_libdir}/ocaml/{dynlink,runtime_events,str,threads,unix}/*.mli
%if %{native_compiler}
%{_libdir}/ocaml/{dynlink,runtime_events,str,threads,unix}/*.a
%{_libdir}/ocaml/{dynlink,runtime_events,str,threads,unix}/*.cmxa
%{_libdir}/ocaml/{dynlink,profiling,runtime_events,str,threads,unix}/*.cmx
%{_libdir}/ocaml/profiling/*.o
%endif
%if %{natdynlink}
%{_libdir}/ocaml/{runtime_events,str,unix}/*.cmxs
%endif

# headers
%{_libdir}/ocaml/caml


%files runtime
%doc README.html Changes
%license LICENSE
%{_bindir}/ocamlrun
%{_bindir}/ocamlrund
%{_bindir}/ocamlruni
%dir %{_libdir}/ocaml
%{_libdir}/ocaml/*.cmo
%{_libdir}/ocaml/*.cmi
%{_libdir}/ocaml/*.cma
%{_libdir}/ocaml/stublibs
%dir %{_libdir}/ocaml/dynlink
%{_libdir}/ocaml/dynlink/META
%{_libdir}/ocaml/dynlink/*.cmi
%{_libdir}/ocaml/dynlink/*.cma
%dir %{_libdir}/ocaml/profiling
%{_libdir}/ocaml/profiling/*.cmo
%{_libdir}/ocaml/profiling/*.cmi
%dir %{_libdir}/ocaml/runtime_events
%{_libdir}/ocaml/runtime_events/META
%{_libdir}/ocaml/runtime_events/*.cmi
%{_libdir}/ocaml/runtime_events/*.cma
%{_libdir}/ocaml/runtime-launch-info
%{_libdir}/ocaml/stdlib
%dir %{_libdir}/ocaml/str
%{_libdir}/ocaml/str/META
%{_libdir}/ocaml/str/*.cmi
%{_libdir}/ocaml/str/*.cma
%dir %{_libdir}/ocaml/threads
%{_libdir}/ocaml/threads/META
%{_libdir}/ocaml/threads/*.cmi
%{_libdir}/ocaml/threads/*.cma
%dir %{_libdir}/ocaml/unix
%{_libdir}/ocaml/unix/META
%{_libdir}/ocaml/unix/*.cmi
%{_libdir}/ocaml/unix/*.cma
%{_libdir}/ocaml/fedora-ocaml-release


%files source
%license LICENSE
%{_libdir}/ocaml/*.ml
%{_libdir}/ocaml/*.cmt*
%{_libdir}/ocaml/*/*.cmt*


%files ocamldoc
%license LICENSE
%doc ocamldoc/Changes.txt
%{_bindir}/ocamldoc*
%{_libdir}/ocaml/ocamldoc


%files docs
%{_mandir}/man1/*
%{_mandir}/man3/*


%files compiler-libs
%license LICENSE
%{_libdir}/ocaml/compiler-libs


%files rpm-macros
%{rpmmacrodir}/macros.ocaml-rpm
%{_rpmconfigdir}/redhat/ocaml_files.py


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.4.1-4
- Prepare for Oreon 11 (RP1)
