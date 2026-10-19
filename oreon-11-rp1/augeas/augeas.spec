%global source0_hash b50ab817b7e246e63af3b489e572542986a3aa88dd63b83616a1f67fd347bf74
%global source1_hash 528538b14c4cc39741a533dee17ef0937fca611f917a9b4866dd0c33c6680f9c
Name:           augeas
Version:        1.15.0
Summary:        A library for changing configuration files
License:        LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND (GPL-3.0-or-later WITH Bison-exception-2.2) AND Kazlib AND GPL-2.0-or-later AND BSD-2-Clause AND LicenseRef-Public-Domain
%global forgeurl https://github.com/rwmjones/augeas
%global commit ada6219325d9a835b71b62a42c3e150427b91882
%forgemeta
Release:        1%{?dist}
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source1:        https://github.com/coreutils/gnulib/archive/2f7479a16a.tar.gz#/gnulib-2f7479a16a.tar.gz
Provides:       bundled(gnulib)
%if 0%{?fedora} > 40 || 0%{?rhel} > 10 || (0%{?oreon} >= 11)
%endif
Requires:       %{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash-completion
BuildRequires:  bash-completion-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl-constant
BuildRequires:  perl-interpreter
BuildRequires:  readline-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n augeas-%{commit}
mkdir -p .gnulib
tar xzf %{SOURCE1} -C .gnulib --strip-components=1

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

export CFLAGS="$CFLAGS -Wno-error=implicit-function-declaration"
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
%oreon_autofiles augeas-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles augeas-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles augeas-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles augeas-bash-completion usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n augeas-devel -f %{oreon_filedir}/augeas-devel.list
%files -n augeas-libs -f %{oreon_filedir}/augeas-libs.list
%files -n augeas-static -f %{oreon_filedir}/augeas-static.list
%files -n augeas-bash-completion -f %{oreon_filedir}/augeas-bash-completion.list

%changelog

%autochangelog
