%global source0_hash cdf776ea5f29430b1258209630555beea6d2be5481f9da4d64986b077ff37504

# Guile produces ELF images that are just containers for guile and don't
# include build-ids. https://wingolog.org/archives/2014/01/19/elf-in-guile
%undefine _missing_build_ids_terminate_build

%global mver 2.2

Name: guile22
Version: 2.2.7
Release: 18%{?dist}
Summary: A GNU implementation of Scheme for application extensibility
Source: https://ftp.gnu.org/gnu/guile/guile-%{version}.tar.xz
URL: http://www.gnu.org/software/guile/
License: LGPL-3.0-or-later

BuildRequires: libtool libtool-ltdl-devel gmp-devel readline-devel
BuildRequires: gettext-devel libunistring-devel libffi-devel gc-devel
BuildRequires: make
BuildRequires: libxcrypt-devel
Requires: coreutils

Provides: bundled(gnulib)

Patch1: guile-multilib.patch
Patch3: guile-threadstest.patch
Patch4: disable-out-of-memory-test.patch
Patch5: guile-configure.patch
Patch6: guile22-configure-tz-c99.patch
Patch7: guile22-configure-c99.patch

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

# Our gdb doesn't support guile yet
rm -f $RPM_BUILD_ROOT%{_libdir}/libguile*gdb.scm

for i in $RPM_BUILD_ROOT%{_infodir}/goops.info; do
    iconv -f iso8859-1 -t utf-8 < $i > $i.utf8 && mv -f ${i}{.utf8,}
done

touch $RPM_BUILD_ROOT%{_datadir}/guile/site/%{mver}/slibcat

# Adjust mtimes so they are all identical on all architectures.
# When guile.x86_64 and guile.i686 are installed at the same time on an x86_64 system,
# the *.scm files' timestamps change, as they normally reside in /usr/share/guile/.
# Their corresponding compiled *.go file go to /usr/lib64/, or /usr/lib/, depending on the arch.
# The mismatch in timestamps between *.scm and *.go files makes guile to compile itself
# everytime it's run. The following code adjusts the files so that their timestamps are the same
# for every file, but unique between builds.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1208760.
find $RPM_BUILD_ROOT%{_datadir} -name '*.scm' -exec touch -r "%{_specdir}/guile22.spec" '{}' \;
find $RPM_BUILD_ROOT%{_libdir} -name '*.go' -exec touch -r "%{_specdir}/guile22.spec" '{}' \;

# Remove Libtool archive
rm $RPM_BUILD_ROOT%{_libdir}/guile/%{mver}/extensions/guile-readline.la

%check
make %{?_smp_mflags} check

%triggerin -- slib >= 3b4-1
rm -f %{_datadir}/guile/site/%{mver}/slibcat
export SCHEME_LIBRARY_PATH=%{_datadir}/slib/

# Build SLIB catalog
%{_bindir}/guile2.2 --fresh-auto-compile --no-auto-compile -c \
    "(use-modules (ice-9 slib)) (require 'new-catalog)" &> /dev/null || \
    rm -f %{_datadir}/guile/site/%{mver}/slibcat
:

%triggerun -- slib >= 3b4-1
if [ "$2" = 0 ]; then
    rm -f %{_datadir}/guile/site/%{mver}/slibcat
fi

%files
%license COPYING COPYING.LESSER LICENSE
%doc AUTHORS HACKING README THANKS
%{_bindir}/guild%{?mver}
%{_bindir}/guile%{?mver}
%{_bindir}/guile-tools%{?mver}
%{_libdir}/libguile*.so.*
%{_libdir}/guile
%dir %{_datadir}/guile
%dir %{_datadir}/guile/%{mver}
%{_datadir}/guile/%{mver}/ice-9
%{_datadir}/guile/%{mver}/language
%{_datadir}/guile/%{mver}/oop
%{_datadir}/guile/%{mver}/rnrs
%{_datadir}/guile/%{mver}/scripts
%{_datadir}/guile/%{mver}/srfi
%{_datadir}/guile/%{mver}/sxml
%{_datadir}/guile/%{mver}/system
%{_datadir}/guile/%{mver}/texinfo
%{_datadir}/guile/%{mver}/web
%{_datadir}/guile/%{mver}/guile-procedures.txt
%{_datadir}/guile/%{mver}/*.scm
%dir %{_datadir}/guile/site
%dir %{_datadir}/guile/site/%{mver}
%ghost %{_datadir}/guile/site/%{mver}/slibcat
%{_infodir}/*
%{_mandir}/man1/guile%{?mver}*

%files devel
%{_bindir}/guile-config%{?mver}
%{_bindir}/guile-snarf%{?mver}
%{_datadir}/aclocal/*
%{_libdir}/libguile-%{mver}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/guile

%changelog
%autochangelog
