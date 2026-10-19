%global source0_hash d9aa07c7429aec19d950ff6fd425c371f77158cd34ff220fc191b2c186c67c7a
Name:		icecast
Version:	2.5.0
Release:        1%{?dist}
Summary:        ShoutCast compatible streaming media server
License:	GPL-2.0-or-later AND GPL-2.0-only AND HPND AND BSD-2-Clause
SourceLicense: %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic AND HPND-sell-variant AND X11 AND FSFULLRWD AND FSFUL
URL:		http://www.%{name}.org/
Source0:        https://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.logrotate
Source2:	%{name}.service
Source3:	%{name}.sysusers
Source4:	%{name}.xml
Source5:	status3.xsl
Patch0:		icecast-2.4.4-Respect-a-default-cipher-list-defined-by-the-SSL-lib.patch
Requires:	mailcap
Provides:	streaming-server
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  curl-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  speex-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n icecast-doc -f %{oreon_filedir}/icecast-doc.list

%changelog

%autochangelog
