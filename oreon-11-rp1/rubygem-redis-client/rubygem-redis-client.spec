%global source1_hash 41bfd1c2167f801498bfd0a3d33e4be301e187b5b2a446c5f8c350849723bdcc
%global source0_hash 31fee4b7cf04109b227327fabeaaf1fc5b652cf48a186a03bc607e40767bacc0
%global gem_name redis-client
%bcond_without regenerate_certs
Name: rubygem-%{gem_name}
Version: 0.22.2
Release:        1%{?dist}
Summary:        Simple low-level client for Redis 6+
License: MIT
URL: https://github.com/redis-rb/redis-client
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/redis-rb/redis-client/archive/refs/tags/v0.22.2.tar.gz
Patch0:  redis-client-GH95c9666-Ractor-ruby4_0.patch
Patch1:  redis-client-GHe5869bf-Ractor-warning-change.patch
Patch2:  redis-client-0.22.2-minitest6.patch
%{?with_regenerate_certs:BuildRequires: %{_bindir}/openssl}
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/openssl
BuildRequires:  /usr/bin/redis-server
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(benchmark)
BuildRequires:  rubygem(connection_pool)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
(
cd %{_builddir}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
cp -a %{_builddir}/test .
%{?with_regenerate_certs: test/fixtures/generate-certs.sh}
sed -i '/build_redis/ s/^/#/' test/test_helper.rb
sed -i '/build_redis/ s/^/#/' test/sentinel/test_helper.rb
sed -i '/def redis_server_bin/,/end/ s/redis_builder.bin_path/"redis-server"/' test/support/servers.rb
sed -i '/^\s*REDIS_SOCKET_FILE/ s/ServerManager::ROOT\.join("tmp\/redis\.sock")/"\/tmp\/redis\.sock"/' test/support/servers.rb
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
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-redis-client-doc -f %{oreon_filedir}/rubygem-redis-client-doc.list

%changelog

%autochangelog
