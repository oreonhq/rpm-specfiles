%global source0_hash 9b9d32daf0e231f6e7620e2b2a6dc3cb42c7c5111c9b6976b7e2b241a9551171

%global bashcompletion_dir %(pkg-config --variable=completionsdir bash-completion 2> /dev/null || :)

%global vagrant_spec_commit a88825f4cb254b703d0f9235667223f02ad5c600

%bcond_without help2man
%bcond_without ed25519

Name: vagrant
Version: 2.3.4
Release: 10%{?dist}
Summary: Build and distribute virtualized development environments
License: MIT
URL: http://vagrantup.com
Source0: https://github.com/hashicorp/%{name}/archive/refs/tags/v%{version}.tar.gz
# Upstream binstub with adjusted paths, the offical way how to run vagrant
Source1: binstub
# The library has no official release yet. But since it is just test
# dependency, it should be fine to include the source right here.
# wget https://github.com/hashicorp/vagrant-spec/archive/03d88fe2467716b072951c2b55d78223130851a6/vagrant-spec-03d88fe2467716b072951c2b55d78223130851a6.tar.gz
Source2: https://github.com/hashicorp/%{name}-spec/archive/%{vagrant_spec_commit}/%{name}-spec-%{vagrant_spec_commit}.tar.gz
# Monkey-patching needed for Vagrant to work until the respective patches
# for RubyGems and Bundler are in place
Source4: macros.vagrant

# Do not load runtime dependencies in %%check if vagrant is not loaded
# https://github.com/hashicorp/vagrant/pull/10945
Patch1: vagrant-2.2.9-do-not-load-dependencies.patch
# Remove GRPC dependencies for Fedora. It seems that it will serve
# for communication with upcoming Golang backend, however
# it is only in tech-preview now and grpc is not simple to package.
# Let's remove it for now and revisit in the future.
Patch2: vagrant-2.3.4-remove_grpc.patch
# Ruby 3.2 compatibility for tests.
# Commits are cherry-picked instead of a whole PR as it also edits .github
# files that we do not care about.
# https://github.com/hashicorp/vagrant/pull/13043
Patch3: vagrant-2.3.4-Environment-home-dir-is-also-not-accessible-if-EROFS-error-occurs.patch
Patch4: vagrant-2.3.4-Only-check-for-arguments-matching-test-string.patch
# Disable loading of direc_conversions.rb in other files.
# The file is removed as it requires protobuf components not yet
# packaged in Fedora.
Patch5: vagrant-2.3.4-Disable-loading-of-direct_conversions-file.patch
# Default URL for pulling boxes seems to have changed.
# This fix allows vagrant to pull boxes again.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2337302
Patch6: vagrant-2.3.4-Fix-the-default-vagrant-URL-for-pulling-boxes.patch

# The load directive is supported since RPM 4.12, i.e. F21+. The build process
# fails on older Fedoras.
%{load:%{SOURCE4}}

Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
# Explicitly specify MRI, since Vagrant does not work with JRuby ATM.
Requires: ruby
Requires: rubygem(hashicorp-checkpoint) >= 0.1.5
Requires: rubygem(childprocess) >= 0.5.0
Requires: rubygem(erubi)
Requires: (rubygem(i18n) >= 1.8 with rubygem(i18n) < 2.0)
Requires: rubygem(json)
Requires: (rubygem(listen) >= 3.2 with rubygem(listen) < 4)
Requires: rubygem(log4r) >= 1.1.9
Requires: (rubygem(net-ssh) >= 5.2.0 with rubygem(net-ssh) < 8)
Requires: rubygem(net-scp) >= 1.2.0
Requires: rubygem(net-sftp) >= 2.1
Requires: rubygem(rubyzip) >= 1.1.7
Requires: rubygem(net-ftp)
Requires: rubygem(rexml)
Requires: rubygem(mime-types)
Requires: bsdtar
Requires: curl
Requires: %{_bindir}/ps

Recommends: vagrant(vagrant-libvirt)
Recommends: (podman-docker if podman)

%if %{with ed25519}
Requires: rubygem(ed25519)
Requires: rubygem(bcrypt_pbkdf)
BuildRequires: rubygem(ed25519)
BuildRequires: rubygem(bcrypt_pbkdf)
%else
Recommends: rubygem(ed25519)
Recommends: rubygem(bcrypt_pbkdf)
%endif

