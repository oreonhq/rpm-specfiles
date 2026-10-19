%global source0_hash 7b0180c8bda0df15c627a99a105e41f76d421c19a8f7f8f256da7eb2fec991b5
%bcond check 1
%global selinuxtype targeted
%global modulename opkssh
%global goipath         github.com/openpubkey/opkssh
Version:                0.13.0
%gometa -L -f
Name:           opkssh
Release:        1%{?dist}
Summary:        OpenPubkey SSH
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND Unlicense
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        opkssh-providers
Source4:        opkssh-auth_id
Source5:        ssh-opkssh.conf
Source6:        sudoers-opkssh
Source7:        sysuser-opkssh.conf
Source8:        logrotate.conf
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  bzip2
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
OpenPubkey SSH is a tool which enables ssh to be used with OpenID Connect
allowing SSH access to be managed via identities like alice@example.com instead
of long-lived SSH keys.

# Split the server into a separate package to avoid opkssh authentication available
# on client-only systems. This improves security by reducing the attack surface.
%package server
Summary:        Server configuration for OpenPubkey SSH
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       (opkssh-server-selinux if selinux-policy-%{selinuxtype})
%description server
Server configuration for opkssh (OpenPubkey SSH).

%package server-selinux
Summary:        SELinux policy for OpenPubkey SSH
BuildArch:      noarch
Requires(post): selinux-policy-%{selinuxtype}
%description server-selinux
SELinux policy for opkssh (OpenPubkey SSH).

%package doc
Summary:        Documentation for OpenPubkey SSH
BuildArch:      noarch
%description doc
Documentation for opkssh (OpenPubkey SSH).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X main.Version=%{version} \
                   -X main.logFilePathServer=/var/log/opkssh/opkssh.log"
%gobuild -o %{gobuilddir}/bin/opkssh %{goipath}
make -f %{_datadir}/selinux/devel/Makefile opkssh.pp
bzip2 -9 opkssh.pp
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0640 -vp -D %{SOURCE3} %{buildroot}%{_sysconfdir}/opk/providers
install -m 0640 -vp -D %{SOURCE4} %{buildroot}%{_sysconfdir}/opk/auth_id
install -m 0600 -vp -D %{SOURCE5} %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/60-opkssh.conf
install -m 0440 -vp -D %{SOURCE6} %{buildroot}%{_sysconfdir}/sudoers.d/opkssh
install -m 0644 -vp -D %{SOURCE7} %{buildroot}%{_sysusersdir}/opkssh.conf
install -m 0644 -vp -D opkssh.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/targeted/opkssh.pp.bz2
install -m 0644 -vp -D %{SOURCE8} %{buildroot}%{_sysconfdir}/logrotate.d/opkssh.conf
mkdir -p %{buildroot}%{_localstatedir}/log/opkssh
touch %{buildroot}%{_localstatedir}/log/opkssh/opkssh.log
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%pre server

%sysusers_create_compat %{SOURCE6}
%pre server-selinux

%selinux_relabel_pre -s %{selinuxtype}
%post server-selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%postun server-selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi
%posttrans server-selinux

%selinux_relabel_post -s %{selinuxtype}
%files -f %{oreon_filedir}/main.list
%files -n opkssh-server -f %{oreon_filedir}/opkssh-server.list
%files -n opkssh-server-selinux -f %{oreon_filedir}/opkssh-server-selinux.list
%files -n opkssh-doc -f %{oreon_filedir}/opkssh-doc.list

%changelog

%autochangelog
