%global source0_hash 6f46c9f2875dfab88a4a9196a5c6616c448e32af9dd6aa2d410593e3cd00f376
%global git 4915c308
%{!?_without_checks:	%{!?_with_checks: %global _without_checks --without-checks}}
%{?_with_checks:	%global enable_checks 1}
%{?_without_checks:	%global enable_checks 0}
Name:		libspf2
Version:	1.2.11
Release:        1%{?dist}
Summary:        An implementation of the SPF specification
License:	BSD or LGPLv2+
Url:		http://www.libspf2.org/
Source0:        %{name}-%{version}-%{git}.tar.xz
Patch1:	0001-remove-libreplace-unneeded-on-Linux.patch
Patch2:	0002-add-include-string-for-memset.patch
Patch3:	CVE-2023-42118-and-other-fixes.patch
BuildConflicts:	perl(Test::Pod::Coverage)
BuildConflicts:	perl(Mail::SPF::Test)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(String::Escape)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
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

ac_cv_func___ns_get16=no
export ac_cv_func___ns_get16
autoreconf -vif
%configure --enable-perl --disable-dependency-tracking
sed -i 's|^sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/%{_lib} %{_libdir}|' libtool
make %{?_smp_mflags} CFLAGS="%{optflags} -fno-strict-aliasing"
sed -i -e 's/\(SHORT_NAMES[[:space:]]*=[[:space:]]*\)NO/\1YES/' Doxyfile
/usr/bin/doxygen
%install
make \
	DESTDIR=%{buildroot} \
	PERL_INSTALL_ROOT=$(grep DESTDIR perl/Makefile &> /dev/null && echo "" || echo %{buildroot}) \
	INSTALLDIRS=vendor \
	INSTALL="install -p" \
	install
find %{buildroot} \( -name perllocal.pod -o -name .packlist \) -delete
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*
rm -f %{buildroot}%{_bindir}/spf*_static
mv -f %{buildroot}%{_bindir}/spfquery	%{buildroot}%{_bindir}/spfquery.libspf2
mv -f %{buildroot}%{_bindir}/spfd	%{buildroot}%{_bindir}/spfd.libspf2
rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la
%oreon_autofiles perl-Mail-SPF_XS usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.*

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
%files -f %{oreon_filedir}/main.list
%files -n libspf2-devel -f %{oreon_filedir}/libspf2-devel.list
%files -n libspf2-apidocs -f %{oreon_filedir}/libspf2-apidocs.list
%files -n perl-Mail-SPF_XS -f %{oreon_filedir}/perl-Mail-SPF_XS.list
%files -n libspf2-progs -f %{oreon_filedir}/libspf2-progs.list

%changelog

%autochangelog
