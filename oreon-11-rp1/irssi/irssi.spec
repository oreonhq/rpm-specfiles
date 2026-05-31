%global source0_hash 72a951cb0ad622785a8962801f005a3a412736c7e7e3ce152f176287c52fe062

%if 0%{?rhel} < 10
%bcond_without	otr
%else
%bcond_with	otr
%endif

%define		perl_vendorarch	%(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary:	Modular text mode IRC client with Perl scripting
Name:		irssi
Version:	1.4.5
Release:	11%{?dist}

License:	gpl-2.0-or-later AND gpl-2.0-only AND gfdl-1.1-or-later AND licenseref-fedora-public-domain AND hpnd-markus-kuhn
URL:		http://irssi.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:	gpgkey-7EE65E3082A5FB06AC7C368D00CCB587DDBEF0E1.asc
Source3:	irssi-config.h

BuildRequires:	make
BuildRequires:  libxcrypt-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	pkgconf-pkg-config
BuildRequires:	glib2-devel
BuildRequires:	gnupg2
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::Embed)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	utf8proc-devel
%if %{with otr}
BuildRequires:	libotr-devel
%endif

Requires:	perl(lib)
Requires:	perl(Symbol)
# https://github.com/irssi/irssi/issues/1374
Patch0:		irssi-1.4.1-botti-perl-link-fix.patch

%package devel
Summary:	Development package for irssi
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconf-pkg-config

%description
Irssi is a modular IRC client with Perl scripting. Only text-mode
frontend is currently supported. The GTK/GNOME frontend is no longer
being maintained.

%description devel
This package contains headers needed to develop irssi plugins.

Irssi is a modular IRC client with Perl scripting. Only text-mode
frontend is currently supported. The GTK/GNOME frontend is no longer
being maintained.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
autoreconf -fi
%configure --with-textui		\
	--with-proxy			\
	--with-bot			\
	--with-perl=module		\
	--with-perl-lib=vendor		\
	--enable-true-color		\
	%{?with_otr:--with-otr=yes}	\
	%{!?with_otr:--with-otr=no}

%make_build CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
mv irssi-config.h irssi-config-$(getconf LONG_BIT).h
cp -p %{SOURCE3} irssi-config.h


%install
%make_install
install -p irssi-config-$(getconf LONG_BIT).h $RPM_BUILD_ROOT%{_includedir}/%{name}/irssi-config-$(getconf LONG_BIT).h

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/lib*.*a
rm -Rf $RPM_BUILD_ROOT/%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
find $RPM_BUILD_ROOT%{perl_vendorarch} -type f -a -name '*.bs' -a -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{perl_vendorarch} -type f -a -name .packlist -exec rm {} ';'
chmod -R u+w $RPM_BUILD_ROOT%{perl_vendorarch}


%files
%doc docs/*.txt docs/*.html AUTHORS COPYING NEWS README.md TODO
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/botti
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1*
%{perl_vendorarch}/Irssi*
%{perl_vendorarch}/auto/Irssi


%files devel
%{_includedir}/irssi/
%{_libdir}/pkgconfig/irssi-1.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.5-11
- Prepare for Oreon 11 (RP1)
