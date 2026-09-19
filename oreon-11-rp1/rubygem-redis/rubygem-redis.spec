%global source0_hash 336b975a56b166c6af4d4a1026c71dbed429ba5dc949aac373ef2fded07936b4

%global gem_name redis

Name: rubygem-%{gem_name}
Version: 5.2.0
Release: 4%{?dist}
Summary: A Ruby client library for Redis
License: MIT
URL: https://github.com/redis/redis-rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/redis/redis-rb.git && cd redis-rb
# git archive -v -o redis-rb-5.2.0-tests.txz v5.2.0 makefile test/
Source1: %{gem_name}-rb-%{version}-tests.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(redis-client)
BuildRequires: %{_bindir}/make
BuildRequires: %{_bindir}/redis-server
BuildArch: noarch

%description
A Ruby client that tries to match Redis' API one-to-one, while still
providing an idiomatic interface.

%package doc
Summary: Documentation for %{name}
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

cp -a %{_builddir}/{makefile,test} .

# We are using packaged Redis, so provide just dummy Redis build script.
mkdir bin
echo '#!/usr/bin/sh' > bin/build
chmod a+x bin/build

# The following steps correspond to GH workflow:
# https://github.com/redis/redis-rb/blob/ce2c258297efc2991e509d57e593e76285d58b0b/.github/workflows/test.yaml#L60-L65
# https://github.com/redis/redis-rb/blob/ce2c258297efc2991e509d57e593e76285d58b0b/.github/workflows/test.yaml#L136-L141
# TODO: There is no hiredis-client in Fedora yet, skipt the `hiredis` for now.
# for driver in ruby hiredis ; do
for driver in ruby ; do
  (
    export DRIVER=${driver}
    make BINARY=$(which redis-server) start
    ruby -Itest -e 'Dir.glob "./test/redis/**/*_test.rb", &method(:require)'
    ruby -Itest -e 'Dir.glob "./test/distributed/**/*_test.rb", &method(:require)'
    make stop
    # Give some time for Redis shutdown.
    sleep 1
  )
done

make BINARY=$(which redis-server) REDIS_CLIENT=$(which redis-cli) BUILD_DIR='${TMP}' start_sentinel wait_for_sentinel
ruby -Itest -e 'Dir.glob "./test/sentinel/**/*_test.rb", &method(:require)'
make stop_all
# Give some time for Redis shutdown.
sleep 1
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
