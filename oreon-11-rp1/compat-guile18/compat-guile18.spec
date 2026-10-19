%global source0_hash c3471fed2e72e5b04ad133bbaaf16369e8360283679bcf19800bc1b381024050
%bcond_without emacs
%global mver 1.8
Summary:        A GNU implementation of Scheme for application extensibility
Name: compat-guile18
Version: %{mver}.8
Release:        1%{?dist}
Source0:        https://mirrors.kernel.org/gnu/guile/guile-%{version}.tar.gz
URL: http://www.gnu.org/software/guile/
Patch1: guile-1.8.7-multilib.patch
Patch2: guile-1.8.7-testsuite.patch
Patch3: guile-1.8.8-deplibs.patch
Patch4: guile-1.8.8-cve-2016-8605.patch
Patch5: guile-1.8.8-configure.patch
Patch6: guile-configure-tz-c99.patch
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND MIT AND BSD-4-Clause-UC
%{?with_emacs:BuildRequires: emacs}
Provides: guile = 5:%{version}-7
Provides: guile%{?_isa} = 5:%{version}-7
Obsoletes: guile < 5:%{version}-7
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
GUILE (GNU's Ubiquitous Intelligent Language for Extension) is a library
implementation of the Scheme programming language, written in C.  GUILE
provides a machine-independent execution platform that can be linked in
as a library during the building of extensible programs.

Install the compat-guile18 package if you'd like to add extensibility to
programs that you are developing.

%package devel
Summary: Libraries and header files for the GUILE extensibility library
Requires: %{name}%{?_isa} = %{version}-%{release} gmp-devel
Requires: pkgconfig
Provides: guile-devel = 5:%{version}-7
Provides: guile-devel%{?_isa} = 5:%{version}-7
Obsoletes: guile-devel < 5:%{version}-7
%description devel
The compat-guile18-devel package includes the libraries, header files, etc.,
that you'll need to develop applications that are linked with the
GUILE extensibility library.

You need to install the compat-guile18-devel package if you want to develop
applications that will be linked to GUILE.  You'll also need to install the
compat-guile18 package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n guile-%{version}

%patch -P1 -p1 -b .multilib
%patch -P2 -p1 -b .testsuite
%patch -P3 -p1 -b .deplibs
%patch -P4 -p1 -b .cve-2016-8605
%patch -P5 -p1 -b .configure
%patch -P6 -p1

%build

export CFLAGS="$RPM_OPT_FLAGS -fwrapv -std=gnu17"
export LDFLAGS="$RPM_LD_FLAGS -Wl,--as-needed"
%configure --disable-static --disable-error-on-warning --disable-rpath
sed -i 's|" $sys_lib_dlsearch_path "|" $sys_lib_dlsearch_path %{_libdir} "|' \
    {,guile-readline/}libtool
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/guile/site
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libguile*.la
rm -rf ${RPM_BUILD_ROOT}%{_infodir}
mv ${RPM_BUILD_ROOT}%{_bindir}/guile{,%{mver}}
mv ${RPM_BUILD_ROOT}%{_bindir}/guile{,%{mver}}-tools
mv ${RPM_BUILD_ROOT}%{_mandir}/man1/guile{,%{mver}}.1
mv ${RPM_BUILD_ROOT}%{_bindir}/guile{,%{mver}}-config
mv ${RPM_BUILD_ROOT}%{_bindir}/guile{,%{mver}}-snarf
mv ${RPM_BUILD_ROOT}%{_datadir}/aclocal/guile{,%{mver}}.m4
sed -i -e 's|/usr/bin/guile|/usr/bin/guile%{mver}|' \
    ${RPM_BUILD_ROOT}%{_bindir}/guile%{mver}-config
sed -i -e 's|guile-tools|guile%{mver}-tools|g' \
    ${RPM_BUILD_ROOT}%{_bindir}/guile%{mver}-tools
sed -i -e 's|guile-snarf|guile%{mver}-snarf|g' \
    ${RPM_BUILD_ROOT}%{_bindir}/guile%{mver}-snarf
ac=${RPM_BUILD_ROOT}%{_datadir}/aclocal/guile%{mver}.m4
sed -i -e 's|,guile|,guile%{mver}|g' $ac
sed -i -e 's|guile-tools|guile%{mver}-tools|g' $ac
sed -i -e 's|guile-config|guile%{mver}-config|g' $ac
sed -i -e 's|GUILE_PROGS|GUILE1_8_PROGS|g' $ac
sed -i -e 's|GUILE_FLAGS|GUILE1_8_FLAGS|g' $ac
sed -i -e 's|GUILE_SITE_DIR|GUILE1_8_SITE_DIR|g' $ac
sed -i -e 's|GUILE_CHECK|GUILE1_8_CHECK|g' $ac
sed -i -e 's|GUILE_MODULE_CHECK|GUILE1_8_MODULE_CHECK|g' $ac
sed -i -e 's|GUILE_MODULE_AVAILABLE|GUILE1_8_MODULE_AVAILABLE|g' $ac
sed -i -e 's|GUILE_MODULE_REQUIRED|GUILE1_8_MODULE_REQUIRED|g' $ac
sed -i -e 's|GUILE_MODULE_EXPORTS|GUILE1_8_MODULE_EXPORTS|g' $ac
sed -i -e 's|GUILE_MODULE_REQUIRED_EXPORT|GUILE1_8_MODULE_REQUIRED_EXPORT|g' $ac
bzip2 NEWS
touch $RPM_BUILD_ROOT%{_datadir}/guile/%{mver}/slibcat
ln -s ../../slib $RPM_BUILD_ROOT%{_datadir}/guile/%{mver}/slib
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libguile-srfi-srfi-1-v-3.so.3.0.2
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libguile-srfi-srfi-4-v-3.so.3.0.1
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libguile-srfi-srfi-13-14-v-3.so.3.0.1
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libguile-srfi-srfi-60-v-2.so.2.0.2
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/guile1.8
%oreon_autofiles compat-guile18-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make %{?_smp_mflags} check
%ldconfig_scriptlets
%triggerin -- slib

rm -f %{_datadir}/guile/site/slib{,cat}
ln -sfT ../../slib %{_datadir}/guile/%{mver}/slib
rm -f %{_datadir}/guile/%{mver}/slibcat
export SCHEME_LIBRARY_PATH=%{_datadir}/slib/
for pre in \
    "(use-modules (ice-9 slib))" \
    "(load \"%{_datadir}/slib/guile.init\")"
do
    %{_bindir}/guile%{mver} -c "$pre
        (set! implementation-vicinity (lambda ()
        \"%{_datadir}/guile/%{mver}/\"))
        (require 'new-catalog)" &> /dev/null && break
    rm -f %{_datadir}/guile/%{mver}/slibcat
done
:
%triggerun -- slib

if [ "$2" = 0 ]; then
    rm -f %{_datadir}/guile/%{mver}/slib{,cat}
fi
%files -f %{oreon_filedir}/main.list
%files -n compat-guile18-devel -f %{oreon_filedir}/compat-guile18-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.8-50
- Import
