Name:           nfs4-acl-tools
Version:        0.4.2
Release:        10%{?dist}
Summary:        The nfs4 ACL tools
License:        LGPL-2.1-or-later
URL:            http://git.linux-nfs.org/?p=steved/nfs4-acl-tools.git;a=summary
Source0:        http://linux-nfs.org/~steved/nfs4-acl-tools/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: libtool
BuildRequires: libattr-devel

%description
This package contains commandline ACL utilities for the Linux
NFSv4 client.

%prep
%autosetup -p1

%build
%configure \
	CFLAGS="%{build_cflags} -D_FILE_OFFSET_BITS=64" \
	LDFLAGS="%{build_ldflags}"

%make_build

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%doc COPYING INSTALL README TODO VERSION
%{_bindir}/nfs4_editfacl
%{_bindir}/nfs4_getfacl
%{_bindir}/nfs4_setfacl
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.2-10
- Prepare for Oreon 11 (RP1)
