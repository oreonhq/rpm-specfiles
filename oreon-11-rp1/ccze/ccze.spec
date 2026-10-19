%global source0_hash 8263a11183fd356a033b6572958d5a6bb56bfd2dba801ed0bff276cfae528aa3
Name:           ccze
Version:        0.2.1
Release:        1%{?dist}
Summary:        A robust log colorizer
Summary(ru):    Мощный коллоризатор логов
URL:            http://bonehunter.rulez.org/CCZE.html
License:        GPL-2.0-or-later
Source0:        ftp://bonehunter.rulez.org/pub/ccze/stable/ccze-%{version}.tar.gz
Patch0:         ccze-0.2.1-Wmulticharacter.patch
Patch1:         ccze-opts.diff
Patch2:         ccze-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel
# /oreon:deps
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
%make_build CFLAGS="%{optflags} -D__error_t_defined=1"
%install
%make_install
src/ccze-dump > cczerc
install -Dpm0644 -t %{buildroot}/%{_sysconfdir} cczerc
rm %{buildroot}/%{_includedir}/ccze.h
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
