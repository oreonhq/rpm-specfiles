%global source0_hash 3c4facfef1bc1f96235808865665b94857e6e508ce346bfc36b53b775fd8423c
%bcond docs %{undefined rhel}
%global pkgbuild dune-build-info,dune-configurator,dune-private-libs,dune-site,dyn,fs-io,ordering,stdune,top-closure,xdg
%global giturl  https://github.com/ocaml/dune
Name:           ocaml-dune
Version:        3.24.2
Release:        1%{?dist}
Summary:        Composable build system for OCaml and Reason
License:        MIT AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-2.1-only AND LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND LGPL-2.1-or-later
URL:            https://dune.build
VCS:            git:%{giturl}.git
Source0:        https://github.com/ocaml/dune/archive/refs/tags/3.24.2.tar.gz#/dune-3.23.1.tar.gz
Patch:          %{name}-unbundle-lmdb.patch
Patch:          %{name}-unbundle-libev.patch
Patch:          %{name}-debuginfo.patch
ExcludeArch:    %{ix86}
%if %{with docs}
%endif
Provides:       bundled(ocaml-bigstringaf) = 0.10.0
Provides:       bundled(ocaml-blake3-mini) = c6aa40e5f1973c2e6b736660ce2c8dcd3b3f9c9f
Provides:       bundled(ocaml-build-path-prefix-map) = 0.3
Provides:       bundled(ocaml-cmdliner) = 1.2.0
Provides:       bundled(ocaml-csexp) = 1.5.2
Provides:       bundled(ocaml-incremental-cycles) = 1e2030a5d5183d84561cde142eecca40e03db2a3
Provides:       bundled(ocaml-inotify) = 2.3
Provides:       bundled(ocaml-lmdb) = 1.1
Provides:       bundled(ocaml-lwd) = 0.3
Provides:       bundled(ocaml-notty) = 0.2.3
Provides:       bundled(ocaml-opam) = 2.2.0
Provides:       bundled(ocaml-opam-file-format) = 2.1.6
Provides:       bundled(ocaml-pp) = 2.0.0
Provides:       bundled(ocaml-re) = 1.13.2
Provides:       bundled(ocaml-sha) = 1.15.4
Provides:       bundled(ocaml-spawn) = 0.15.1
Provides:       bundled(ocaml-uutf) = 1.0.4
Provides:       dune = %{version}-%{release}
Requires:       ocaml-rpm-macros
Requires:       ocaml-compiler-libs%{?_isa}
Obsoletes:      ocaml-fiber < 3.7.0
Obsoletes:      ocaml-fiber-devel < 3.7.0
Provides:       ocaml-fiber = %{version}-%{release}
Provides:       ocaml-fiber-devel = %{version}-%{release}
Obsoletes:      ocaml-chrome-trace < 3.21.0
Obsoletes:      ocaml-chrome-trace-devel < 3.21.0
Obsoletes:      ocaml-dune-action-plugin < 3.21.0
Obsoletes:      ocaml-dune-action-plugin-devel < 3.21.0
Obsoletes:      ocaml-dune-glob < 3.21.0
Obsoletes:      ocaml-dune-glob-devel < 3.21.0
Obsoletes:      ocaml-dune-rpc < 3.21.0
Obsoletes:      ocaml-dune-rpc-devel < 3.21.0
Obsoletes:      ocaml-ocamlc-loc < 3.21.0
Obsoletes:      ocaml-ocamlc-loc-devel < 3.21.0
Provides:       ocaml-chrome-trace = %{version}-%{release}
Provides:       ocaml-chrome-trace-devel = %{version}-%{release}
Provides:       ocaml-dune-action-plugin = %{version}-%{release}
Provides:       ocaml-dune-action-plugin-devel = %{version}-%{release}
Provides:       ocaml-dune-glob = %{version}-%{release}
Provides:       ocaml-dune-glob-devel = %{version}-%{release}
Provides:       ocaml-dune-rpc = %{version}-%{release}
Provides:       ocaml-dune-rpc-devel = %{version}-%{release}
Provides:       ocaml-ocamlc-loc = %{version}-%{release}
Provides:       ocaml-ocamlc-loc-devel = %{version}-%{release}
%global _docdir_fmt %{name}
# oreon:deps
BuildRequires:  emacs-nw
BuildRequires:  libev-devel
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-csexp-devel
BuildRequires:  ocaml-pp-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  python3dist(furo)
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinx-design)
# /oreon:deps
%description
Dune is a build system designed for OCaml/Reason projects only.  It focuses on
providing the user with a consistent experience and takes care of most of the
low-level details of OCaml compilation. All you have to do is provide a
description of your project and Dune will do the rest.

