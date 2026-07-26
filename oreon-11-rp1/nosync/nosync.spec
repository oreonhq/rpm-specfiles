%global source0_hash 998f21e6e599f6372795ca5d30144362597eb73c9a5a38a6bfe60370feccaf4f

Name:           nosync
Version:        1.1
Release:        22%{?dist}
Summary:        Preload library for disabling file's content synchronization
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://github.com/kjn/%{name}
Source0:        http://github.com/kjn/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Eliminate dependency on ELF constructor ordering
# Solves segfaults during buildroot population in mock with nosync
# enabled for builds with openssl
# "FIPS module installed state definition is modified" changes
# https://bugzilla.redhat.com/show_bug.cgi?id=1837809
# https://github.com/kjn/nosync/pull/4
Patch0:         4.patch

BuildRequires:  make
BuildRequires:  gcc

%description
nosync is a small preload library that can be used to disable
synchronization of file's content with storage devices on GNU/Linux.
It works by overriding implementations of certain standard functions
like fsync or open.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
%makeinstall

%files
%doc AUTHORS README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%{_libdir}/%{name}

%changelog
%autochangelog