BuildRequires: bsdtar
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(listen)
BuildRequires: rubygem(childprocess)
BuildRequires: rubygem(hashicorp-checkpoint)
BuildRequires: rubygem(log4r)
BuildRequires: rubygem(net-ssh)
BuildRequires: rubygem(net-scp)
BuildRequires: rubygem(i18n)
BuildRequires: rubygem(json)
BuildRequires: rubygem(erubi)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-its)
BuildRequires: rubygem(net-sftp)
BuildRequires: rubygem(rubyzip)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(webrick)
BuildRequires: rubygem(fake_ftp)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(net-ftp)
BuildRequires: rubygem(rexml)
BuildRequires: rubygem(mime-types)
BuildRequires: pkgconfig(bash-completion)
%if %{with help2man}
BuildRequires: help2man
%endif
BuildRequires: %{_bindir}/ssh
BuildArch: noarch

# Since Vagrant itself is installed on the same place as its plugins
# the vagrant_plugin macros can be reused in the spec file, but the plugin
# name must be specified.
%global vagrant_plugin_name vagrant

%description
Vagrant is a tool for building and distributing virtualized development
environments.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -b2

# TODO: package vagrant_cloud, as it is not in Fedora yet
%gemspec_remove_dep -s %{name}.gemspec -g vagrant_cloud

# Remove `cloud` command and references to it
%gemspec_remove_file -s %{name}.gemspec Dir.glob('plugins/commands/cloud/**/*.*')
rm -rf ./plugins/commands/cloud/
sed -i '/^\s*I18n\..*$/ s/^/#/g' plugins/commands/login/plugin.rb
sed -i '/^\s*command(:login) do$/,/\s*end$/ s/^/#/g' plugins/commands/login/plugin.rb

# Expand required Ruby compatibility, otherwise RubyGems throws exceptions.
# Relevant rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=2053476#c0
# Relevant RubyGems issue: https://github.com/rubygems/rubygems/issues/4338
sed -i -e '/required_ruby_version/ s/, "< 3.2"//' %{name}.gemspec

# We have older version in Fedora
%gemspec_remove_dep -s %{name}.gemspec -g net-sftp '~> 4.0'
%gemspec_add_dep -s %{name}.gemspec -g net-sftp '>= 2.1.2'
%gemspec_remove_dep -s %{name}.gemspec -g net-scp '~> 4.0'
%gemspec_add_dep -s %{name}.gemspec -g net-scp '>= 1.2.0'

# We have newer version in Fedora
%gemspec_remove_dep -s %{name}.gemspec -g listen
%gemspec_add_dep -s %{name}.gemspec -g listen '>= 3.5.1'
%gemspec_remove_dep -s %{name}.gemspec -g rubyzip '~> 2.0'
%gemspec_add_dep -s %{name}.gemspec -g rubyzip '>= 2.0.0'

# Remove Windows specific dependencies
%gemspec_remove_dep -s %{name}.gemspec -g wdm
%gemspec_remove_dep -s %{name}.gemspec -g winrm
%gemspec_remove_dep -s %{name}.gemspec -g winrm-fs
%gemspec_remove_dep -s %{name}.gemspec -g winrm-elevated

# Remove BSD dependency
%gemspec_remove_dep -s %{name}.gemspec -g rb-kqueue

# Allow older childprocess version
%gemspec_remove_dep -s %{name}.gemspec -g childprocess
%gemspec_add_dep -s %{name}.gemspec -g childprocess '>= 1.0.1'

# Relax net-ssh dependency. We have newer net-ssh in Fedora
%gemspec_remove_dep -s %{name}.gemspec -g net-ssh
%gemspec_add_dep -s %{name}.gemspec -g net-ssh ['>= 5.2.0', '< 8']

# Remove "optional" dependencies
# This seems like prelude for the in-development golang backend.
# Nothing runtime critical.
%gemspec_remove_dep -s %{name}.gemspec -g googleapis-common-protos-types
%gemspec_remove_dep -s %{name}.gemspec -g grpc
%gemspec_remove_dep -s %{name}.gemspec -g rgl
# Load missing dependency Vagrant::Util::MapCommandOptions
# https://github.com/hashicorp/vagrant/pull/11609
sed -i '/^\s*require..vagrant.util.experimental.\s*$/ a\require "vagrant/util/map_command_options"' \
  plugins/kernel_v2/config/vm.rb

%if %{without ed25519}
# Remove optional dependencies
%gemspec_remove_dep -s %{name}.gemspec -g bcrypt_pbkdf