The scheme it implements is inspired from the one used inside Jane Street and
adapted to the open source world.  It has matured over a long time and is used
daily by hundred of developers, which means that it is highly tested and
productive.

%if %{with docs}
%package        doc
License:        MIT AND BSD-2-Clause
Summary:        HTML documentation for %{name}
BuildArch:      noarch
%description    doc
HTML documentation for dune, a composable build system for OCaml.
%endif

%package        emacs
Summary:        Emacs support for %{name}
License:        ISC
Requires:       %{name} = %{version}-%{release}
Requires:       emacs-filesystem >= %{?_emacs_version}%{!?_emacs_version:0}
BuildArch:      noarch
%description    emacs
The %{name}-devel package contains Emacs integration with the dune build
system, a mode to edit dune files, and flymake support for dune files.

## Dune libraries

%package        configurator
Summary:        Helper library for gathering system configuration
License:        MIT
%description    configurator
Dune-configurator is a small library that helps write OCaml scripts that test
features available on the system, in order to generate config.h files for
instance.  Among other things, dune-configurator allows one to:

- test if a C program compiles
- query pkg-config
- import a #define from OCaml header files
- generate a config.h file

%package        configurator-devel
Summary:        Development files for %{name}-configurator
License:        MIT
Requires:       %{name}-configurator%{?_isa} = %{version}-%{release}
Requires:       ocaml-csexp-devel%{?_isa}
%description    configurator-devel
The ocaml-dune-configurator-devel package contains libraries and signature
files for developing applications that use ocaml-dune-configurator.

%package     -n ocaml-xdg
Summary:        XDG Base Directory Specification
License:        MIT
%description -n ocaml-xdg
This package contains the XDG Base Directory Specification.

%package     -n ocaml-xdg-devel
Summary:        Development files for ocaml-xdg
License:        MIT
Requires:       ocaml-xdg%{?_isa} = %{version}-%{release}
%description -n ocaml-xdg-devel
The ocaml-xdg-devel package contains libraries and signature files for
developing applications that use ocaml-xdg.

%package        build-info
Summary:        Embed build information in an executable
License:        MIT
%description    build-info
The build-info library allows access to information about how an
executable was built, such as the version of the project at which it was
built or the list of statically linked libraries with their versions.
It supports reporting the version from a version control system during
development to get a precise reference of when the executable was built.

%package        build-info-devel
Summary:        Development files for %{name}-build-info
License:        MIT
Requires:       %{name}-build-info%{?_isa} = %{version}-%{release}
%description    build-info-devel
The ocaml-dune-build-info-devel package contains libraries and signature
files for developing applications that use ocaml-dune-build-info.

%package        private-libs
Summary:        Private dune libraries
License:        MIT
Requires:       ocaml-dyn%{?_isa} = %{version}-%{release}
Requires:       ocaml-stdune%{?_isa} = %{version}-%{release}
%description    private-libs
This package contains code that is shared between various dune-xxx packages.
However, it is not meant for public consumption and provides no stability
guarantee.

