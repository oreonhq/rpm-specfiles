%global source0_hash 5422078bda23d5baa60fcbf0a11d25d20f1a1fda526aab430585fe63fce5eef7

Name:           fastback
Version:        0.4
Release:        33%{?dist}
Summary:        File uploader, configureable file uploader

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fedorahosted.org/fastback
Source0:        http://fedorahosted.org/released/fastback/fastback-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires: openssl-devel
Requires: openssl

%if 0%{?rhel} && 0%{?rhel} <= 5
BuildRequires: curl-devel
%else
BuildRequires: libcurl-devel
%endif  
BuildRequires: make

%description
Fastback is a command line tool to upload files to a ticketing system, or
other configurable URL (FTP,SCP,...).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README FIXME
/usr/bin/fastback
/usr/bin/fastback-unload-receipt
%attr(0644,root,root) %config(noreplace) /etc/fastback.conf

%changelog
%autochangelog
