%global source0_hash 3583352bf60cb9013907b880868c1eeee053d2dd647a4f9e388a34cba373622d

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
# Get these by checking out the right tag from https://github.com/puppetlabs/puppet-agent and:
# sed 's|.\+puppetlabs/\([a-z_-]\+\).git.\+tags/v\?\([0-9\.]\+\)"}|https://forge.puppet.com/v3/files/\1-\2.tar.gz|' configs/components/module-puppetlabs-*.json
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

# ruby-devel does not require the base package, but requires -libs instead
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: rubygem-json
BuildRequires: facter
BuildRequires: hiera
BuildRequires: systemd
BuildRequires: gnupg2
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
# racc was a default gem, is now a bundled gem but shipped as a sepeate package
Requires: (ruby-default-gems < 3.3 or rubygem(racc))
Requires: augeas >= 1.10.1
Requires: augeas-libs >= 1.10.1
Requires: ruby(selinux) libselinux-utils
Obsoletes: puppet-headless < 6.0.0
Obsoletes: puppet-server < 6.0.0
Obsoletes: puppet < 6.0.0

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

# Note(hguemar): Conflicts with config file from hiera package
rm %{buildroot}%{_sysconfdir}/%{name}/hiera.yaml

# Install a NetworkManager dispatcher script to pickup changes to
# /etc/resolv.conf and such (https://bugzilla.redhat.com/532085).
install -Dpv -m0755 %{SOURCE13} \
 %{buildroot}%{nm_dispatcher_dir}/dispatcher.d/98-%{name}

# Install the ext/ directory to %%{_datadir}/%%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a ext/ %{buildroot}%{_datadir}/%{name}

# Install wrappers for SELinux
install -Dp -m0755 %{SOURCE14} %{buildroot}%{_bindir}/start-puppet-agent
sed -i 's|^ExecStart=.*/bin/puppet|ExecStart=%{_bindir}/start-puppet-agent|' \
 %{buildroot}%{_unitdir}/%{name}.service

# Setup tmpfiles.d config
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "D %{_rundir}/%{name} 0755 %{name} %{name} -" > \
 %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Unbundle
# Note(hguemar): remove unrelated OS/distro specific folders
# These mess-up with RPM automatic dependencies compute by adding
# unnecessary deps like /sbin/runscripts
# some other things were removed with the patch
rm -r %{buildroot}%{_datadir}/%{name}/ext/{debian,osx,solaris,suse,windows,systemd,redhat}
rm %{buildroot}%{_datadir}/%{name}/ext/{build_defaults.yaml,project_data.yaml}

%files
%attr(-, puppet, puppet) %{_localstatedir}/log/%{name}
%attr(-, root, root) %{_datadir}/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %{nm_dispatcher_dir}
%dir %{nm_dispatcher_dir}/dispatcher.d
%{nm_dispatcher_dir}/dispatcher.d/98-puppet

# Vendor modules
%doc %{_datadir}/%{name}/vendor_modules/*/*.md
%doc %{_datadir}/%{name}/vendor_modules/*/readmes
%license %{_datadir}/%{name}/vendor_modules/*/LICENSE
# Strip development files
%exclude %{_datadir}/%{name}/vendor_modules/*/.{github,puppet-lint.rc,sync.yml}
%exclude %{_datadir}/%{name}/vendor_modules/*/{CODEOWNERS,Gemfile,appveyor.yml,spec}

%doc README.md examples
%license LICENSE
%{_datadir}/ruby/vendor_ruby/hiera
%{_datadir}/ruby/vendor_ruby/hiera_puppet.rb
%{_datadir}/ruby/vendor_ruby/puppet
%{_datadir}/ruby/vendor_ruby/puppet_pal.rb
%{_datadir}/ruby/vendor_ruby/puppet.rb
%{_datadir}/ruby/vendor_ruby/puppet_x.rb
%dir %{_sharedstatedir}/%{name}
%dir %{_sharedstatedir}/%{name}/public
%{_bindir}/puppet
%{_bindir}/start-puppet-agent
%{_mandir}/man5/puppet.conf.5*
%{_mandir}/man8/puppet-plugin.8*
%{_mandir}/man8/puppet-report.8*
%{_mandir}/man8/puppet-resource.8*
%{_mandir}/man8/puppet-script.8*
%{_mandir}/man8/puppet-ssl.8*
%{_mandir}/man8/puppet-agent.8*
%{_mandir}/man8/puppet.8*
%{_mandir}/man8/puppet-apply.8*
%{_mandir}/man8/puppet-catalog.8*
%{_mandir}/man8/puppet-config.8*
%{_mandir}/man8/puppet-describe.8*
%{_mandir}/man8/puppet-device.8*
%{_mandir}/man8/puppet-doc.8*
%{_mandir}/man8/puppet-epp.8*
%{_mandir}/man8/puppet-facts.8*
%{_mandir}/man8/puppet-filebucket.8*
%{_mandir}/man8/puppet-generate.8*
%{_mandir}/man8/puppet-help.8*
%{_mandir}/man8/puppet-lookup.8*
%{_mandir}/man8/puppet-module.8*
%{_mandir}/man8/puppet-node.8*
%{_mandir}/man8/puppet-parser.8*

%config(noreplace) %attr(-, root, root) %dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(-, root, root) %dir %{_sysconfdir}/%{name}/code
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/%{name}/puppet.conf
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}

%ghost %attr(755, puppet, puppet) %{_rundir}/%{name}
%{_sysusersdir}/puppet.conf

%post
%systemd_post %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
%autochangelog
