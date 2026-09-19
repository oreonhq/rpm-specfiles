%global source0_hash 27b564bd27482fddcc4da2ecb4c7fad824371b4a2cb58d0686494b50b4fd07a3

%global gem_name net-scp

Summary: A pure Ruby implementation of the SCP client protocol
Name: rubygem-%{gem_name}
Version: 4.0.0
Release: 10%{?dist}
License: MIT
URL: https://github.com/net-ssh/net-scp
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are not packaged with the gem. You may get them like so:
# git clone --no-checkout https://github.com/net-ssh/net-scp
# git -C net-scp archive -v --format=tar.gz -o net-scp-4.0.0-test.tar.gz v4.0.0 test
Source1: %{gem_name}-%{version}-test.tar.gz
# This is required for Mocha 2+ compatibility.
# https://github.com/net-ssh/net-scp/commit/5871b93867151a1f7e6bb41bce92bdc5ae083cab
Patch0: rubygem-net-scp-4.0.0-Fix-Mocha-deprecation-warning.patch
# Fix Mocha > 2.1.0 compatibility
# https://github.com/net-ssh/net-scp/pull/74/commits/c3fbf50bd9506892c1869dddec0a643213358b73
Patch1: rubygem-mocha-2.6.1-Fix-rake-test-fails-with-mocha-2-1-0-72.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(base64)
BuildRequires: rubygem(net-ssh)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
A pure Ruby implementation of the SCP client protocol

%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

pushd %{_builddir}
%patch 0 -p1
%patch 1 -p1
popd

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

ruby -Ilib:test test/test_all.rb
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/setup.rb

%files doc
%{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/net-scp.gemspec
%{gem_instdir}/net-scp-public_cert.pem
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES.txt
%doc %{gem_docdir}

%changelog
%autochangelog
