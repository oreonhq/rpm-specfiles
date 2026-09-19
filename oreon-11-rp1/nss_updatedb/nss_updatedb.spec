%global source0_hash a0f95ec12eb2a986774bf7f6738925ccb9ee588ae99d1fa7a771bd1d07676ab1

Name:		nss_updatedb
Version:	10
Release:	34%{?dist}
Summary:	Maintains a local cache of network directory user and group information

License:	GPL-1.0-or-later
URL:		http://www.padl.com/OSS/%{name}.html
Source0:	http://www.padl.com/download/%{name}.tgz
Patch0: nss_updatedb-configure-c99.patch

#BuildRequires:	db4-devel
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libdb-devel

%description
The nss_updatedb utility maintains a local cache of network directory user
and group information. Used in conjunction with the pam_ccreds module, 
it provides a mechanism for disconnected use of network directories.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -ldb"

%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}/
install -p %{name} $RPM_BUILD_ROOT/%{_sbindir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/%name-%{version}

%files
%doc ChangeLog README COPYING AUTHORS
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*gz

%changelog
%autochangelog
