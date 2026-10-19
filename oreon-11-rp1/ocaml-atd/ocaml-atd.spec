%global source0_hash 40e54c8ecdc45794155221f4299c2a9d49170f4ec41424e8c889d235a52d3a55
ExcludeArch: %{ix86}
Name:           ocaml-atd
Version:        4.2.0
Release:        1%{?dist}
Summary:        Adaptable Type Definitions for cross-language data types
License:        BSD-3-Clause
URL:            https://github.com/ahrefs/atd
VCS:            git:%{url}.git
Source0:        https://github.com/ahrefs/atd/releases/download/%{version}/atd-%{version}.tbz
%ifarch %{java_arches}
%endif
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-menhir
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-yojson-devel
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description
ATD stands for Adaptable Type Definitions. It is a syntax for defining
cross-language data types. It is used as input to generate efficient and
type-safe serializers, deserializers and validators. The current target
languages are OCaml and Java.

The following opam packages are provided by the atd project:

* atdgen: executable that generates OCaml code dealing with json and biniou
  data formats
* atdj: executable that generates Java code dealing with json
* atd: library for parsing atd files used by code generators

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-easy-format-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n     ocaml-atdgen
Summary:        Generates efficient JSON serializers, deserializers and validators
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-atdgen-runtime%{?_isa} = %{version}-%{release}
%description -n ocaml-atdgen
Atdgen is a command-line program that takes as input type definitions in the
ATD syntax and produces OCaml code suitable for data serialization and
deserialization.  Two data formats are currently supported, these are biniou
and JSON.  Atdgen-biniou and Atdgen-json will refer to Atdgen used in one
context or the other.  Atdgen was designed with efficiency and durability in
mind.  Software authors are encouraged to use Atdgen directly and to write
tools that may reuse part of Atdgen’s source code.

%package -n     ocaml-atdcpp
Summary:        C++ code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n ocaml-atdcpp
Atdcpp takes type definitions in the ATD format and derives C++ classes that
can read and write JSON data.  This saves the developer the labor writing
boilerplate that converts between dicts and classes.

This allows safe interoperability with other languages supported by ATD such
as D, OCaml, Java, Python or Scala.

%package -n     ocaml-atdd
Summary:        DLang code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n ocaml-atdd
Atdd takes type definitions in the ATD format and derives `dlang` classes that
can read and write JSON data.  This saves the developer the labor writing
boilerplate that converts between dicts and classes.

This allows safe interoperability with other languages supported by ATD such
as C++, OCaml, Java, Python or Scala.

%package -n     ocaml-atdj
Summary:        Java code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n ocaml-atdj
Atdj is a program that generates a Java interface from type definitions.  In
particular, given a set of ATD type definitions, this tool generates a set of
Java classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Java, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the
  ATD specification.

- Details such as optional fields and their associated default values are
  automatically handled.

%package -n     ocaml-atdpy
Summary:        Python/mypy code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n ocaml-atdpy
Atdpy is a program that generates a Python interface from type definitions.
In particular, given a set of ATD type definitions, this tool generates a set
of Python classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Python, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the
  ATD specification.

- Details such as optional fields and their associated default values are
  automatically handled.

%package -n     ocaml-atds
Summary:        ATD Code generator for Scala
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n ocaml-atds
Atds is a program that generates a Scala interface from type definitions.  In
particular, given a set of ATD type definitions, this tool generates a set of
Scala classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Scala, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the
  ATD specification.

- Details such as optional fields and their associated default values are
  automatically handled.

%package -n     ocaml-atdts
Summary:        TypeScript code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n ocaml-atdts
Atdts takes type definitions in the ATD format and derives TypeScript classes
that can read and write JSON data.  This saves the developer the labor writing
boilerplate that converts between dicts and classes.

This allows safe interoperability with other languages supported by ATD such
as C++, OCaml, Java, Scala, or Python.

%package -n     ocaml-atdgen-codec-runtime
Summary:        Runtime for atdgen generated Melange converters
%description -n ocaml-atdgen-codec-runtime
This library contains the types that are used by atdgen's Melange backend.

%package -n     ocaml-atdgen-codec-runtime-devel
Summary:        Development files for ocaml-atdgen-codec-runtime
Requires:       ocaml-atdgen-codec-runtime%{?_isa} = %{version}-%{release}
%description -n ocaml-atdgen-codec-runtime-devel
The ocaml-atdgen-codec-runtime-devel package contains libraries and signature
files for developing applications that use ocaml-atdgen-codec-runtime.

%package -n     ocaml-atdgen-runtime
Summary:        Runtime library for code generated by atdgen
%description -n ocaml-atdgen-runtime
This package should be used only in conjunction with the atdgen code
generator.

%package -n     ocaml-atdgen-runtime-devel
Summary:        Development files for ocaml-atdgen-runtime
Requires:       ocaml-atdgen-runtime%{?_isa} = %{version}-%{release}
Requires:       ocaml-biniou-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}
Obsoletes:      ocaml-atdgen-devel < 2.16.0
Provides:       ocaml-atdgen-devel = %{version}-%{release}
%description -n ocaml-atdgen-runtime-devel
The ocaml-atdgen-runtime-devel package contains libraries and signature files
for developing applications that use ocaml-atdgen-runtime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir atd-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install -s
rm -rf %{buildroot}%{_libdir}/ocaml/atd{cpp,d,gen,j,py,s,ts}
%oreon_autofiles ocaml-atdgen usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atdcpp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atdd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atdj usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atdpy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atds usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atdts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atdgen-codec-runtime usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atdgen-codec-runtime-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ocaml-atdgen-runtime usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-atdgen-runtime-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch %{java_arches}
%dune_check -p atd{,cpp,d,gen,gen-runtime,gen-codec-runtime,j,py,ts}
%else
%dune_check -p atd{,cpp,d,gen,gen-runtime,gen-codec-runtime,py,ts}
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-atd-devel -f %{oreon_filedir}/ocaml-atd-devel.list
%files -n ocaml-atdgen -f %{oreon_filedir}/ocaml-atdgen.list
%files -n ocaml-atdcpp -f %{oreon_filedir}/ocaml-atdcpp.list
%files -n ocaml-atdd -f %{oreon_filedir}/ocaml-atdd.list
%files -n ocaml-atdj -f %{oreon_filedir}/ocaml-atdj.list
%files -n ocaml-atdpy -f %{oreon_filedir}/ocaml-atdpy.list
%files -n ocaml-atds -f %{oreon_filedir}/ocaml-atds.list
%files -n ocaml-atdts -f %{oreon_filedir}/ocaml-atdts.list
%files -n ocaml-atdgen-codec-runtime -f %{oreon_filedir}/ocaml-atdgen-codec-runtime.list
%files -n ocaml-atdgen-codec-runtime-devel -f %{oreon_filedir}/ocaml-atdgen-codec-runtime-devel.list
%files -n ocaml-atdgen-runtime -f %{oreon_filedir}/ocaml-atdgen-runtime.list
%files -n ocaml-atdgen-runtime-devel -f %{oreon_filedir}/ocaml-atdgen-runtime-devel.list

%changelog

%autochangelog
