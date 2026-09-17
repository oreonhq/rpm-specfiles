%global source0_hash 9d7363010b4ef45b1646f6b5f5027b49bb6a209c502fb84e281c7bd771d56bed

Name:           mbuffer
Version:        20241007
Release:        3%{?dist}
Summary:        Measuring Buffer is an enhanced version of buffer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.maier-komor.de/mbuffer.html
Source0:        http://www.maier-komor.de/software/mbuffer/mbuffer-%{version}.tgz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mt-st
BuildRequires:  mhash-devel
BuildRequires:  autoconf
BuildRequires:  automake

%description
Measuring Buffer is an enhanced version of buffer. It features displayof
throughput, memory-mapped file I/O for huge buffers, and multithreading.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
#autoconf
# suppress detection of MD5_Init functions if openssl-devel
# is available on build system, let only mhash_init be
# detected if the md5 hash feature is enabled
export ac_cv_search_MD5_Init=no
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}/usr/etc/mbuffer.rc

%files
%doc AUTHORS ChangeLog NEWS README
%license LICENSE
%{_mandir}/man1/mbuffer.1*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/mbuffer.rc

%changelog
%autochangelog
