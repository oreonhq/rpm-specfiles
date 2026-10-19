%global source0_hash cdf776ea5f29430b1258209630555beea6d2be5481f9da4d64986b077ff37504
%undefine _missing_build_ids_terminate_build
%global mver 2.2
Name: guile22
Version: 2.2.7
Release:        1%{?dist}
Summary:        A GNU implementation of Scheme for application extensibility
Source0:        https://ftp.gnu.org/gnu/guile/guile-%{version}.tar.xz
URL: http://www.gnu.org/software/guile/
License: LGPL-3.0-or-later
Requires: coreutils
Provides: bundled(gnulib)
Patch1: guile-multilib.patch
Patch3: guile-threadstest.patch
Patch4: disable-out-of-memory-test.patch
Patch5: guile-configure.patch
Patch6: guile22-configure-tz-c99.patch
Patch7: guile22-configure-c99.patch
# oreon:deps
BuildRequires:  gc-devel
BuildRequires:  gettext-devel
BuildRequires:  gmp-devel
BuildRequires:  libffi-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libunistring-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
GUILE (GNU's Ubiquitous Intelligent Language for Extension) is a library
implementation of the Scheme programming language, written in C.  GUILE
provides a machine-independent execution platform that can be linked in
as a library during the building of extensible programs.

Install the guile package if you'd like to add extensibility to programs
that you are developing.

%package devel
Summary: Libraries and header files for the GUILE extensibility library
Requires: guile22%{?_isa} = %{version}-%{release} gmp-devel gc-devel
Requires: pkgconfig
%description devel
The guile-devel package includes the libraries, header files, etc.,
that you'll need to develop applications that are linked with the
GUILE extensibility library.

You need to install the guile-devel package if you want to develop
applications that will be linked to GUILE.  You'll also need to
install the guile package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n guile-%version

%build

autoreconf -fiv
%configure --disable-static --disable-error-on-warning --program-suffix=%{?mver} --disable-rpath
%{make_build}
%install
%{make_install}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/guile/site/%{mver}
rm -f $RPM_BUILD_ROOT%{_libdir}/libguile*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
for i in $(seq 1 10); do
  mv $RPM_BUILD_ROOT%{_infodir}/guile{,-%{mver}}.info-$i
  sed -i -e 's/guile\.info/guile-%{mver}.info/' $RPM_BUILD_ROOT%{_infodir}/guile-%{mver}.info-$i
  sed -i -e 's/\* Guile Reference: (guile)/* Guile %{mver} Reference: (guile-%{mver})/' $RPM_BUILD_ROOT%{_infodir}/guile-%{mver}.info-$i
done
mv $RPM_BUILD_ROOT%{_infodir}/guile{,-%{mver}}.info
sed -i -e 's/guile\.info/guile-%{mver}.info/' $RPM_BUILD_ROOT%{_infodir}/guile-%{mver}.info
sed -i -e 's/\* Guile Reference: (guile)/* Guile %{mver} Reference: (guile-%{mver})/' $RPM_BUILD_ROOT%{_infodir}/guile-%{mver}.info
mv $RPM_BUILD_ROOT%{_infodir}/r5rs{,-%{mver}}.info
mv $RPM_BUILD_ROOT%{_datadir}/aclocal/guile{,-%{mver}}.m4
rm -f $RPM_BUILD_ROOT%{_libdir}/libguile*gdb.scm
for i in $RPM_BUILD_ROOT%{_infodir}/goops.info; do
    iconv -f iso8859-1 -t utf-8 < $i > $i.utf8 && mv -f ${i}{.utf8,}
done
touch $RPM_BUILD_ROOT%{_datadir}/guile/site/%{mver}/slibcat
find $RPM_BUILD_ROOT%{_datadir} -name '*.scm' -exec touch -r "%{_specdir}/guile22.spec" '{}' \;
find $RPM_BUILD_ROOT%{_libdir} -name '*.go' -exec touch -r "%{_specdir}/guile22.spec" '{}' \;
rm $RPM_BUILD_ROOT%{_libdir}/guile/%{mver}/extensions/guile-readline.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make %{?_smp_mflags} check
%triggerin -- slib >= 3b4-1

rm -f %{_datadir}/guile/site/%{mver}/slibcat
export SCHEME_LIBRARY_PATH=%{_datadir}/slib/
%{_bindir}/guile2.2 --fresh-auto-compile --no-auto-compile -c \
    "(use-modules (ice-9 slib)) (require 'new-catalog)" &> /dev/null || \
    rm -f %{_datadir}/guile/site/%{mver}/slibcat
:
%triggerun -- slib >= 3b4-1

if [ "$2" = 0 ]; then
    rm -f %{_datadir}/guile/site/%{mver}/slibcat
fi
%files -f %{oreon_filedir}/main.list
%files -n guile22-devel -f %{oreon_filedir}/guile22-devel.list

%changelog

%autochangelog
