%global source0_hash 6f46c9f2875dfab88a4a9196a5c6616c448e32af9dd6aa2d410593e3cd00f376

# NOTE THAT THE TEST SUITE IS CURRENTLY BROKEN
# USE rpmbuild --with checks TO SEE THIS FOR YOURSELF

# While the library and perlmod each have different versions, there is
# only one release number for both the library and the perlmod, as
# both are in the same source code.

%global git 4915c308

# Use rpmbuild --with checks to try running the broken test suite (disabled by default)
%{!?_without_checks:	%{!?_with_checks: %global _without_checks --without-checks}}
%{?_with_checks:	%global enable_checks 1}
%{?_without_checks:	%global enable_checks 0}

Name:		libspf2
Version:	1.2.11
Release:	20.20210922git%{git}%{?dist}
Summary:	An implementation of the SPF specification
License:	BSD or LGPLv2+
Url:		http://www.libspf2.org/

#Source0:	http://www.libspf2.org/spf/libspf2-%{version}.tar.gz
# Upstream source tree at https://github.com/shevek/libspf2/
# git archive --format tar --prefix libspf2-1.2.10-0e23f41e/ HEAD | xz -c > libspf2-1.2.10-0e23f41e.tar.xz
Source0:	libspf2-%{version}-%{git}.tar.xz
Patch1:	0001-remove-libreplace-unneeded-on-Linux.patch
Patch2:	0002-add-include-string-for-memset.patch
Patch3:	CVE-2023-42118-and-other-fixes.patch

BuildRequires:	gcc
BuildRequires:	automake autoconf libtool
BuildRequires:	doxygen, graphviz
# For perl bindings (Makefile.PL claims Mail::SPF is needed, but it isn't)
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
# For perl test suite
BuildRequires:	perl(Test::Pod), perl(String::Escape)
BuildRequires: make
# POD Coverage is non-existent, causes test suite to fail
BuildConflicts:	perl(Test::Pod::Coverage)
# Perl module fails the standard test suite
BuildConflicts:	perl(Mail::SPF::Test)

%description
libspf2 is an implementation of the SPF (Sender Policy Framework)
specification as found at:
http://www.ietf.org/internet-drafts/draft-mengwong-spf-00.txt
SPF allows email systems to check SPF DNS records and make sure that
an email is authorized by the administrator of the domain name that
it is coming from. This prevents email forgery, commonly used by
spammers, scammers, and email viruses/worms.

A lot of effort has been put into making it secure by design, and a
great deal of effort has been put into the regression tests.

%package devel
Summary:	Development tools needed to build programs that use libspf2
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The libspf2-devel package contains the header files necessary for
developing programs using the libspf2 (Sender Policy Framework)
library.

If you want to develop programs that will look up and process SPF records,
you should install libspf2-devel.

API documentation is in the separate libspf2-apidocs package.

%package apidocs
Summary:	API documentation for the libspf2 library
Requires:	%{name} = %{version}-%{release}
BuildArch: noarch

%description apidocs
The libspf2-apidocs package contains the API documentation for creating
applications that use the libspf2 (Sender Policy Framework) library.

%package -n perl-Mail-SPF_XS
Summary:	An XS implementation of Mail::SPF
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n perl-Mail-SPF_XS
This is an interface to the C library libspf2 for the purpose of
testing. While it can be used as an SPF implementation, you can also
use Mail::SPF, which is a little more perlish.

%package progs
Summary:	Programs for making SPF queries using libspf2
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Requires(postun): /usr/sbin/alternatives, /usr/bin/readlink

%description progs
Programs for making SPF queries and checking their results using libspf2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libspf2-%{version}-%{git}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
# The configure script checks for the existence of __ns_get16 and uses the
# system-supplied version if found, otherwise one from src/libreplace.
# However, this function is marked GLIBC_PRIVATE in recent versions of glibc
# and shouldn't be called even if the configure script finds it. So we make
# sure that the configure script always uses the version in src/libreplace.
# This prevents us getting an unresolvable dependency in the built RPM.
ac_cv_func___ns_get16=no
export ac_cv_func___ns_get16

autoreconf -vif
%configure --enable-perl --disable-dependency-tracking

# Kill bogus RPATHs
sed -i 's|^sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/%{_lib} %{_libdir}|' libtool

make %{?_smp_mflags} CFLAGS="%{optflags} -fno-strict-aliasing"

# Generate API docs
sed -i -e 's/\(SHORT_NAMES[[:space:]]*=[[:space:]]*\)NO/\1YES/' Doxyfile
/usr/bin/doxygen

%install
make \
	DESTDIR=%{buildroot} \
	PERL_INSTALL_ROOT=$(grep DESTDIR perl/Makefile &> /dev/null && echo "" || echo %{buildroot}) \
	INSTALLDIRS=vendor \
	INSTALL="install -p" \
	install

# Clean up after impure perl installation
find %{buildroot} \( -name perllocal.pod -o -name .packlist \) -delete
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

# Don't want statically-linked binaries
rm -f %{buildroot}%{_bindir}/spf*_static

# Rename binaries that will be accessed via alternatives
mv -f %{buildroot}%{_bindir}/spfquery	%{buildroot}%{_bindir}/spfquery.libspf2
mv -f %{buildroot}%{_bindir}/spfd	%{buildroot}%{_bindir}/spfd.libspf2

# Remove libtool archive and static
rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la

%check
%if %{enable_checks}
make -C tests check
LD_PRELOAD=$(pwd)/src/libspf2/.libs/libspf2.so make -C perl test
%endif

%ldconfig_scriptlets

%post progs
/usr/sbin/alternatives --install %{_bindir}/spfquery spf %{_bindir}/spfquery.libspf2 20 \
	--slave %{_bindir}/spfd spf-daemon %{_bindir}/spfd.libspf2
exit 0

%preun progs
if [ $1 = 0 ]; then
	/usr/sbin/alternatives --remove spf %{_bindir}/spfquery.libspf2
fi
exit 0

%postun progs
if [ "$1" -ge "1" ]; then
	spf=`readlink /etc/alternatives/spf`
	if [ "$spf" == "%{_bindir}/spfquery.libspf2" ]; then
		/usr/sbin/alternatives --set spf %{_bindir}/spfquery.libspf2
	fi
fi
exit 0

%files
%license LICENSES
%doc README INSTALL TODO
%{_libdir}/libspf2.so.*

%files devel
%{_includedir}/spf2/
%{_libdir}/libspf2.so

%files apidocs
%doc doxygen/html

%files progs
%{_bindir}/spfd.libspf2
%{_bindir}/spfquery.libspf2
%{_bindir}/spftest
%{_bindir}/spf_example

%files -n perl-Mail-SPF_XS
%{perl_vendorarch}/Mail/
%{perl_vendorarch}/auto/Mail/
%{_mandir}/man3/Mail::SPF_XS.3pm*

%changelog
%autochangelog
