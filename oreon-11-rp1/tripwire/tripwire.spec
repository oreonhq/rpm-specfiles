%global source0_hash 18d40b85f04b8822717d9a3e987887600840a3753f0e9a9f6ab77692d5658450

%define		path_to_vi /bin/vi
%define		path_to_sendmail /usr/sbin/sendmail

Name:		tripwire
Version:	2.4.3.7
Release:	21%{?dist}
Summary:	IDS (Intrusion Detection System)

License:	GPL-2.0-or-later
Source0:	https://github.com/Tripwire/%{name}-open-source/releases/download/%{version}/%{name}-open-source-%{version}.tar.gz
Source1:	tripwire.cron.in
Source3:	tripwire.gif
Source4:	twcfg.txt.in
Source5:	tripwire-setup-keyfiles.in
Source6:	twpol.txt.in
Source7:	README.Fedora.in
Source9:	License-Issues
URL:		https://github.com/Tripwire/%{name}-open-source/

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	openssl-devel
Requires(post):	sed

%description
Tripwire is a very valuable security tool for Linux systems, if  it  is
installed to a clean system. Tripwire should be installed  right  after
the OS installation, and before you have connected  your  system  to  a
network (i.e., before any possibility exists that someone  could  alter
files on your system).

When Tripwire is initially set up, it creates a database  that  records
certain file information. Then when it is run, it compares a designated
set of files and directories to the information stored in the database.
Added or deleted files are flagged and reported, as are any files  that
have changed from their previously recorded state in the database. When
Tripwire is run against system files  on  a  regular  basis,  any  file
changes will be spotted when Tripwire is run. Tripwire will report  the
changes, which will give system administrators a clue that they need to
enact damage control measures immediately if certain  files  have  been
altered.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-open-source-%{version}
%{__cp} -p %{SOURCE3} .

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --sysconfdir=%{_sysconfdir}/tripwire \
           path_to_vi=%{path_to_vi} \
           path_to_sendmail=%{path_to_sendmail}

%{__make} %{?_smp_mflags}

%install
%{__rm} -fr %{buildroot}

# Install the binaries.
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -p -m755 bin/siggen %{buildroot}%{_sbindir}
%{__install} -p -m755 bin/tripwire %{buildroot}%{_sbindir}
%{__install} -p -m755 bin/twadmin %{buildroot}%{_sbindir}
%{__install} -p -m755 bin/twprint %{buildroot}%{_sbindir}

# Install the man pages.
%{__mkdir_p} %{buildroot}%{_mandir}/{man4,man5,man8}
%{__install} -p -m644 man/man4/*.4 %{buildroot}%{_mandir}/man4/
%{__install} -p -m644 man/man5/*.5 %{buildroot}%{_mandir}/man5/
%{__install} -p -m644 man/man8/*.8 %{buildroot}%{_mandir}/man8/

# Create configuration files from templates.
%{__rm} -fr _tmpcfg
%{__mkdir} _tmpcfg
for infile in %{SOURCE1} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} ; do
	outfile=${infile##/*/}
	outfile=${outfile%.*n}
	cat ${infile} |\
	%{__sed} -e 's|@path_to_vi@|%{path_to_vi}|g' |\
	%{__sed} -e 's|@path_to_sendmail@|%{path_to_sendmail}|g' |\
	%{__sed} -e 's|@sysconfdir@|%{_sysconfdir}|g' |\
	%{__sed} -e 's|@sbindir@|%{_sbindir}|g' |\
	%{__sed} -e 's|@vardir@|%{_var}|g' >\
	_tmpcfg/${outfile}
done
%{__mv} _tmpcfg/{tripwire-setup-keyfiles,README.Fedora} .

# Create the reports directory.
%{__install} -d -m700 %{buildroot}%{_var}/lib/tripwire/report

# Install the cron job.
%{__install} -d -m755 %{buildroot}%{_sysconfdir}/cron.daily
%{__install} -p -m755 _tmpcfg/tripwire.cron \
	%{buildroot}%{_sysconfdir}/cron.daily/tripwire-check
%{__rm} _tmpcfg/tripwire.cron

# Install configuration files.
%{__mkdir_p} %{buildroot}%{_sysconfdir}/tripwire
for file in _tmpcfg/* ; do
	%{__install} -p -m644 ${file} %{buildroot}%{_sysconfdir}/tripwire
done

# Install the keyfile setup script
%{__install} -p -m755 tripwire-setup-keyfiles %{buildroot}%{_sbindir}

# Fix permissions on documentation files.
%{__cp} -p %{SOURCE9} .
%{__chmod} 644 \
	ChangeLog COMMERCIAL COPYING TRADEMARK tripwire.gif \
	README.Fedora policy/policyguide.txt License-Issues

%post
# Set the real hostname in twpol.txt
%{__sed} -i -e "s|localhost|$HOSTNAME|g" %{_sysconfdir}/tripwire/twpol.txt

%files
%doc ChangeLog COMMERCIAL COPYING TRADEMARK tripwire.gif
%doc README.Fedora policy/policyguide.txt License-Issues
%attr(0700,root,root) %dir %{_sysconfdir}/tripwire
%config(noreplace) %{_sysconfdir}/tripwire/twcfg.txt
%config(noreplace) %{_sysconfdir}/tripwire/twpol.txt
%attr(0755,root,root) %{_sysconfdir}/cron.daily/tripwire-check
%attr(0700,root,root) %dir %{_var}/lib/tripwire
%attr(0700,root,root) %dir %{_var}/lib/tripwire/report
%{_mandir}/*/*
%attr(0755,root,root) %{_sbindir}/*

%changelog
%autochangelog
