%global source0_hash 51314bb222c20e963da61724c752e418261a7bfc2408e7b7d619e82a425f6541

Name:		msktutil
Version:	1.2.2
Release:	3%{?dist}
Summary:	Program for interoperability with Active Directory 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/msktutil/msktutil
Source0:	https://github.com/msktutil/msktutil/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	openldap-devel
BuildRequires:	krb5-devel
Requires:	cyrus-sasl-gssapi

%description
Msktutil is a program for interoperability with Active Directory that can
create a computer account in Active Directory, create a system Kerberos keytab,
add and remove principals to and from that keytab, and change the computer
account's password.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license LICENSE
%doc README ChangeLog
%{_mandir}/man1/*
%{_sbindir}/%{name}

%changelog
%autochangelog
