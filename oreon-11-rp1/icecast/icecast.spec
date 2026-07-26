%global source0_hash 49b5979f9f614140b6a38046154203ee28218d8fc549888596a683ad604e4d44

Name:		icecast
Version:	2.4.4
Release:	26%{?dist}
Summary:	ShoutCast compatible streaming media server

# admin/xspf.xsl:	GPL-2.0-or-later
# COPYING:		    GPL-2.0 text
# src/fserve.c:		GPL-2.0-only
# src/thread/thread.c:	GPL-2.0-or-later
# src/avl/avl.c:	HPND
# web/xml2json.xslt:	BSD-2-Clause
## In doc package only:
# examples/icecast_auth-1.0.tar.gz:
#   config.guess:	GPL-2.0-or-later WITH Autoconf-exception-generic
#   configure:		FSFUL
#   COPYING:		GPL-2.0 text
#   install-sh:		HPND-sell-variant
#   Makefile.in:	FSFULLRWD
## Not in any binary package:
# config.guess:		GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# configure:		FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# doc/assets/img/Makefile.in:	FSFULLRWD
# install-sh:		X11
License:	GPL-2.0-or-later AND GPL-2.0-only AND HPND AND BSD-2-Clause
SourceLicense: %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic AND HPND-sell-variant AND X11 AND FSFULLRWD AND FSFUL
URL:		http://www.%{name}.org/
Source0:	https://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.logrotate
Source2:	%{name}.service
Source3:	%{name}.sysusers
Source4:	%{name}.xml
Source5:	status3.xsl
# Respect a system crypto policy, bug #1645612
Patch0:		icecast-2.4.4-Respect-a-default-cipher-list-defined-by-the-SSL-lib.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	curl-devel >= 7.10.0
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libtheora-devel >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	openssl-devel
BuildRequires:	speex-devel
BuildRequires:	systemd-rpm-macros

Requires:	mailcap
%if 0%{?rhel} < 9
%{?systemd_requires}
%endif
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
%sysusers_requires_compat
%endif

Provides:	streaming-server

%description
Icecast is a streaming media server which currently supports
Ogg Vorbis and MP3 audio streams.  It can be used to create an
Internet radio station or a privately running jukebox and many
things in between.  It is very versatile in that new formats
can be added relatively easily and supports open standards for
communication and interaction.

%package doc
Summary:	Documentation files for %{name}
License:	GPL-2.0-or-later WITH Autoconf-exception-generic AND HPND-sell-variant AND FSFULLRWD AND FSFUL
BuildArch:	noarch

%description doc
This package contains the documentation files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
%{_bindir}/find doc/ -type f | xargs %{__chmod} 0644
%{__cp} -a doc/ html/
%{_bindir}/find html/ -name 'Makefile*' | xargs %{__rm} -f
autoreconf -f

%build
%configure \
	--with-curl \
	--enable-largefile \
	--enable-maintainer-mode \
	--with-ogg \
	--with-openssl \
	--enable-shared \
	--with-speex \
	--disable-static \
	--with-theora \
	--with-vorbis \
	--enable-yp
%make_build

%install
%make_install
rm -fr %{buildroot}%{_datadir}/%{name}/doc
rm -fr %{buildroot}%{_docdir}/%{name}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/icecast.conf
install -Dpm 0640 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}.xml
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_datadir}/%{name}/web/status3.xsl
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}	\
	 %{buildroot}%{_pkgdocdir}/{conf,examples}
cp -a html/ AUTHORS ChangeLog NEWS TODO %{buildroot}%{_pkgdocdir}
cp -a conf/*.dist %{buildroot}%{_pkgdocdir}/conf
cp -a examples/%{name}_auth-1.0.tar.gz %{buildroot}%{_pkgdocdir}/examples

%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
%pre
%sysusers_create_compat %{SOURCE3}
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%config(noreplace) %attr(-,root,%{name}) %{_sysconfdir}/%{name}.xml
%dir %attr(-,%{name},%{name}) %{_localstatedir}/log/%{name}
%doc %dir %{_pkgdocdir}
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{_sysconfdir}/logrotate.d
%{_sysconfdir}/logrotate.d/%{name}
%{_sysusersdir}/icecast.conf
%{_unitdir}/%{name}.service

%files doc
%license %{_datadir}/licenses/%{name}*
%doc %{_pkgdocdir}

%changelog
%autochangelog
