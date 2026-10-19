%global source0_hash 7132eea4bcad5ad753bad635d0808ecb1e5905bf9191318e056cf7dccc3b93c1
%global commit 75e66fe16a3afcb78db5786018487adb63e91793
%global date 20230910
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define name    safekeep
%define version 1.5.1
%define release 7
%define homedir %{_localstatedir}/lib/%{name}
Name:           %{name}
Version:        %{version}^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        The SafeKeep backup system
License:        GPL-2.0-or-later
URL:            http://%{name}.sourceforge.net
Source0:        https://github.com/dimipaun/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source1:        README.Fedora
BuildArch:      noarch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  xmlto
# /oreon:deps
%description
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

%package common
Summary:        The SafeKeep backup system (common component)
Requires:       rdiff-backup
Requires:       python3 >= 3.4
%description common
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the common component of SafeKeep. It is shared in 
between the client/server components.

%package client
Summary:        The SafeKeep backup system (client component)
Requires:       openssh-server
Requires:       coreutils
Requires:       util-linux
Requires:       %{name}-common = %{version}-%{release}
%description client
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the client component of SafeKeep. It should be
installed on all hosts that need to be backed-up.

%package server
Summary:        The SafeKeep backup system (server component)
Requires:       openssh, openssh-clients
Requires:       %{name}-common = %{version}-%{release}
Requires:       crontabs
%description server
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the server component of SafeKeep. It should be
installed on the server on which the data will be backed-up to.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
cp -p %{SOURCE1} .

# Create a sysusers.d config file
cat >safekeep.sysusers.conf <<EOF
u safekeep - 'Used by %{name} to run and store backups.' %{homedir} -
EOF

%build

make %{?_smp_mflags} build
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m 750 "%{buildroot}%{homedir}"
install -d -m 700 "%{buildroot}%{homedir}/.ssh"
install -m0644 -D safekeep.sysusers.conf %{buildroot}%{_sysusersdir}/safekeep.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n safekeep-common -f %{oreon_filedir}/safekeep-common.list
%files -n safekeep-client -f %{oreon_filedir}/safekeep-client.list
%files -n safekeep-server -f %{oreon_filedir}/safekeep-server.list

%changelog

%autochangelog
