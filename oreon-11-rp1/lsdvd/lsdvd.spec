%global source0_hash 7d2c5bd964acd266b99a61d9054ea64e01204e8e3e1a107abe41b1274969e488

Summary: Small application for listing the contents of DVDs
Name: lsdvd
Version: 0.17
Release: 26%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://sourceforge.net/projects/lsdvd/
Source: http://downloads.sf.net/lsdvd/lsdvd-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: libdvdread-devel
BuildRequires: make

%description
lsdvd is a small application which lists the contents of DVDs to your terminal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-dependency-tracking
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/lsdvd
%{_mandir}/man1/lsdvd.1*

%changelog
%autochangelog
