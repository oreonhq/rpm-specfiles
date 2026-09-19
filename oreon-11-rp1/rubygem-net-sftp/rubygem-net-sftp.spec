%global source0_hash e2e3cbae1eefe4aa4ad9cef27da979e99371b1470d37d072019f4c575f56c82b

%global gem_name net-sftp

Name: rubygem-%{gem_name}
Version: 4.0.0
Release: 8%{?dist}
Summary: A pure Ruby implementation of the SFTP client protocol
License: MIT
URL: https://github.com/net-ssh/net-sftp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/net-ssh/net-sftp.git && cd net-sftp
# git archive -v --format=tar.gz -o net-sftp-4.0.0-test.tar.gz v4.0.0 test/
Source1: %{gem_name}-%{version}-test.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(base64)
BuildRequires: rubygem(minitest) > 5
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(net-ssh)
BuildArch: noarch

%description
A pure Ruby implementation of the SFTP client protocol.

%package doc
Summary: Documentation for %{name}
# LICENSE.txt declares MIT
# setup.rb: LGPL-2.1-only
License: MIT AND LGPL-2.1-only
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

ruby -Ilib:test test/test_all.rb
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.txt
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/Manifest
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/net-sftp-public_cert.pem
%{gem_instdir}/net-sftp.gemspec
%{gem_instdir}/setup.rb

%changelog
%autochangelog
