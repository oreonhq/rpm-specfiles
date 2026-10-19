%global source12_hash 7c722015b3d16b6a48bec1b6f79dd7369cfd0de70731f17b94c27553f7e08096
%global source11_hash 8971b3bc892590fb94faf6ce16af9a543038f799f37f73ffd4dabe020914ab35
%global source10_hash 32e78df32121fa65312f0948f614dab8c7414ccfedbc5e2c70a8cf468fe89cbe
%global source9_hash b67365307a2b21c1ba2ecf444c3e4895244559d8c5bd40cc2ead4d33fe27cd11
%global source8_hash 140e41c1ab4c0523b46b0e89f3316945ae4b5328e661da87aebfc33628d92b57
%global source7_hash 9f0ba59b55caadeb658ba2d5cc51f0a76136d4bb5fffe008bbd5c911b42ac43f
%global source6_hash 5924b9e974f6fa592cea29cbe93a07b5d7e08bbf2e98145f7ae7157305946b4a
%global source5_hash 3583352bf60cb9013907b880868c1eeee053d2dd647a4f9e388a34cba373622d
%global source4_hash 2a7be4004acc3881357b2e11db1a8937f4d64d37d8ce38872cefe1c7c4a2a6ef
%global source3_hash 470406981b7638869acb4ecc75e2fd079b5999b5aeeb8324b9b475fe07bca935
%global source1_hash 8272ba5ec733f39f1c33ca8910939bb07f3a40ad3e85120d95fe06f8642a43a1
%global source0_hash 6eedc184c546b5f2b8d2dc3f8189255235fcf26b09953d8477ab9768b8827b4f
%global nm_dispatcher_dir %{_prefix}/lib/NetworkManager
%global puppet_libdir %{ruby_vendorlibdir}
%global puppet_vendor_mod_dir %{_datadir}/%{name}/vendor_modules
Name:           puppet
Version:        8.10.0
Release:        4%{?dist}
Summary:        Network tool for managing many disparate systems
License:        Apache-2.0
URL:            https://puppet.com
Source0:        https://downloads.puppetlabs.com/puppet/%{name}-%{version}.tar.gz
Source1:        https://downloads.puppetlabs.com/puppet/%{name}-%{version}.tar.gz.asc
Source2:        RPM-GPG-KEY-puppet-20250406
Source3:        https://forge.puppet.com/v3/files/puppetlabs-augeas_core-1.5.0.tar.gz
Source4:        https://forge.puppet.com/v3/files/puppetlabs-cron_core-1.3.0.tar.gz
Source5:        https://forge.puppet.com/v3/files/puppetlabs-host_core-1.3.0.tar.gz
Source6:        https://forge.puppet.com/v3/files/puppetlabs-mount_core-1.3.0.tar.gz
Source7:        https://forge.puppet.com/v3/files/puppetlabs-scheduled_task-3.2.0.tar.gz
Source8:        https://forge.puppet.com/v3/files/puppetlabs-selinux_core-1.4.0.tar.gz
Source9:        https://forge.puppet.com/v3/files/puppetlabs-sshkeys_core-2.5.0.tar.gz
Source10:       https://forge.puppet.com/v3/files/puppetlabs-yumrepo_core-2.1.0.tar.gz
Source11:       https://forge.puppet.com/v3/files/puppetlabs-zfs_core-1.6.1.tar.gz
Source12:       https://forge.puppet.com/v3/files/puppetlabs-zone_core-1.2.0.tar.gz
Source13:       puppet-nm-dispatcher.systemd
Source14:       start-puppet-wrapper
Source15:       logrotate
Patch:          0001-Avoid-closing-directory-we-re-iterating.patch
Patch:          openvox-dnf5.patch
BuildArch: noarch
Requires: hiera >= 3.3.1
Requires: facter >= 4.3.0
Requires: rubygem(concurrent-ruby) >= 1.1.9
Requires: rubygem(deep_merge) >= 1.0
Requires: rubygem(facter) >= 4.3.0
Requires: rubygem(multi_json) >= 1.13
Requires: rubygem(puppet-resource_api) >= 1.5
Requires: rubygem(semantic_puppet) >= 1.0.2
Requires: rubygem(scanf) >= 1.0
Requires: ruby-augeas >= 0.5.0
Requires: (ruby-default-gems < 3.3 or rubygem(racc))
Requires: augeas >= 1.10.1
Requires: augeas-libs >= 1.10.1
Requires: ruby(selinux) libselinux-utils
Obsoletes: puppet-headless < 6.0.0
Obsoletes: puppet-server < 6.0.0
Obsoletes: puppet < 6.0.0
# oreon:deps
BuildRequires:  facter
BuildRequires:  gnupg2
BuildRequires:  hiera
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygem-json
BuildRequires:  systemd
# /oreon:deps
%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp -a %{sources} .
for f in puppetlabs-*.tar*; do
  tar xvf $f
