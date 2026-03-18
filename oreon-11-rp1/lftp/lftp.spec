Summary:	A sophisticated file transfer program
Name:		lftp
Version:	4.9.3
Release:	6%{?dist}
License:	GPL-3.0-or-later
Source0:	http://lftp.yar.ru/ftp/%{name}-%{version}.tar.xz
URL:		http://lftp.yar.ru/
BuildRequires:	ncurses-devel, gnutls-devel, perl-generators, pkgconfig, readline-devel, gettext
BuildRequires:	zlib-devel, gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: make

Patch1:  lftp-4.0.9-date_fmt.patch
Patch2:  lftp-4.9.2-cdefs.patch
Patch3:  lftp-4.9.2-tls-close.patch
Patch4:  lftp-4.9.3-cert-pem-location.patch

%description
LFTP is a sophisticated ftp/http file transfer program. Like bash, it has job
control and uses the readline library for input. It has bookmarks, built-in
mirroring, and can transfer several files in parallel. It is designed with
reliability in mind.

%package scripts
Summary:	Scripts for lftp
Requires:	lftp >= %{version}-%{release}
BuildArch:	noarch

%description scripts
Utility scripts for use with lftp.

%prep
%setup -q

%patch -P1 -p1 -b .date_fmt
%ifarch ppc64le
%patch -P2 -p1 -b .cdefs
%endif
%patch -P3 -p1 -b .tls-close
%patch -P4 -p1 -b .cert-pem

# Avoid trying to re-run autoconf
touch -r aclocal.m4 configure m4/needtrio.m4

#sed -i.rpath -e '/lftp_cv_openssl/s|-R.*lib||' configure
sed -i.norpath -e \
	'/sys_lib_dlsearch_path_spec/s|/usr/lib |/usr/lib /usr/lib64 /lib64 |' \
	configure

%build
%configure --with-modules --disable-static --with-gnutls --without-openssl --with-debug
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
export tagname=CC
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/lftp/*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/lftp/%{version}/*.so
iconv -f ISO88591 -t UTF8 NEWS -o NEWS.tmp
touch -c -r NEWS NEWS.tmp
mv NEWS.tmp NEWS
# Remove files from $RPM_BUILD_ROOT that we aren't shipping.
#rm $RPM_BUILD_ROOT%{_libdir}/lftp/%{version}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/liblftp-jobs.la
rm $RPM_BUILD_ROOT%{_libdir}/liblftp-tasks.la
rm $RPM_BUILD_ROOT%{_libdir}/liblftp-jobs.so
rm $RPM_BUILD_ROOT%{_libdir}/liblftp-tasks.so
desktop-file-install	\
--dir=%{buildroot}%{_datadir}/applications	\
%{buildroot}/%{_datadir}/applications/lftp.desktop

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc BUGS COPYING ChangeLog FAQ FEATURES README* NEWS THANKS TODO
%config(noreplace) %{_sysconfdir}/lftp.conf
%{_bindir}/lftp
%{_bindir}/lftpget
%{_mandir}/man1/lftp*.1*
%{_mandir}/man5/lftp.conf.5*
%dir %{_libdir}/lftp
%dir %{_libdir}/lftp/%{version}
%{_libdir}/lftp/%{version}/cmd-torrent.so
%{_libdir}/lftp/%{version}/cmd-mirror.so
%{_libdir}/lftp/%{version}/cmd-sleep.so
%{_libdir}/lftp/%{version}/liblftp-network.so
%{_libdir}/lftp/%{version}/liblftp-pty.so
%{_libdir}/lftp/%{version}/proto-file.so
%{_libdir}/lftp/%{version}/proto-fish.so
%{_libdir}/lftp/%{version}/proto-ftp.so
%{_libdir}/lftp/%{version}/proto-http.so
%{_libdir}/lftp/%{version}/proto-sftp.so
%{_libdir}/liblftp-jobs.so.*
%{_libdir}/liblftp-tasks.so.*
%{_datadir}/applications/lftp.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/zsh/site-functions/_lftp



%files scripts
%{_datadir}/lftp


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.9.3-6
- Prepare for Oreon 11 (RP1)
