%global source0_hash 8db3f9bf4ef884f24df5f753b8f350898cadbc8e7b346c09c1bd7eb9bd3145fd

# % global alphatag	rc1
%global revision	%{?alphatag:-}%{?alphatag}

Name:		ocspd
Version:	1.9.0
Release:	36%{?alphatag:.}%{?alphatag}%{?dist}
Summary:	OpenCA OCSP Daemon
License:	Apache-1.0
Source:		http://downloads.sourceforge.net/openca/openca-ocspd-%{version}%{revision}.tar.gz
Source1:	ocspd.service
Patch1:		ocspd-1.7.0-bufresponse.patch
Patch2:		ocspd-1.9.0-misc.patch
Patch3:		ocspd-1.7.0-openssl.patch
Patch4:		ocspd-1.7.0-podsyntax.patch
Patch5:		ocspd-1.7.0-badalgorcast.patch
Patch6:		ocspd-1.7.0-badcasts.patch
Patch7:		ocspd-1.7.0-deprecldap.patch
Patch8:		ocspd-1.7.0-threadinit.patch
Patch9:		ocspd-1.7.0-config.patch
Patch10:	ocspd-1.7.0-setgroups.patch
Patch11:	ocspd-1.9.0-stealthy.patch
Patch12:	ocspd-1.9.0-noformat.patch
Patch13:	ocspd-1.9.0-openssl11.patch
URL:		http://www.openca.org/projects/ocspd
Obsoletes:	openca-ocspd <= %{version}-%{release}
Provides:	openca-ocspd = %{version}-%{release}
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:	openssl-devel-engine
%endif
BuildRequires:	openldap-devel
BuildRequires:	automake autoconf
BuildRequires:	perl-podlators
BuildRequires:	systemd-rpm-macros
Requires(post):	systemd
Requires(post):	systemd-sysv
Requires(preun):systemd
Requires(postun):systemd

%description
 The ocspd is an RFC2560 compliant OCSPD responder. It can be used to
verify the status of a certificate using OCSP clients (such as
Mozilla/Firefox/Thunderbird/Apache).

#-------------------------------------------------------------------------------
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#-------------------------------------------------------------------------------

%setup -q -n openca-ocspd-%{version}%{revision}
%patch -P1 -p1 -b .bufresponse
%patch -P2 -p1 -b .misc
%patch -P3 -p1 -b .openssl
%patch -P4 -p1 -b .podsyntax
%patch -P5 -p1 -b .badalgorcast
%patch -P6 -p1 -b .badcasts
%patch -P7 -p1 -b .deprecldap
%patch -P8 -p1 -b .threadinit
%patch -P9 -p1 -b .config
%patch -P10 -p1 -b .setgroups
%patch -P11 -p1 -b .stealthy
%patch -P12 -p1 -b .noformat
%patch -P13 -p1 -b .openssl11

#	Create a sysusers.d config file.
cat > ocspd.sysusers.conf <<EOF
u ocspd - 'OCSP Responder' %{_sysconfdir}/ocspd -
EOF

#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

#	Need automake/autoconf rebuild because of above patches.

aclocal
autoheader
automake --add-missing
autoconf

%ifarch alpha
	ARCH_FLAGS='--host=alpha-redhat-linux'
%endif

%configure ${ARCH_FLAGS} --enable-openssl-engine --with-ocspd-group=ocspd
make %{?_smp_mflags}

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

make DESTDIR='%{buildroot}' install

#	Remove SysV init scripts directory.

rm -rf '%{buildroot}%{_initrddir}'

#	Install systemd service script.

mkdir -p '%{buildroot}%{_unitdir}/'
cp -a '%{SOURCE1}' '%{buildroot}%{_unitdir}/'

#	Install sysusers config file.

install -m 644 -D ocspd.sysusers.conf '%{buildroot}%{_sysusersdir}/ocspd.conf'

#-------------------------------------------------------------------------------
%post
#-------------------------------------------------------------------------------

%systemd_post ocspd.service

#-------------------------------------------------------------------------------
%preun
#-------------------------------------------------------------------------------

%systemd_preun ocspd.service

#-------------------------------------------------------------------------------
%postun
#-------------------------------------------------------------------------------

%systemd_postun_with_restart ocspd.service

#-------------------------------------------------------------------------------
%triggerun -- ocspd < 1.5.1-0.9
#-------------------------------------------------------------------------------

%{_bindir}/systemd-sysv-convert --save ocspd > /dev/null 2>&1 || :
/sbin/chkconfig --del ocspd > /dev/null 2>&1 || :
/bin/systemctl try-restart ocspd.service > /dev/null 2>&1 || :

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%doc AUTHORS COPYING ChangeLog README
%{_sbindir}/*
%dir %{_sysconfdir}/ocspd
%dir %{_sysconfdir}/ocspd/c*
%attr(700, ocspd, root) %dir %{_sysconfdir}/ocspd/private
%config(noreplace) %{_sysconfdir}/ocspd/ocspd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/*
%{_mandir}/*/*
%{_unitdir}/*
%{_sysusersdir}/ocspd.conf

#-------------------------------------------------------------------------------
%changelog
%autochangelog
