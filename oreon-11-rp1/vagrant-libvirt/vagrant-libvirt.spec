%global source1_hash a6d87c660a52912103acdcb70297b51ba47fc81eabdca382cc1d7b5bf5ab0342
%global source0_hash 34c8918eb550a36522f67389c290e6349524fbde60b13f39a7014c222c376f04
%global vagrant_plugin_name vagrant-libvirt
%global vagrant_spec_commit 259c55e204674f2b006700c6d351d04250d13b04
Name: %{vagrant_plugin_name}
Version: 0.12.2
Release:        1%{?dist}
Summary:        libvirt provider for Vagrant
License: MIT
URL: https://github.com/vagrant-libvirt/vagrant-libvirt
Source0:        https://rubygems.org/gems/%{name}-%{version}.gem
Source1: https://github.com/mitchellh/vagrant-spec/archive/%{vagrant_spec_commit}/vagrant-spec-%{vagrant_spec_commit}.tar.gz
Patch0: vagrant-libvirt-pr1709-ruby32-File_exists-URL-parse.patch
Patch1: vagrant-libvirt-0.11.2-Allow-a-mock-object-to-receive-synced_folders.patch
Patch2: vagrant-libvirt-pr1837-testsuite-support-rexml-332.patch
Patch3: vagrant-libvirt-0.12.2-Remove-config-unsupported-by-fog-libvirt.patch
Patch4: vagrant-libvirt-0.12.2-Fix-REXML-3-4-2-compatibility.patch
Patch5: vagrant-libvirt-0.12.2-Replace-CGI.parse-with-URI-equivalent.patch
Patch100: vagrant-libvirt-0.11.2-enable-qemu-session-by-default.patch
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(diffy)
Requires: rubygem(fog-libvirt) >= 0.6.0
Requires: rubygem(nokogiri) >= 1.6
Requires: rubygem(rexml)
Requires: rubygem(xml-simple)
Requires: vagrant >= 1.9.1
Recommends: %{_bindir}/virt-sysprep
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}
# oreon:deps
BuildRequires:  /usr/bin/ps
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(diffy)
BuildRequires:  rubygem(fog-libvirt)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rdoc)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(thor)
BuildRequires:  rubygem(xml-simple)
BuildRequires:  rubygems-devel
BuildRequires:  vagrant
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd ../vagrant-spec-%{vagrant_spec_commit}
sed -i '/git / s/^/#/' vagrant-spec.gemspec
sed -i '/thor/ s/~>/>=/' vagrant-spec.gemspec
sed -i '/rspec/ s/~>/>=/' vagrant-spec.gemspec
popd
cp ../%{vagrant_plugin_name}-%{version}.gemspec .%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec
pushd .%{vagrant_plugin_instdir}
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
tmpdir=$(mktemp -d)
touch "${tmpdir}/rsync"
chmod +x "${tmpdir}/rsync"
GEM_PATH=%{vagrant_plugin_dir}:`ruby -e "print Gem.path.join(':')"` \
PATH="$PATH:${tmpdir}" \
bundle exec rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n vagrant-libvirt-doc -f %{oreon_filedir}/vagrant-libvirt-doc.list

%changelog

%autochangelog