%gemspec_remove_dep -s %{name}.gemspec -g ed25519
# Disable patch for ed25519
sed -i '/^  require .net\/ssh\/authentication\/ed25519.$/,/^  end$/ s/^/#/' \
  lib/vagrant/patches/net-ssh.rb
%else
%gemspec_remove_dep -s %{name}.gemspec -g ed25519
%gemspec_add_dep -s %{name}.gemspec -g ed25519 ['>= 1.2.4', '< 1.4']
%endif

# Let's get rid of protobuf related components
%patch 2 -p16

%gemspec_remove_file -s %{name}.gemspec Dir.glob('lib/vagrant/protobufs/**/*.*')
# This file contains monkey patching and compatibility for Protobuf serialization.
# We do not need that as we skip protobuf related parts completely.
%gemspec_remove_file -s %{name}.gemspec "plugins/commands/serve/util/direct_conversions.rb"
rm -rf plugins/commands/serve/util/direct_conversions.rb
# Patch out related requires in code.
%patch 5 -p1

%patch 3 -p1

%patch 6 -p1

%build
gem build %{name}.gemspec

gem install -V --local \
  --no-user-install \
  --install-dir .%{vagrant_plugin_dir} \
  --bindir .%{vagrant_plugin_dir}/bin \
  --ignore-dependencies --force --no-document --backtrace \
  %{name}-%{version}.gem

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -pa .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

find %{buildroot}%{vagrant_plugin_dir}/bin -type f | xargs chmod a+x

# Provide executable similar to upstream:
# https://github.com/mitchellh/vagrant-installers/blob/master/substrate/modules/vagrant_installer/templates/vagrant.erb
install -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/vagrant
sed -i 's|@vagrant_embedded_dir@|%{vagrant_embedded_dir}|' %{buildroot}%{_bindir}/vagrant

# auto-completion
install -D -m 0644 %{buildroot}%{vagrant_plugin_instdir}/contrib/bash/completion.sh \
  %{buildroot}%{bashcompletion_dir}/%{name}
sed -i '/#!\// d' %{buildroot}%{bashcompletion_dir}/%{name}

install -D -m 0644 %{buildroot}%{vagrant_plugin_instdir}/contrib/zsh/_%{name} \
  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

# Install Vagrant macros
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
cp %{SOURCE4} %{buildroot}%{_rpmconfigdir}/macros.d/
# Expand some basic macros.
sed -i "s/%%{name}/%{name}/" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}
sed -i "/vagrant_embedded_dir/ s/%%{name}/%{name}/" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}
sed -i "/vagrant_embedded_dir/ s/%%{version}/%{version}/" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}

# Create configuration directory.
install -d -m 755 %{buildroot}%{vagrant_plugin_conf_dir}
# Make sure the plugins.json exists and provide the link to
# VAGRANT_INSTALLER_EMBEDDED_DIR so Vagrant can locate the file.
touch %{buildroot}%{vagrant_plugin_conf}
ln -s -t %{buildroot}%{vagrant_embedded_dir}/ %{vagrant_plugin_conf}

%if %{with help2man}
# Turn `vagrant --help` into man page.
export GEM_PATH="%{gem_dir}:%{buildroot}/usr/share/vagrant/gems"
# Needed to display help page without a warning.
export VAGRANT_INSTALLER_ENV=1
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -s1 -o %{buildroot}%{_mandir}/man1/%{name}.1 \
    %{buildroot}/usr/share/%{name}/gems/gems/%{name}-%{version}/bin/%{name} || \
    %{buildroot}/usr/share/%{name}/gems/gems/%{name}-%{version}/bin/%{name}
%endif

%check
# Do not load dependencies from gemspec
cat %{PATCH1} | patch -p1
# Ruby 3.2 compatibility fix
cat %{PATCH4} | patch -p1

sed -i '/^\s*context "when vagrant specification is not found" do$/,/^    end$/ s/^/#/' \
  test/unit/vagrant/bundler_test.rb
sed -i '/^\s*it "should init the bundler instance with plugins" do$/,/^    end$/ s/^/#/' \
  test/unit/vagrant/plugin/manager_test.rb

# Adjust the vagrant-spec directory name.
rm -rf ../vagrant-spec
mv ../vagrant-spec{-%{vagrant_spec_commit},}

# Remove the git reference, which is useless in our case.
sed -i '/git/ s/^/#/' ../vagrant-spec/vagrant-spec.gemspec

