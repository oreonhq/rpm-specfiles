%global source0_hash e3e2c2e3abf37898138db5b6c1d1dc35c9160c5978be7947d2c741705251d445
%global api_version 1.19
%undefine _auto_set_build_flags
%global __brp_mangle_shebangs_exclude_from /usr/share/automake-%{api_version}
%bcond_without check
%bcond_without automake_enables_optional_test
Summary:        A GNU tool for automatically creating Makefiles
Name:       automake
Version:    %{api_version}
Release:        1%{?dist}
License:    GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Texinfo-exception AND GFDL-1.3-or-later AND FSFAP AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND LicenseRef-Public-Domain
Source0:        https://mirrors.kernel.org/gnu/automake/automake-%{version}.tar.xz
Patch:        fort2.patch
URL:        http://www.gnu.org/software/automake/
Requires:   autoconf >= 2.65
Requires:   perl(Thread::Queue)
Requires:   perl(threads)
BuildArch:  noarch
%if %{with check}
%if %{with automake_enables_optional_test}
%if !0%{?rhel:1} || (0%{?oreon} >= 11)
%endif
%endif
%endif
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Automake::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Automake::
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  cscope
BuildRequires:  dejagnu
BuildRequires:  emacs
BuildRequires:  expect
BuildRequires:  findutils
BuildRequires:  flex
BuildRequires:  gcc-gfortran
BuildRequires:  gcc-objc
BuildRequires:  gcc-objc++
BuildRequires:  gettext-devel
BuildRequires:  help2man
BuildRequires:  imake
BuildRequires:  libtool
BuildRequires:  lzip
BuildRequires:  make
BuildRequires:  ncompress
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sharutils
BuildRequires:  texinfo-tex
BuildRequires:  texlive-dvips
BuildRequires:  vala
# /oreon:deps
%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

You should install Automake if you are developing software and would
like to use its ability to automatically generate GNU standard
Makefiles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%if %{with check} && %{with automake_enables_optional_test}
autoreconf -iv
%endif

%build

%configure
%make_build
cp m4/acdir/README README.aclocal
cp contrib/multilib/README README.multilib
%install
%make_install
%oreon_autofiles main

%check

%if %{with check}
make -k %{?_smp_mflags} check %{?TESTS_FLAGS: TESTS="%{TESTS_FLAGS}"} \
    || ( cat ./test-suite.log && false )
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
