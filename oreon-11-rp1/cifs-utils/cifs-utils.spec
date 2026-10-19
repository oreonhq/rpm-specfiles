%global source0_hash b5321d3ff848d361c129aeec4ec8431642582b7036cb8a2a403667d5909d4172
%define pre_release %nil
%global bash_completion_dir %(pkg-config --variable=completionsdir bash-completion || echo /etc/bash_completion.d)
Name:            cifs-utils
Version:         7.8
Release:        1%{?dist}
Summary:        Utilities for mounting and managing CIFS mounts
License:         GPL-3.0-only
URL:             http://linux-cifs.samba.org/cifs-utils/
Requires:        keyutils
Requires(post):  /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Recommends: %{name}-info%{?_isa} = %{version}-%{release}
Source0:        https://download.samba.org/pub/linux-cifs/cifs-utils/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  keyutils-libs-devel
BuildRequires:  krb5-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libwbclient-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  python3-docutils
# /oreon:deps
%description
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains tools for mounting
shares on Linux using the SMB/CIFS protocol. The tools in this package
work in conjunction with support in the kernel to allow one to mount a
SMB/CIFS share onto a client and use it as if it were a standard Linux
file system.

%package devel
Summary:        Files needed for building plugins for cifs-utils
%description devel
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains the header file
necessary for building ID mapping plugins for cifs-utils.

%package -n pam_cifscreds
Summary:        PAM module to manage NTLM credentials in kernel keyring
%description -n pam_cifscreds
The pam_cifscreds PAM module is a tool for automatically adding
credentials (username and password) for the purpose of establishing
sessions in multiuser mounts.

When a cifs filesystem is mounted with the "multiuser" option, and does
not use krb5 authentication, it needs to be able to get the credentials
for each user from somewhere. The pam_cifscreds module can be used to
provide these credentials to the kernel automatically at login.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}%{pre_release} -p1

%build

grep -F -r -l '/usr/bin/env python' | xargs --no-run-if-empty -n1 sed -i 's@/usr/bin/env python.*@%python3@g'
autoreconf -i
%configure --prefix=/usr ROOTSBINDIR=%{_sbindir}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/request-key.d
install -m 644 contrib/request-key.d/cifs.idmap.conf %{buildroot}%{_sysconfdir}/request-key.d
install -m 644 contrib/request-key.d/cifs.spnego.conf %{buildroot}%{_sysconfdir}/request-key.d
install -Dpm 644 bash-completion/smbinfo %{buildroot}%{_datadir}%{bash_completion_dir}/smbinfo
%oreon_autofiles cifs-utils-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles pam_cifscreds usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cifs-utils-info usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

alternatives --install /etc/cifs-utils/idmap-plugin cifs-idmap-plugin %{_libdir}/%{name}/idmapwb.so 10
%preun

if [ $1 = 0 ]; then
	alternatives --remove cifs-idmap-plugin %{_libdir}/%{name}/idmapwb.so
fi
%package info
Summary: Additional tools for querying information about CIFS mount
Requires: %{name}%{?_isa} = %{version}-%{release}
%description info
This subpackage includes additional tools for querying information
about CIFS mount.

%files -f %{oreon_filedir}/main.list
%files -n cifs-utils-devel -f %{oreon_filedir}/cifs-utils-devel.list
%files -n pam_cifscreds -f %{oreon_filedir}/pam_cifscreds.list
%files -n cifs-utils-info -f %{oreon_filedir}/cifs-utils-info.list

%changelog

%autochangelog