# Relax the dependencies, since Fedora ships with newer versions.
sed -i '/thor/ s/~>/>=/' ../vagrant-spec/vagrant-spec.gemspec
sed -i '/rspec/ s/~>/>=/' ./vagrant.gemspec
sed -i '/rspec/ s/~>/>=/' ../vagrant-spec/vagrant-spec.gemspec
sed -i '/childprocess/ s/~>/>=/' ../vagrant-spec/vagrant-spec.gemspec

#Insert new test dependencies
sed -i '25 i\  spec.add_dependency "webmock"' ../vagrant-spec/vagrant-spec.gemspec
sed -i '26 i\  spec.add_dependency "fake_ftp"' ../vagrant-spec/vagrant-spec.gemspec

# TODO: winrm is not in Fedora yet.
rm -rf test/unit/plugins/communicators/winrm
sed -i '/it "eager loads WinRM" do/,/^      end$/ s/^/#/' test/unit/vagrant/machine_test.rb
sed -i '/it "should return the specified communicator if given" do/,/^    end$/ s/^/#/' test/unit/vagrant/machine_test.rb
sed -i '/^    context "with winrm communicator" do$/,/^    end$/ s/^/#/' \
  test/unit/plugins/provisioners/ansible/provisioner_test.rb

# Disable test that requires bundler
# https://github.com/hashicorp/vagrant/issues/9273
mv test/unit/vagrant/util/env_test.rb{,.disable}

# vagrant_cloud is not in Fedora yet; login command is deprecated
# in favor of vagrant_cloud
rm -r test/unit/plugins/commands/cloud/

# Disable test that requires network
sed -i '/^    it "generates a network name and configuration" do$/,/^    end/ s/^/#/' \
  test/unit/plugins/providers/docker/action/prepare_networks_test.rb

# Remove failing BSD-host tests, as we don't care about those.
rm -rf test/unit/plugins/hosts/bsd

# Export the OS as an environment variable that Vagrant can access, so the
# test suite is executed with same host it will be run (also avoids docker
# installer_test issue).
export VAGRANT_DETECTED_OS="$(uname -s 2>/dev/null)"

# Disable tests concerning protobuf
mv ./test/unit/plugins/commands/serve/service/guest_service_test.rb{,.disabled}
mv ./test/unit/plugins/commands/serve/service/host_service_test.rb{,.disabled}
mv ./test/unit/plugins/commands/serve/util/exception_transformer_test.rb{,.disabled}
mv ./test/unit/plugins/commands/serve/mappers_test.rb{,.disabled}
sed -i -e '/    it "uses a directory within the home directory by default" do/a\
    skip "Requires protobuf"' ./test/unit/vagrant/environment_test.rb

# Put gem load path on top of the load path, so they are loaded earlier then
# their StdLib symlinks.
%{!?buildtime_libdir:%global buildtime_libdir $(ruby -rrbconfig -e 'puts RbConfig::CONFIG["libdir"]')}

RUBYOPT="-I"
for module in \
    openssl \
    psych
do
    for dir in \
        %{gem_dir}/gems/$module-*/lib \
        %{buildtime_libdir}/gems/ruby/$module-*
    do
        RUBYOPT="$RUBYOPT:$dir"
    done
done
export RUBYOPT

# Rake solves the requires issues for tests
rake -f tasks/test.rake test:unit \
  | tee error.log

%if %{with help2man}
# Check `--help` output, using which man page is created
export GEM_PATH="%{gem_dir}:%{buildroot}/usr/share/vagrant/gems"
export VAGRANT_INSTALLER_ENV=1
%{buildroot}/usr/share/%{name}/gems/gems/%{name}-%{version}/bin/%{name} --help 2>/dev/null \
  | grep -q '^Usage: vagrant '
%endif

%post -p %{_bindir}/ruby
begin
  $LOAD_PATH.unshift "%{vagrant_dir}/lib"
  begin
    require "vagrant/plugin/manager"
  rescue LoadError => e
    raise
  end;

  unless File.exist?("%{vagrant_plugin_conf_link}")
    Vagrant::Plugin::StateFile.new(Pathname.new(File.expand_path "%{vagrant_plugin_conf}")).save!
    File.symlink "%{vagrant_plugin_conf}", "%{vagrant_plugin_conf_link}"
  end
rescue => e
  puts "Vagrant plugin.json is not properly initialized: #{e}"
end

