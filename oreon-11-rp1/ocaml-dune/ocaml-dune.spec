# TESTING NOTE: The testsuite requires numerous packages, many of which are
# built with dune.  Furthermore, the testsuite assumes it is running in a git
# checkout, and has access to the Internet.  We cannot satisfy any of these
# conditions on a koji builder, so we do not run the test suite.

# docs are not needed in RHEL, and add unwanted build dependencies
%bcond docs %{undefined rhel}

# These are the only libraries currently required by Fedora, along with the
# dependencies of those libraries:
# - dune-build-info required by alt-ergo
# - dune-configurator required by many packages (e.g., ocaml-lwt)
# - dune-site and its dependencies required by frama-c and ocaml-camomile
# - xdg required by utop
%global pkgbuild dune-build-info,dune-configurator,dune-private-libs,dune-site,dyn,fs-io,ordering,stdune,top-closure,xdg

%global giturl  https://github.com/ocaml/dune

Name:           ocaml-dune
Version:        3.23.1
Release:        1%{?dist}
Summary:        Composable build system for OCaml and Reason

# Dune itself is MIT.  Some bundled libraries have a different license:
# BSD-2-Clause:
# - vendor/ocaml-blake3-mini
# BSD-3-Clause:
# - otherlibs/dune-rpc/dbus_address.mll
# - vendor/bigstringaf
# ISC:
# - vendor/cmdliner
# - vendor/notty
# - vendor/sha
# - vendor/uutf
# LGPL-2.1-only:
# - vendor/incremental-cycles
# LGPL-2.1-only WITH OCaml-LGPL-linking-exception
# - vendor/ocaml-inotify
# - vendor/opam
# - vendor/opam-file-format
# - vendor/re
# LGPL-2.1-or-later
# - src/dune_pkg/opam_solver.*
# - src/sat/hash_set.*
# - src/sat/sat.*
# MIT:
# - vendor/build_path_prefix_map
# - vendor/csexp
# - vendor/ocaml-lmdb
# - vendor/lwd
# - vendor/pp
# - vendor/spawn
License:        MIT AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-2.1-only AND LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND LGPL-2.1-or-later
URL:            https://dune.build
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/dune-%{version}.tar.gz
# Unbundle lmdb
Patch:          %{name}-unbundle-lmdb.patch
# Unbundle libev
Patch:          %{name}-unbundle-libev.patch
# Temporary workaround for broken debuginfo (rhbz#2168932)
# See https://github.com/ocaml/dune/issues/6929
Patch:          %{name}-debuginfo.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  emacs-nw
BuildRequires:  libev-devel
BuildRequires:  make
BuildRequires:  ocaml >= 4.14
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-csexp-devel >= 1.5.0
BuildRequires:  ocaml-pp-devel >= 2.0.0
BuildRequires:  ocaml-rpm-macros
BuildRequires:  pkgconfig(lmdb)

%if %{with docs}
BuildRequires:  %{py3_dist furo}
BuildRequires:  %{py3_dist myst-parser}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-copybutton}
BuildRequires:  %{py3_dist sphinx-design}
%endif

# Dune has vendored deps to avoid dependency cycles.  Upstream deliberately
# does not support unbundling these dependencies.
# See https://github.com/ocaml/dune/issues/220
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

# This is needed for the dune-related RPM macros
Requires:       ocaml-rpm-macros

# The dune rules module requires Toploop
Requires:       ocaml-compiler-libs%{?_isa}

# This can be removed when F42 reaches EOL
Obsoletes:      ocaml-fiber < 3.7.0
Obsoletes:      ocaml-fiber-devel < 3.7.0
Provides:       ocaml-fiber = %{version}-%{release}
Provides:       ocaml-fiber-devel = %{version}-%{release}

# This can be removed when F48 reaches EOL
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

# Install documentation in the main package doc directory
%global _docdir_fmt %{name}

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
# The content is MIT.  Other licenses are due to files added by sphinx.
# BSD-2-Clause:
# - _static/basic.css
# - _static/doctools.js
# - _static/documentation_options.js
# - _static/file.png
# - _static/language_data.js
# - _static/minus.png
# - _static/plus.png
# - _static/searchtools.js
# - _static/sphinx_highlight.js
# MIT:
# - _static/check-solid.svg
# - _static/clipboard.min.js
# - _static/copy-button.svg
# - _static/copybutton.css
# - _static/copybutton.js
# - _static/copybutton_funcs.js
# - _static/design-style.*.min.css
# - _static/design-tabs.js
# - _static/css
# - _static/js
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
# We also want the libraries
_boot/dune.exe build -p dune,%{pkgbuild} %{?_smp_mflags} --verbose \
  --profile dune-bootstrap

%if %{with docs}
%make_build doc
%endif

%install
%make_install

# Install the libraries
_boot/dune.exe install --destdir=%{buildroot} -p %{pkgbuild}

# We use %%doc below
rm -fr %{buildroot}%{_prefix}/doc

# Byte compile the Emacs files
cd %{buildroot}%{_emacs_sitelispdir}
%_emacs_bytecompile *.el
cd -

# Generate %%files lists
%ocaml_files -s

%files
%license LICENSE.md
%doc CHANGES.md README.md
%{_bindir}/dune
%{_mandir}/man*/dune*

%if %{with docs}
%files doc
%doc doc/_build/*
%endif

%files emacs
%{_emacs_sitelispdir}/dune*

%files configurator -f .ofiles-dune-configurator
%dir %{ocamldir}/dune/
%{ocamldir}/dune/META

%files configurator-devel -f .ofiles-dune-configurator-devel
%{ocamldir}/dune/dune-package
%{ocamldir}/dune/opam

%files -n ocaml-xdg -f .ofiles-xdg

%files -n ocaml-xdg-devel -f .ofiles-xdg-devel

%files build-info -f .ofiles-dune-build-info

%files build-info-devel -f .ofiles-dune-build-info-devel

%files private-libs -f .ofiles-dune-private-libs

%files private-libs-devel -f .ofiles-dune-private-libs-devel

%files site -f .ofiles-dune-site

%files site-devel -f .ofiles-dune-site-devel

%files -n ocaml-dyn -f .ofiles-dyn

%files -n ocaml-dyn-devel -f .ofiles-dyn-devel

%files -n ocaml-fs-io -f .ofiles-fs-io

%files -n ocaml-fs-io-devel -f .ofiles-fs-io-devel

%files -n ocaml-ordering -f .ofiles-ordering

%files -n ocaml-ordering-devel -f .ofiles-ordering-devel

%files -n ocaml-stdune -f .ofiles-stdune

%files -n ocaml-stdune-devel -f .ofiles-stdune-devel

%files -n ocaml-top-closure -f .ofiles-top-closure

%files -n ocaml-top-closure-devel -f .ofiles-top-closure-devel

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.23.1-1
- Import
