%global source0_hash 31fee4b7cf04109b227327fabeaaf1fc5b652cf48a186a03bc607e40767bacc0

# Generated from redis-client-0.12.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis-client

%bcond_without regenerate_certs

Name: rubygem-%{gem_name}
Version: 0.22.2
Release: 7%{?dist}
Summary: Simple low-level client for Redis 6+
License: MIT
URL: https://github.com/redis-rb/redis-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/redis-rb/redis-client.git && cd redis-client
# git archive -v -o redis-client-0.22.2-tests.txz v0.22.2 test/
Source1: %{gem_name}-%{version}-tests.txz
# https://github.com/redis-rb/redis-client/commit/95c96666868fb60286b473abbef1daa18d827b52
# ruby4_0 removes Ractor#take
Patch0:  redis-client-GH95c9666-Ractor-ruby4_0.patch
# https://github.com/redis-rb/redis-client/issues/270
# https://github.com/redis-rb/redis-client/commit/e5869bf151c2b922fbc52e87edba8f7d1efe8b93
# Adjust to Ractor warning change
Patch1:  redis-client-GHe5869bf-Ractor-warning-change.patch
# Fix compatibility with minitest 6
Patch2:  redis-client-0.22.2-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygem(benchmark)
BuildRequires: rubygem(connection_pool)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
%{?with_regenerate_certs:BuildRequires: %{_bindir}/openssl}
BuildRequires: %{_bindir}/redis-server
BuildArch: noarch

%description
Simple low-level client for Redis 6+.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
)

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
cp -a %{_builddir}/test .

# Make sure we are using fresh certificates.
%{?with_regenerate_certs: test/fixtures/generate-certs.sh}

# Do not download Redis, use the system one.
# https://github.com/redis-rb/redis-client/issues/88
sed -i '/build_redis/ s/^/#/' test/test_helper.rb
sed -i '/build_redis/ s/^/#/' test/sentinel/test_helper.rb
sed -i '/def redis_server_bin/,/end/ s/redis_builder.bin_path/"redis-server"/' test/support/servers.rb

# Reduce the unix socket nesting, because RPM 4.20+ adds one additional layer
# of nesting and that results in test failures such as:
# `ArgumentError: too long unix socket path (130bytes given but 108bytes max)`
sed -i '/^\s*REDIS_SOCKET_FILE/ s/ServerManager::ROOT\.join("tmp\/redis\.sock")/"\/tmp\/redis\.sock"/' test/support/servers.rb

# We don't have Toxiproxy in Fedora :/
# https://github.com/redis-rb/redis-client/issues/89
sed -i '/toxiproxy/ s/^/#/' test/env.rb
sed -i '/TOXIPROXY,/ s/^/#/' test/support/servers.rb
sed -i '/REDIS.*79/ s/79/80/' test/support/servers.rb
sed -i '/Toxiproxy\[/i\
      skip' test/redis_client/connection_test.rb

ruby -Ilib:test -e '
  Dir["./test/**/*_test.rb"]
    .reject{|i| i.start_with?("./test/sentinel/")}
    .each &method(:require)
'

# TODO: Add sentinel and hiredis tests.
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/redis-client.gemspec

%changelog
%autochangelog