%package        private-libs-devel
Summary:        Development files for %{name}-private-libs
License:        MIT
Requires:       %{name}-private-libs%{?_isa} = %{version}-%{release}
Requires:       ocaml-dyn-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-stdune-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-csexp-devel%{?_isa}
Requires:       ocaml-pp-devel%{?_isa}
%description    private-libs-devel
The ocaml-dune-private-libs-devel package contains libraries and signature
files for other dune packages.  Do not use.

%package        site
Summary:        Embed location information inside executables and libraries
License:        MIT
Requires:       %{name}-private-libs%{?_isa} = %{version}-%{release}
%description    site
This library enables embedding location information inside executables and
libraries.

%package        site-devel
Summary:        Development files for %{name}-site
License:        MIT
Requires:       %{name}-site%{?_isa} = %{version}-%{release}
Requires:       %{name}-private-libs-devel%{?_isa} = %{version}-%{release}
%description    site-devel
The ocaml-dune-site-devel package contains libraries and signature files for
developing applications that use ocaml-dune-site.

%package     -n ocaml-dyn
Summary:        Dynamic types
License:        MIT
Requires:       ocaml-ordering%{?_isa} = %{version}-%{release}
%description -n ocaml-dyn
This library supports dynamic types in OCaml.

%package     -n ocaml-dyn-devel
Summary:        Development files for ocaml-dyn
License:        MIT
Requires:       ocaml-dyn%{?_isa} = %{version}-%{release}
Requires:       ocaml-ordering-devel%{?_isa} = %{version}-%{release}
%description -n ocaml-dyn-devel
The ocaml-dyn-devel package contains libraries and signature files for
developing applications that use ocaml-dyn.

%package     -n ocaml-fs-io
Summary:        Filesystem operations
License:        MIT
%description -n ocaml-fs-io
This library is a miscellaneous collection of filesystem operations.

%package     -n ocaml-fs-io-devel
Summary:        Development files for ocaml-fs-io
License:        MIT
Requires:       ocaml-fs-io%{?_isa} = %{version}-%{release}
%description -n ocaml-fs-io-devel
The ocaml-fs-io-devel package contains libraries and signature files for
developing applications that use ocaml-fs-io.

%package     -n ocaml-ordering
Summary:        Element ordering
License:        MIT
%description -n ocaml-ordering
Element ordering in OCaml.

%package     -n ocaml-ordering-devel
Summary:        Development files for ocaml-ordering
License:        MIT
Requires:       ocaml-ordering%{?_isa} = %{version}-%{release}
%description -n ocaml-ordering-devel
The ocaml-ordering-devel package contains libraries and signature files for
developing applications that use ocaml-ordering.

%package     -n ocaml-stdune
Summary:        Dune's unstable standard library
License:        MIT
Requires:       ocaml-dyn%{?_isa} = %{version}-%{release}
Requires:       ocaml-fs-io%{?_isa} = %{version}-%{release}
Requires:       ocaml-ordering%{?_isa} = %{version}-%{release}
Requires:       ocaml-top-closure%{?_isa} = %{version}-%{release}
%description -n ocaml-stdune
This package contains Dune's unstable standard library.

%package     -n ocaml-stdune-devel
Summary:        Development files for ocaml-stdune
License:        MIT
Requires:       ocaml-stdune%{?_isa} = %{version}-%{release}
Requires:       ocaml-dyn-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-fs-io-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-ordering-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-top-closure-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-csexp-devel%{?_isa}
Requires:       ocaml-pp-devel%{?_isa}
%description -n ocaml-stdune-devel
The ocaml-stdune-devel package contains libraries and signature files for
developing applications that use ocaml-stdune.

%package     -n ocaml-top-closure
Summary:        Topological closure
License:        MIT
%description -n ocaml-top-closure
Generic topological closure in OCaml.