done
# Puppetlabs messed up with default paths
find -type f -exec \
  sed -i \
    -e 's|/etc/puppetlabs/puppet|%{_sysconfdir}/%{name}|' \
    -e 's|/etc/puppetlabs/code|%{_sysconfdir}/%{name}/code|' \
    -e 's|/opt/puppetlabs/puppet/bin|%{_bindir}|' \
    -e 's|/opt/puppetlabs/puppet/cache|%{_sharedstatedir}/%{name}|' \
    -e 's|/opt/puppetlabs/puppet/public|%{_sharedstatedir}/%{name}/public|' \
    -e 's|/opt/puppetlabs/puppet/share/locale|%{_datadir}/%{name}/locale|' \
    -e 's|/opt/puppetlabs/puppet/modules|%{_datadir}/%{name}/modules|' \
    -e 's|/opt/puppetlabs/puppet/vendor_modules|%{_datadir}/%{name}/vendor_modules|' \
    -e 's|/var/log/puppetlabs/puppet|%{_localstatedir}/log/%{name}|' \
  '{}' +

# Create a sysusers.d config file
cat >puppet.sysusers.conf <<EOF
u puppet 52 'Puppet' - -
EOF

%install
ruby install.rb --destdir=%{buildroot} \
 --bindir=%{_bindir} \
 --configdir=%{_sysconfdir}/%{name} \
 --codedir=%{_sysconfdir}/%{name}/code \
 --logdir=%{_localstatedir}/log/%{name} \
 --rundir=%{_rundir}/%{name} \
 --localedir=%{_datadir}/%{name}/locale \
 --vardir=%{_sharedstatedir}/%{name} \
 --publicdir=%{_sharedstatedir}/%{name}/public \
 --sitelibdir=%{puppet_libdir}
mkdir -p %{buildroot}%{_datadir}/%{name}/vendor_modules
for d in $(find -mindepth 1 -maxdepth 1 -type d -name 'puppetlabs-*'); do
  modver=${d#*-}
  mod=${modver%-*}
  cp -a $d %{buildroot}%{_datadir}/%{name}/vendor_modules/$mod
done
install -Dp -m0644 %{SOURCE15} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -d -m0755 %{buildroot}%{_unitdir}
install -Dp -m0644 ext/systemd/puppet.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m0644 puppet.sysusers.conf %{buildroot}%{_sysusersdir}/puppet.conf
rm %{buildroot}%{_sysconfdir}/%{name}/hiera.yaml
install -Dpv -m0755 %{SOURCE13} \
 %{buildroot}%{nm_dispatcher_dir}/dispatcher.d/98-%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a ext/ %{buildroot}%{_datadir}/%{name}
install -Dp -m0755 %{SOURCE14} %{buildroot}%{_bindir}/start-puppet-agent
sed -i 's|^ExecStart=.*/bin/puppet|ExecStart=%{_bindir}/start-puppet-agent|' \
 %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "D %{_rundir}/%{name} 0755 %{name} %{name} -" > \
 %{buildroot}%{_tmpfilesdir}/%{name}.conf
rm -r %{buildroot}%{_datadir}/%{name}/ext/{debian,osx,solaris,suse,windows,systemd,redhat}
rm %{buildroot}%{_datadir}/%{name}/ext/{build_defaults.yaml,project_data.yaml}
%oreon_autofiles main

%post

%systemd_post %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
