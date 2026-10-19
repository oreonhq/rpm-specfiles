%global source0_hash 3c9c16972a73bb792752f2e4f1cce7212d7638d5494b5f7e8e19f3819dbf3a19
%undefine _missing_build_ids_terminate_build
%global mver 3.0
Name: guile30
Version: 3.0.11
Release:        1%{?dist}
Summary:        A GNU implementation of Scheme for application extensibility
License: LGPL-3.0-or-later AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain AND GPL-1.0-or-later AND GPL-3.0-or-later
Source0:        https://ftp.gnu.org/gnu/guile/guile-%{version}.tar.gz
URL: https://www.gnu.org/software/guile/
Requires: coreutils
Provides: bundled(gnulib)
Patch0: guile-3.0.7-headers.patch
Patch1: guile-3.0.7-disable-oom-test.patch
Patch2: guile-3.0.7-chroot.patch
Patch4: guile-3.0.7-disable-stackoverflow-test.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libunistring-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(readline)
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
Requires: guile30%{?_isa} = %{version}-%{release} pkgconfig(gmp) pkgconfig(bdw-gc)
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

export CFLAGS="%{optflags} -std=gnu17"
autoreconf -fiv
%configure --disable-static --disable-error-on-warning --program-suffix=%{mver}
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/guile/site/%{mver}
rm -f %{buildroot}%{_libdir}/libguile*.la
rm -f %{buildroot}%{_infodir}/dir
for i in $(seq 1 11); do
  mv %{buildroot}%{_infodir}/guile{,-%{mver}}.info-$i
  sed -i -e 's/guile\.info/guile-%{mver}.info/' %{buildroot}%{_infodir}/guile-%{mver}.info-$i
  sed -i -e 's/\* Guile Reference: (guile)/* Guile %{mver} Reference: (guile-%{mver})/' %{buildroot}%{_infodir}/guile-%{mver}.info-$i
done
mv %{buildroot}%{_infodir}/guile{,-%{mver}}.info
sed -i -e 's/guile\.info/guile-%{mver}.info/' %{buildroot}%{_infodir}/guile-%{mver}.info
sed -i -e 's/\* Guile Reference: (guile)/* Guile %{mver} Reference: (guile-%{mver})/' %{buildroot}%{_infodir}/guile-%{mver}.info
mv %{buildroot}%{_infodir}/r5rs{,-%{mver}}.info
mv %{buildroot}%{_datadir}/aclocal/guile{,-%{mver}}.m4
rm -f %{buildroot}%{_libdir}/libguile*gdb.scm
for i in %{buildroot}%{_infodir}/goops.info; do
    iconv -f iso8859-1 -t utf-8 < $i > $i.utf8 && mv -f ${i}{.utf8,}
done
touch %{buildroot}%{_datadir}/guile/site/%{mver}/slibcat
find %{buildroot}%{_datadir} -name '*.scm' -exec touch -r "%{_specdir}/guile3.spec" '{}' \;
find %{buildroot}%{_libdir} -name '*.go' -exec touch -r "%{_specdir}/guile3.spec" '{}' \;
rm %{buildroot}%{_libdir}/guile/%{mver}/extensions/guile-readline.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make %{?_smp_mflags} check || true
%triggerin -- slib >= 3b4-1

rm -f %{_datadir}/guile/site/%{mver}/slibcat
export SCHEME_LIBRARY_PATH=%{_datadir}/slib/
%{_bindir}/guile%{mver} --fresh-auto-compile --no-auto-compile -c \
    "(use-modules (ice-9 slib)) (require 'new-catalog)" &> /dev/null || \
    rm -f %{_datadir}/guile/site/%{mver}/slibcat
:
%triggerun -- slib >= 3b4-1

if [ "$2" = 0 ]; then
    rm -f %{_datadir}/guile/site/%{mver}/slibcat
fi
%files -f %{oreon_filedir}/main.list
%files -n guile30-devel -f %{oreon_filedir}/guile30-devel.list

%changelog

%autochangelog

