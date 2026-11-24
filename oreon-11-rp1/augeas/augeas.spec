# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f5dbd355cf35b65e54d7b6c1495b4ba4248381ce8ebe0b9a2fc71df31b2eda8c
%global source1_hash 61da4d20e2a8c7cc6ec98078cc376b62ee8a4437018f04253dfec85521c0a843
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           augeas
Version:        1.15.0
Summary:        A library for changing configuration files
License:        LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND (GPL-3.0-or-later WITH Bison-exception-2.2) AND Kazlib AND GPL-2.0-or-later AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain

%global forgeurl https://github.com/rwmjones/augeas
%global commit 8e7cb3a9a2002144081c90647e3a2bc17fb9705f
%forgemeta

Release:        1%{?dist}
URL:            %{forgeurl}
Source0:        augeas-%{commit}.tar.gz

Source1:        gnulib-8e7cb3a9.tar.gz

Provides:       bundled(gnulib)

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  readline-devel
BuildRequires:  libselinux-devel
BuildRequires:  libxml2-devel
BuildRequires:  bash-completion
%if 0%{?fedora} > 40 || 0%{?rhel} > 10
BuildRequires:  bash-completion-devel
%endif

Requires:       %{name}-libs = %{version}-%{release}

%description
A library for programmatically editing configuration files. Augeas parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the file
format and the transformation into a tree.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Libraries for %{name}

%description    libs
The libraries for %{name}.

Augeas is a library for programmatically editing configuration files. It parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel = %{version}-%{release}

%description    static
The %{name}-static package contains static libraries needed to produce
static builds using %{name}.

%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name} = %{version}-%{release}

%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%forgeautosetup -p1
zcat %{SOURCE1} | tar xf -

modules='argz fnmatch getline getopt-gnu gitlog-to-changelog
canonicalize-lgpl isblank locale mkstemp regex safe-alloc selinux-h
stpcpy stpncpy strchrnul strndup sys_wait vasprintf'
.gnulib/gnulib-tool             \
  --lgpl=2                      \
  --with-tests                  \
  --m4-base=gnulib/m4           \
  --source-base=gnulib/lib      \
  --tests-base=gnulib/tests     \
  --aux-dir=build/ac-aux        \
  --libtool                     \
  --quiet                       \
  --import $modules

autoreconf -fiv

%build
%configure \
%ifarch riscv64
    --disable-gnulib-tests \
%endif
    --enable-static
make

%check
export SKIP_TEST_PRESERVE_SELINUX=1

make %{?_smp_mflags} check || {
  echo '===== tests/test-suite.log ====='
  cat tests/test-suite.log
  exit 1
}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm -r $RPM_BUILD_ROOT%{_datadir}/augeas/lenses/dist/tests

rm -f $RPM_BUILD_ROOT/usr/bin/dump

%ldconfig_scriptlets libs

%files
%{_bindir}/augmatch
%{_bindir}/augparse
%{_bindir}/augprint
%{_bindir}/augtool
%{_bindir}/fadot
%doc %{_mandir}/man1/*
%{_datadir}/vim/vimfiles/syntax/augeas.vim
%{_datadir}/vim/vimfiles/ftdetect/augeas.vim

%files libs
%{_datadir}/augeas/lenses/dist
%{_libdir}/*.so.*
%doc AUTHORS COPYING NEWS

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/augeas.pc

%files static
%{_libdir}/libaugeas.a
%{_libdir}/libfa.a

%files bash-completion
%if 0%{?fedora} > 40 || 0%{?rhel} > 10
%dir %{bash_completions_dir}
%{bash_completions_dir}/augmatch
%{bash_completions_dir}/augprint
%{bash_completions_dir}/augtool
%else
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/augmatch
%{_datadir}/bash-completion/completions/augprint
%{_datadir}/bash-completion/completions/augtool
%endif

%changelog
%autochangelog
