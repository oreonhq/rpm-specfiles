%global source0_hash 9527702a48789084e314e5c08d4115129467ca7ef25983d7214c9439d31ef2a6
Name: kstart
Version: 4.3
Release:        1%{?dist}
Summary:        Daemon version of kinit for Kerberos v5
License: MIT
URL: http://www.eyrie.org/~eagle/software/kstart/
Source0:        http://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
Patch0: https://github.com/rra/kstart/pull/13.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  fakeroot
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
k5start is a modified version of kinit which can use keytabs to authenticate, 
can run as a daemon and wake up periodically to refresh a ticket, and can run 
single commands with its own authentication credentials and refresh those 
credentials until the command exits. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

./bootstrap
%configure --enable-setpag --enable-reduced-depends --with-aklog=%{_bindir}/aklog
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
%post

%systemd_post k5start@\*.service
%systemd_user_post krenew.service
%preun

%systemd_preun k5start@\*.service
%systemd_user_preun krenew.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
