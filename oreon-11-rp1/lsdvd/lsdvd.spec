%global source0_hash 7d2c5bd964acd266b99a61d9054ea64e01204e8e3e1a107abe41b1274969e488
Summary:        Small application for listing the contents of DVDs
Name: lsdvd
Version: 0.21
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://sourceforge.net/projects/lsdvd/
Source0:        http://downloads.sf.net/lsdvd/lsdvd-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libdvdread-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
