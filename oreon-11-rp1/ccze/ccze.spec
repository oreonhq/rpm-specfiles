%global source0_hash 8263a11183fd356a033b6572958d5a6bb56bfd2dba801ed0bff276cfae528aa3

Name:           ccze
Version:        0.2.1
Release:        %autorelease
Summary:        A robust log colorizer
Summary(ru):    Мощный коллоризатор логов

# http://web.archive.org/web/20040803024236/bonehunter.rulez.org/CCZE.phtml
URL:            http://bonehunter.rulez.org/CCZE.html
License:        GPL-2.0-or-later
Source:         ftp://bonehunter.rulez.org/pub/ccze/stable/ccze-%{version}.tar.gz
# Upstream is dead. So, patch himself.
Patch0:         ccze-0.2.1-Wmulticharacter.patch
# Upstream is dead, port Debian patch to correct handle -o switch
Patch1:         ccze-opts.diff
# Port configure script to C99
Patch2:         ccze-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  ncurses-devel >= 5.0
BuildRequires:  pcre-devel >= 3.1

%description
CCZE is a roboust and modular log colorizer, with plugins for apm,
exim, fetchmail, httpd, postfix, procmail, squid, syslog, ulogd,
vsftpd, xferlog and more.

%description -l ru
CCZE это мощный и модульный раскрашиватель логов. Имеются модули-
-плагины для: apm, exim, fetchmail, httpd, postfix, procmail, squid,
syslog, ulogd, vsftpd, xferlog и другие.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

iconv -f ISO-8859-1 -t UTF-8 THANKS > THANKS.new
touch --reference THANKS THANKS.new
mv -f THANKS.new THANKS

%build
%configure --with-builtins=all
# To avoid problem: /usr/include/errno.h:69: error: two or more data types in declaration specifiers
# we add -D__error_t_defined=1 to inform what errno_t already defined.
%make_build CFLAGS="%{optflags} -D__error_t_defined=1"

%install
%make_install

src/ccze-dump > cczerc
install -Dpm0644 -t %{buildroot}/%{_sysconfdir} cczerc

rm %{buildroot}/%{_includedir}/ccze.h

%files
%doc AUTHORS COPYING ChangeLog ChangeLog-0.1 NEWS README THANKS FAQ
%config(noreplace) %{_sysconfdir}/cczerc
%{_bindir}/ccze
%{_bindir}/ccze-cssdump
%{_mandir}/man1/ccze.1*
%{_mandir}/man1/ccze-cssdump.1*
%{_mandir}/man7/ccze-plugin.7*

%changelog
%autochangelog
