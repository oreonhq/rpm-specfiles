%global source1_hash 20b688f92ba5a6d093bee5444efe167466178a8d266b8e855f34912c70e9b481
%global source0_hash 72a951cb0ad622785a8962801f005a3a412736c7e7e3ce152f176287c52fe062
%bcond_with	otr
%define		perl_vendorarch	%(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
Summary:        Modular text mode IRC client with Perl scripting
Name:		irssi
Version:	1.4.5
Release:        1%{?dist}
License:	gpl-2.0-or-later AND gpl-2.0-only AND gfdl-1.1-or-later AND licenseref-fedora-public-domain AND hpnd-markus-kuhn
URL:		http://irssi.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:	gpgkey-7EE65E3082A5FB06AC7C368D00CCB587DDBEF0E1.asc
Source3:	irssi-config.h
%if %{with otr}
%endif
Requires:	perl(lib)
Requires:	perl(Symbol)
Patch0:		irssi-1.4.1-botti-perl-link-fix.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconf-pkg-config
BuildRequires:  utf8proc-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n irssi-devel -f %{oreon_filedir}/irssi-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.5-11
- Prepare for Oreon 11 (RP1)
