%global source0_hash a28ee90ac20a996e2fc19cbc36a36c152483085011f3b2ec8dfd913b7a6d9804
Name:           imapfilter
Version:        2.8.3
Release:        1%{?dist}
Summary:        A flexible client side mail filtering utility for IMAP servers
%global forgeurl https://github.com/lefcha/imapfilter/
%forgemeta
License:        MIT
URL:            %forgeurl
Source0:        %{forgeurl}archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         imapfilter-makefile-fix.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
# /oreon:deps
%description
IMAPFilter is a mail filtering utility. It connects to remote mail servers
using the Internet Message Access Protocol (IMAP), sends searching queries
to the server and processes mailboxes based on the results. It can be used
to delete, copy, move, flag, etc. messages residing in mailboxes at the
same or different mail servers. The 4rev1 and 4 versions of the IMAP
protocol are supported.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

CFLAGS=$RPM_OPT_FLAGS make PREFIX=%{_prefix} %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
