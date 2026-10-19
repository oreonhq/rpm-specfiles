%global source0_hash eadf0f7c7705ae08210e93bfa543d6b55b3f4a81e7bd1bbdfa319b52cd75775d
Name:           nfs4-acl-tools
Version:        0.4.2
Release:        10%{?dist}
Summary:        The nfs4 ACL tools
License:        LGPL-2.1-or-later
URL:            http://git.linux-nfs.org/?p=steved/nfs4-acl-tools.git;a=summary
Source0:        http://linux-nfs.org/~steved/nfs4-acl-tools/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package contains commandline ACL utilities for the Linux
NFSv4 client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
	CFLAGS="%{build_cflags} -D_FILE_OFFSET_BITS=64" \
	LDFLAGS="%{build_ldflags}"
%make_build
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.2-10
- Prepare for Oreon 11 (RP1)