%transfiletriggerin -p %{_bindir}/ruby -- %{dirname:%{vagrant_plugin_spec}}/
begin
  $LOAD_PATH.unshift "%{vagrant_dir}/lib"
  begin
    require "vagrant/plugin/manager"
  rescue LoadError => e
    raise
  end

  $stdin.each_line do |gemspec_file|
    next if gemspec_file =~ /\/%{name}-%{version}.gemspec$/

    spec = Gem::Specification.load(gemspec_file.strip)
    Vagrant::Plugin::StateFile.new(Pathname.new(File.expand_path "%{vagrant_plugin_conf_link}")).add_plugin spec.name
  end
rescue => e
  puts "Vagrant plugin register error: #{e}"
end

%transfiletriggerun -p %{_bindir}/ruby -- %{dirname:%{vagrant_plugin_spec}}/
begin
  $LOAD_PATH.unshift "%{vagrant_dir}/lib"
  begin
    require "vagrant/plugin/manager"
  rescue LoadError => e
    raise
  end

  $stdin.each_line do |gemspec_file|
    next if gemspec_file =~ /\/%{name}-%{version}.gemspec$/

    spec = Gem::Specification.load(gemspec_file.strip)
    Vagrant::Plugin::StateFile.new(Pathname.new(File.expand_path "%{vagrant_plugin_conf_link}")).remove_plugin spec.name
  end
rescue => e
  puts "Vagrant plugin un-register error: #{e}"
end

%files
# Explicitly include Vagrant plugins directory strucure to avoid accidentally
# packaged content.
%dir %{vagrant_embedded_dir}
%dir %{vagrant_plugin_dir}
%dir %{vagrant_plugin_dir}/bin
%dir %{vagrant_plugin_dir}/build_info
%dir %{dirname:%{vagrant_plugin_cache}}
%dir %{dirname:%{vagrant_plugin_docdir}}
%dir %{vagrant_plugin_dir}/extensions
%dir %{dirname:%{vagrant_plugin_instdir}}
%dir %{dirname:%{vagrant_plugin_spec}}

%exclude %{vagrant_plugin_instdir}/Makefile
%exclude %{vagrant_plugin_instdir}/Dockerfile
%exclude %{vagrant_plugin_instdir}/flake*
%exclude %{vagrant_plugin_instdir}/go.{mod,sum}
%exclude %{vagrant_plugin_instdir}/gen.go
%exclude %{vagrant_plugin_instdir}/binstubs/vagrant
%exclude %{vagrant_plugin_instdir}/nix/*.nix
%exclude %{vagrant_plugin_instdir}/shell.nix
%exclude %{vagrant_plugin_instdir}/vagrant-config.hcl

%{_bindir}/%{name}
%dir %{vagrant_plugin_instdir}
%license %{vagrant_plugin_instdir}/LICENSE
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_dir}/bin/vagrant
%exclude %{vagrant_plugin_instdir}/.*
%exclude %{vagrant_plugin_instdir}/Vagrantfile
%{vagrant_plugin_instdir}/bin
# TODO: Make more use of contribs.
%{vagrant_plugin_instdir}/contrib
%exclude %{vagrant_plugin_instdir}/contrib/bash
%exclude %{vagrant_plugin_instdir}/contrib/zsh/_%{name}
# This is not the original .gemspec.
%exclude %{vagrant_plugin_instdir}/vagrant.gemspec
%{vagrant_plugin_instdir}/keys
%{vagrant_plugin_instdir}/lib
%{vagrant_plugin_instdir}/plugins
%exclude %{vagrant_plugin_instdir}/scripts
%{vagrant_plugin_instdir}/templates
%{vagrant_plugin_instdir}/version.txt
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}
%dir %{vagrant_plugin_conf_dir}
%ghost %{vagrant_plugin_conf_link}
%ghost %{vagrant_plugin_conf}
# TODO: This is suboptimal and may break, but can't see much better way ...
%dir %{dirname:%{bashcompletion_dir}}
%dir %{bashcompletion_dir}
%{bashcompletion_dir}/%{name}
# By "owning" the site-functions dir, we don't need to Require zsh
%dir %{_datadir}/zsh
%{_datadir}/zsh/site-functions/_%{name}
%{_rpmconfigdir}/macros.d/macros.%{name}
%if %{with help2man}
%{_mandir}/man1/%{name}.1*
%endif

%files doc
%doc %{vagrant_plugin_instdir}/RELEASE.md
%doc %{vagrant_plugin_instdir}/CHANGELOG.md
%{vagrant_plugin_instdir}/Gemfile
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/tasks
%{vagrant_plugin_instdir}/vagrant-spec.config.example.rb

%changelog
%autochangelog
