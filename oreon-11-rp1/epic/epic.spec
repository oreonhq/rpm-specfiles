%global source0_hash 133b05aea6a7fd51dc6a67b334859e9cc3b51b469f8178513f62ac8ada73dd87

Summary: An ircII chat client
Name: epic
Version: 3.0
Release: 6%{?dist}
Epoch: 4
License: BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
Source0: ftp://ftp.epicsol.org/pub/epic/EPIC4-PRODUCTION/epic4-%{version}.tar.xz
Source1: ftp://ftp.epicsol.org/pub/epic/EPIC4-PRODUCTION/epic4-help-current.tar.bz2
Source2: epic.wmconfig
Source3: ircII.servers
Source4: http://prdownloads.sourceforge.net/splitfire/sf-1.35.irc.gz
Source5: http://splitfire.sourceforge.net/schemes/sf-bitchx-scheme.irc.gz
Source6: http://splitfire.sourceforge.net/schemes/sf-eggsandham-scheme.irc.gz
Source7: http://splitfire.sourceforge.net/schemes/sf-light-scheme.irc.gz
Source8: http://splitfire.sourceforge.net/schemes/sf-perry-scheme.irc.gz
Patch0: epic-default.patch
Patch1: epic-fix-ftbfs.patch
URL: http://www.epicsol.org/
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: ncurses-devel
BuildRequires: libxcrypt-devel
BuildRequires: make automake autoconf

%description
EPIC (Enhanced Programmable ircII Client) is an advanced ircII chat
client.  Chat clients connect to servers around the world, enabling
you to chat with other people.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

rm -rf $RPM_BUILD_DIR/ircii-EPIC%{prog_version}

%setup -q -n epic4-%{version} -a 1
%autopatch -p0

%build
export CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
autoreconf -vi
%configure

rm -rf help/Makefile help/README_FIRST
find help -type d -name CVS | while read line; do rm -rf $line; done;

make

%install
rm -rf $RPM_BUILD_ROOT

# see INSTALL, -O2 is not usable for epic
export RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed s/-O2/-O/`

make install CFLAGS="$RPM_OPT_FLAGS" installhelp IP=$RPM_BUILD_ROOT prefix=%{_prefix} mandir=%{_mandir} 

rm $RPM_BUILD_ROOT/usr/bin/epic
ln -s epic-EPIC4-%{version} $RPM_BUILD_ROOT/usr/bin/epic 

for file in %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8}; do
	sNAME=`echo $file | sed -e 's/\.gz$//'`;
	bNAME=`basename $sNAME`;
	zcat $file | sed -e 's/^\(\^set HELP_PATH.*\)/#\1/' > $bNAME;
	install $bNAME $RPM_BUILD_ROOT/usr/share/epic/script/
done;

install %{SOURCE3} $RPM_BUILD_ROOT/usr/share/epic/

# remove the CVS dir in the doc dir
rm -rf doc/CVS

# wserv is just not very useful
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/wserv

%files
%doc BUG_FORM INSTALL KNOWNBUGS README UPDATES
%doc doc/*
%license COPYRIGHT
%{_bindir}/*
%{_libexecdir}/*
%dir %{_datadir}/epic
%config(noreplace) %{_datadir}/epic/ircII.servers
%dir %attr(755,root,root) %{_datadir}/epic/script
%attr(644,root,root) %{_datadir}/epic/script/*
%{_mandir}/*/*
%dir %{_datadir}/epic/help
%{_datadir}/epic/help/*

%changelog
%autochangelog
