%global source1_hash f0ad826baece0e958ddcc163443a186a4821f8bae9ad231d050b905b811069a1
%global source0_hash 336b975a56b166c6af4d4a1026c71dbed429ba5dc949aac373ef2fded07936b4
%global gem_name redis
Name: rubygem-%{gem_name}
Version: 5.2.0
Release:        4%{?dist}
Summary:        A Ruby client library for Redis
License: MIT
URL: https://github.com/redis/redis-rb
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/redis/redis-rb/archive/refs/tags/v5.2.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/redis-server
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(redis-client)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

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
cp -a %{_builddir}/{makefile,test} .
mkdir bin
echo '#!/usr/bin/sh' > bin/build
chmod a+x bin/build
for driver in ruby ; do
  (
    export DRIVER=${driver}
    make BINARY=$(which redis-server) start
    ruby -Itest -e 'Dir.glob "./test/redis/**/*_test.rb", &method(:require)'
    ruby -Itest -e 'Dir.glob "./test/distributed/**/*_test.rb", &method(:require)'
    make stop
    sleep 1
  )
done
make BINARY=$(which redis-server) REDIS_CLIENT=$(which redis-cli) BUILD_DIR='${TMP}' start_sentinel wait_for_sentinel
ruby -Itest -e 'Dir.glob "./test/sentinel/**/*_test.rb", &method(:require)'
make stop_all
sleep 1
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-redis-doc -f %{oreon_filedir}/rubygem-redis-doc.list

%changelog

%autochangelog