%package     -n ocaml-top-closure-devel
Summary:        Development files for ocaml-top-closure
License:        MIT
Requires:       ocaml-top-closure%{?_isa} = %{version}-%{release}
%description -n ocaml-top-closure-devel
The ocaml-top-closure-devel package contains libraries and signature files for
developing applications that use ocaml-top-closure.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n dune-%{version} -p1

# Make sure we don't use the bundled lmdb
rm vendor/ocaml-lmdb/{lmdb.h,mdb.c,midl.*}

# Make sure we don't use the bundled libev
rm -fr src/lev/vendor

%build

./configure \
  --prefix %{_prefix} \
  --bindir %{_bindir} \
  --datadir %{_datadir} \
  --docdir %{_prefix}/doc \
  --etcdir %{_sysconfdir} \
  --libdir %{ocamldir} \
  --libexecdir %{ocamldir} \
  --mandir %{_mandir} \
  --sbindir %{_sbindir}
ocaml boot/bootstrap.ml
_boot/dune.exe build -p dune,%{pkgbuild} %{?_smp_mflags} --verbose \
  --profile dune-bootstrap
%if %{with docs}
%make_build doc
%endif
%install
%make_install
_boot/dune.exe install --destdir=%{buildroot} -p %{pkgbuild}
rm -fr %{buildroot}%{_prefix}/doc
cd %{buildroot}%{_emacs_sitelispdir}
%_emacs_bytecompile *.el
cd -
%ocaml_files -s
%oreon_autofiles ocaml-xdg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-xdg-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ocaml-dyn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-dyn-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ocaml-fs-io usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-fs-io-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ocaml-ordering usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-ordering-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ocaml-stdune usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-stdune-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ocaml-top-closure usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-top-closure-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-dune-doc -f %{oreon_filedir}/ocaml-dune-doc.list
%files -n ocaml-dune-emacs -f %{oreon_filedir}/ocaml-dune-emacs.list
%files -n ocaml-dune-configurator -f %{oreon_filedir}/ocaml-dune-configurator.list
%files -n ocaml-dune-configurator-devel -f %{oreon_filedir}/ocaml-dune-configurator-devel.list
%files -n ocaml-xdg -f %{oreon_filedir}/ocaml-xdg.list
%files -n ocaml-xdg-devel -f %{oreon_filedir}/ocaml-xdg-devel.list
%files -n ocaml-dune-build-info -f %{oreon_filedir}/ocaml-dune-build-info.list
%files -n ocaml-dune-build-info-devel -f %{oreon_filedir}/ocaml-dune-build-info-devel.list
%files -n ocaml-dune-private-libs -f %{oreon_filedir}/ocaml-dune-private-libs.list
%files -n ocaml-dune-private-libs-devel -f %{oreon_filedir}/ocaml-dune-private-libs-devel.list
%files -n ocaml-dune-site -f %{oreon_filedir}/ocaml-dune-site.list
%files -n ocaml-dune-site-devel -f %{oreon_filedir}/ocaml-dune-site-devel.list
%files -n ocaml-dyn -f %{oreon_filedir}/ocaml-dyn.list
%files -n ocaml-dyn-devel -f %{oreon_filedir}/ocaml-dyn-devel.list
%files -n ocaml-fs-io -f %{oreon_filedir}/ocaml-fs-io.list
%files -n ocaml-fs-io-devel -f %{oreon_filedir}/ocaml-fs-io-devel.list
%files -n ocaml-ordering -f %{oreon_filedir}/ocaml-ordering.list
%files -n ocaml-ordering-devel -f %{oreon_filedir}/ocaml-ordering-devel.list
%files -n ocaml-stdune -f %{oreon_filedir}/ocaml-stdune.list
%files -n ocaml-stdune-devel -f %{oreon_filedir}/ocaml-stdune-devel.list
%files -n ocaml-top-closure -f %{oreon_filedir}/ocaml-top-closure.list
%files -n ocaml-top-closure-devel -f %{oreon_filedir}/ocaml-top-closure-devel.list

%changelog

%autochangelog
