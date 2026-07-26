%global source0_hash 7920f884c2adafc82c8e41c46d6f3d22698785c7b3f56f5677a8d5c866396386

%global build_type_safety_c 0

Summary: Improved console FTP client
Name: ncftp
Version: 3.3.0
Release: 3%{?dist}
Epoch: 2
License: ClArtistic AND NTP
URL: http://www.ncftp.com/ncftp/
Source: https://www.ncftp.com/public_ftp/ncftp/ncftp-%{version}-src.tar.gz
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel

%description
Ncftp is an improved FTP client. Ncftp's improvements include support
for command line editing, command histories, recursive gets, automatic
anonymous logins, and more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --enable-signals --enable-ipv6
make STRIPFLAG=""

%install
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
make install DESTDIR=%{buildroot}

%files
%license doc/LICENSE.txt
%doc README* doc/html/
%doc doc/CHANGELOG.txt doc/FIREWALLS_AND_PROXIES.txt
%doc doc/READLINE.txt doc/what_changed_between_v2_v3.txt
%{_bindir}/ncftp
%{_bindir}/ncftpget
%{_bindir}/ncftpput
%{_bindir}/ncftpbatch
%{_bindir}/ncftpls
%{_bindir}/ncftpbookmarks
%{_bindir}/ncftpspooler
%{_mandir}/man1/ncftp.1*
%{_mandir}/man1/ncftpget.1*
%{_mandir}/man1/ncftpput.1*
%{_mandir}/man1/ncftpbatch.1*
%{_mandir}/man1/ncftpls.1*
%{_mandir}/man1/ncftpspooler.1*

%changelog
%autochangelog
