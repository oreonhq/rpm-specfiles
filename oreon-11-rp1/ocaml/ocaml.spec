%global source0_hash ae47728d0a876665ccc7b745e3a8d8c9ca5ba63c4f7a11d4db6cdbd1dbeef4bb
%undefine _package_note_flags
%global _lto_cflags %{nil}
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
ExcludeArch: %{ix86}
%global test_arches aarch64 %{power64} riscv64 s390x x86_64
%global test_arches_required NONE
%global rcver %{nil}
Name:           ocaml
Version:        5.5.1
Release:        1%{?dist}
Summary:        OCaml compiler and programming environment
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://www.ocaml.org
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/refs/tags/%{version}.tar.gz#/%{name}-5.4.%{native_compiler}.tar.gz
Source1:        macros.ocaml-rpm
Source2:        ocaml_files.py
Patch:          0001-Don-t-add-rpaths-to-libraries.patch
Patch:          0002-configure-Allow-user-defined-C-compiler-flags.patch
Requires:       gcc
Requires:       redhat-rpm-config
Requires:       libzstd-devel%{?_isa}
Requires:       ocaml-runtime%{?_isa} = %{version}-%{release}
Requires:       ocaml-srpm-macros >= 10
Provides:       ocaml(compiler) = %{version}
%global __ocaml_requires_opts -c -f '%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte' -i Backend_intf -i Inlining_decision_intf -i Simplify_boxed_integer_ops_intf
%global __ocaml_provides_opts -f '%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte'
# oreon:deps
BuildRequires:  /usr/bin/annocheck
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  hardlink
BuildRequires:  make
BuildRequires:  ocaml-srpm-macros
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3-pygments
BuildRequires:  util-linux
# /oreon:deps
%description
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler
and an optimizing native-code compiler), an interactive toplevel system,
parsing tools (Lex,Yacc), a replay debugger, a documentation generator,
and a comprehensive library.

%package runtime
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND LicenseRef-Fedora-Public-Domain
Summary:        OCaml runtime environment
Requires:       util-linux
Provides:       ocaml(runtime) = %{version}
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
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND BSD-3-Clause
Summary:        RPM macros for building OCaml packages
BuildArch:      noarch
Requires:       ocaml = %{version}-%{release}
Requires:       python3
%description rpm-macros
This package contains macros that are useful for building OCaml RPMs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
sed -i '/ld_opts/s|\[\]|["%{build_ldflags}"]|' tools/ocamlmklib.ml
sed -i '/^EXTRACAMLFLAGS=/aLINKOPTS=-cclib -lm' otherlibs/unix/Makefile
./configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir}/ocaml \
    --enable-flambda \
    --disable-native-compiler \
    --disable-native-toplevel \
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
asciidoc -d book README.adoc
for fil in CONTRIBUTING.md HACKING.adoc INSTALL.adoc README.win32.adoc; do
  sed -e "s,\"$fil\",\"https://github.com/ocaml/ocaml/blob/trunk/$fil\"," \
      -i README.html
done
%check

%ifarch %{ocaml_native_compiler}
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
rm -rf $RPM_BUILD_ROOT%{_docdir}/ocaml
mkdir -p $RPM_BUILD_ROOT%{rpmmacrodir}
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{rpmmacrodir}/macros.ocaml-rpm
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/redhat
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_rpmconfigdir}/redhat
hardlink -t $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-runtime -f %{oreon_filedir}/ocaml-runtime.list
%files -n ocaml-source -f %{oreon_filedir}/ocaml-source.list
%files -n ocaml-ocamldoc -f %{oreon_filedir}/ocaml-ocamldoc.list
%files -n ocaml-docs -f %{oreon_filedir}/ocaml-docs.list
%files -n ocaml-compiler-libs -f %{oreon_filedir}/ocaml-compiler-libs.list
%files -n ocaml-rpm-macros -f %{oreon_filedir}/ocaml-rpm-macros.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.4.1-4
- Prepare for Oreon 11 (RP1)
