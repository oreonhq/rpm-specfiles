%global source0_hash 5a7f679b7dddb455e3a7da57c74f1b39023ff1e3e9e98c58d9c699aa679537ce
Name: mk-configure
Version: 0.40.0
Release:        1%{?dist}
Summary:        A build system on top of bmake
License: BSD-2-Clause AND BSD-4-Clause AND ISC
URL: https://github.com/cheusov/mk-configure/
Source0:        https://github.com/cheusov/mk-configure/archive/%{version}/%{name}-%{version}.tar.gz
Source1: mkcmake.macros
Patch0: 0001-ignore-incompatible-pointer-types-errors.patch
Patch1: prototype-fix.patch
Requires: bmake
Requires: imake
Requires: redhat-rpm-config
BuildArch: noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bmake
BuildRequires:  byacc
BuildRequires:  clang
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
BuildRequires:  groff
BuildRequires:  imake
BuildRequires:  info
BuildRequires:  libbsd-devel
BuildRequires:  libfl-devel
BuildRequires:  lua-devel
BuildRequires:  pkgconfig
BuildRequires:  texinfo
BuildRequires:  zlib-devel
# /oreon:deps
%description
The mk-configure tool is a build system, written in and for bmake
(portable version of NetBSD make) and UNIX tools (shell, awk etc.).

%package doc
Summary: The mk-configure documentation
License: BSD-2-Clause AND ISC AND CC0-1.0
Requires: %{name} = %{version}-%{release}
%description doc
The mk-configure package examples

%global env \
        unset MAKEFLAGS \
        export USE_NM=%{_bindir}/nm \
        export USE_INSTALL=%{_bindir}/install \
        export USE_AWK=%{_bindir}/awk \
        export USE_ID=%{_bindir}/id \
        export USE_CC_COMPILERS='gcc clang' \
        export USE_CXX_COMPILERS='g++ clang' \
        export PREFIX=%{_prefix} \
        export SYSCONFDIR=%{_sysconfdir} \
        export MANDIR=%{_mandir}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{env}
bmake all
%install
%{env}
bmake install DESTDIR=%{buildroot}
install -m644 %{SOURCE1} -D %{buildroot}%{_rpmmacrodir}/macros.mkcmake
rm -rf %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}
chmod -x examples/*/*.in
chmod -x examples/*/*/*.in
cp -r examples %{buildroot}%{_docdir}/%{name}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset MAKEFLAGS
env bmake test-tests
%files -f %{oreon_filedir}/main.list
%files -n mk-configure-doc -f %{oreon_filedir}/mk-configure-doc.list

%changelog

%autochangelog
