%global source0_hash a6d87c660a52912103acdcb70297b51ba47fc81eabdca382cc1d7b5bf5ab0342

%global vagrant_plugin_name vagrant-libvirt

%global vagrant_spec_commit 259c55e204674f2b006700c6d351d04250d13b04

Name: %{vagrant_plugin_name}
Version: 0.11.2
Release: 9%{?dist}
Summary: libvirt provider for Vagrant
License: MIT
URL: https://github.com/vagrant-libvirt/vagrant-libvirt
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
# The library has no official release yet. But since it is just test
# dependency, it should be fine to include the source right here.
# wget https://github.com/mitchellh/vagrant-spec/archive/03d88fe2467716b072951c2b55d78223130851a6/vagrant-spec-03d88fe2467716b072951c2b55d78223130851a6.tar.gz
Source1: https://github.com/mitchellh/vagrant-spec/archive/%{vagrant_spec_commit}/vagrant-spec-%{vagrant_spec_commit}.tar.gz

# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1709
# ruby3.2 fix wrt File.exits? removal and URI.split host result change
# A bit modified: spec/support/libvirt_acceptance_context.rb does not exist
# with 0.7.0 yet
Patch0: vagrant-libvirt-pr1709-ruby32-File_exists-URL-parse.patch
# Allow a mock object to receive synced_folders in config validation spec.
# We do not care about synced folder check when testing MAC configuration.
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1721
Patch1: vagrant-libvirt-0.11.2-Allow-a-mock-object-to-receive-synced_folders.patch
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1837
# related to https://github.com/ruby/rexml/pull/167
Patch2: vagrant-libvirt-pr1837-testsuite-support-rexml-332.patch
# Get rid of a warning generated due to usage of option
# no longer supported by fog-libvirt
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1835
Patch3: vagrant-libvirt-0.12.2-Remove-config-unsupported-by-fog-libvirt.patch
# Fix compatibility with REXML 3.4.2+
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1861
Patch4: vagrant-libvirt-0.12.2-Fix-REXML-3-4-2-compatibility.patch
# Replace CGI, removed from Ruby 4.0 bundled gems with URI.
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1866
Patch5: vagrant-libvirt-0.12.2-Replace-CGI.parse-with-URI-equivalent.patch

# Enable QEMU Session by default
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/969
Patch100: vagrant-libvirt-0.11.2-enable-qemu-session-by-default.patch

Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(diffy)
Requires: rubygem(fog-libvirt) >= 0.6.0
Requires: rubygem(nokogiri) >= 1.6
Requires: rubygem(rexml)
Requires: rubygem(xml-simple)
# Vagrant changed packaging scriptlets in version 1.9.1.
Requires: vagrant >= 1.9.1
# Required by "vagrant package" command (rhbz#1292217).
Recommends: %{_bindir}/virt-sysprep
BuildRequires: vagrant >= 1.9.1
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(diffy)
BuildRequires: rubygem(fog-libvirt)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(rexml)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(xml-simple)
BuildRequires: rubygems-devel
BuildRequires: %{_bindir}/ps
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
libvirt provider for Vagrant.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{vagrant_plugin_name}-%{version} -b 1

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 100 -p1

%build
gem build ../%{vagrant_plugin_name}-%{version}.gemspec
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

%check
# Edit gemspec of vagrant-spec
pushd ../vagrant-spec-%{vagrant_spec_commit}
# Remove the git reference, which is useless in our case.
sed -i '/git / s/^/#/' vagrant-spec.gemspec

# Relax the dependencies, since Fedora ships with newer versions.
sed -i '/thor/ s/~>/>=/' vagrant-spec.gemspec
sed -i '/rspec/ s/~>/>=/' vagrant-spec.gemspec
popd

# Use actual gemspec for tests
cp ../%{vagrant_plugin_name}-%{version}.gemspec .%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec

pushd .%{vagrant_plugin_instdir}
# Create dummy Gemfile and load dependencies via gemspec file
cat > Gemfile <<EOG
gem 'vagrant'
gem 'base64'
gem 'logger'
gem 'ostruct'
gem 'rdoc'
gem 'rexml'
gem 'vagrant-spec', :path => '%{_builddir}/vagrant-spec-%{vagrant_spec_commit}'
gemspec
EOG

# Unless rsync binary is present, vagrant-libvirt
# decides to use other methods of folder sync in tests,
# breaking set expectations for the test environment.
# https://github.com/vagrant-libvirt/vagrant-libvirt/issues/1415#issuecomment-985272836
# Luckily, it just needs `rsync` in $PATH for tests to pass.
tmpdir=$(mktemp -d)
touch "${tmpdir}/rsync"
chmod +x "${tmpdir}/rsync"

# Suppress deprecation warnings
GEM_PATH=%{vagrant_plugin_dir}:`ruby -e "print Gem.path.join(':')"` \
PATH="$PATH:${tmpdir}" \
bundle exec rspec spec

popd

%files
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.*
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/spec

%changelog
%autochangelog
