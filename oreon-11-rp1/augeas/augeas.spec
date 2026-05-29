%global source0_hash b50ab817b7e246e63af3b489e572542986a3aa88dd63b83616a1f67fd347bf74
%global source1_hash 61da4d20e2a8c7cc6ec98078cc376b62ee8a4437018f04253dfec85521c0a843

Name:           augeas
Version:        1.14.2
Summary:        A library for changing configuration files
License:        LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND (GPL-3.0-or-later WITH Bison-exception-2.2) AND Kazlib AND GPL-2.0-or-later AND BSD-2-Clause AND LicenseRef-Public-Domain

# Upstream Augeas is missing several important fixes which affect
# Fedora.  For this reason we have soft-forked augeas, here:
# https://github.com/rwmjones/augeas/tree/fedora-45
# See also:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/J7SM6NLIMPU7J4LIRBDPTPWVXOKZWWEH/
# %%global forgeurl https://github.com/hercules-team/augeas
# %%global commit af2aa88ab37fc48167d8c5e43b1770a4ba2ff403
%global forgeurl https://github.com/rwmjones/augeas
%global commit ada6219325d9a835b71b62a42c3e150427b91882
%forgemeta

Release:        0.11%{?dist}
URL:            %{forgeurl}
Source0:        https://github.com/rwmjones/augeas/archive/ada6219325d9a835b71b62a42c3e150427b91882/augeas-ada6219325d9a835b71b62a42c3e150427b91882.tar.gz

# The problem with packaging from the upstream git repo is that we
# need to provide our own gnulib submodule.  I created this by doing:
# (cd .gnulib && git archive --format=tar --prefix=.gnulib/ HEAD) |
#   gzip -9 > gnulib-2f7479a16a.tar.gz
Source1:        gnulib-2f7479a16a.tar.gz

Provides:       bundled(gnulib)

BuildRequires:  autoconf, automake, libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  readline-devel
BuildRequires:  libselinux-devel
BuildRequires:  libxml2-devel
BuildRequires:  bash-completion
%if 0%{?fedora} > 40 || 0%{?rhel} > 10 || (0%{?oreon} >= 11)
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
# Don't use _isa here because it's a noarch package.  This dependency
# is just to ensure that the subpackage is updated along with augeas.
Requires:      %{name} = %{version}-%{release}


%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%forgeautosetup -p1
zcat %{SOURCE1} | tar xf -

# Copied from upstream ./bootstrap:
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
# Disable _smp_mflags because parallel tests fail with the git version
# because it tries to run lex and yacc in parallel even though lex
# depends on parser.h from yacc.
# https://github.com/hercules-team/augeas/issues/572
#make %%{?_smp_mflags}
make


%check
# Disable test-preserve.sh SELinux testing. This fails when run under mock due
# to differing SELinux labelling.
export SKIP_TEST_PRESERVE_SELINUX=1

# Tests disabled because gnulib tests fail see:
# https://bugzilla.redhat.com/show_bug.cgi?id=1674672
make %{?_smp_mflags} check || {
  echo '===== tests/test-suite.log ====='
  cat tests/test-suite.log
  exit 1
}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# The tests/ subdirectory contains lenses used only for testing, and
# so it shouldn't be packaged.
rm -r $RPM_BUILD_ROOT%{_datadir}/augeas/lenses/dist/tests

# In 1.9.0, the example /usr/bin/dump gets installed inadvertently
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
# _datadir/augeas and _datadir/augeas/lenses are owned
# by filesystem.
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
%if 0%{?fedora} > 40 || 0%{?rhel} > 10 || (0%{?oreon} >= 11)
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.14.2-0.11.gitada6219
- Import
