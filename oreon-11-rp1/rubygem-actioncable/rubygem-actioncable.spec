%global source0_hash d373bb17e6544be880fbfd58ca77a0114ebaa2c8396ac394873dadaf0aafc9ba

# Generated from actioncable-5.0.0.rc2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actioncable

# TODO: Re-enable recompilation if possible. Currently, we don't have rollup.js
# in Fedora and therefore it requires network access. Still good for checking
# the results
%bcond_with js_recompilation

Name: rubygem-%{gem_name}
Version: 8.0.3
Release: 2%{?dist}
Summary: WebSocket framework for Rails
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone https://github.com/rails/rails.git && cd rails/actioncable
# git archive -v -o actioncable-8.0.3-tests.tar.gz v8.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz
# Source code of pregenerated JS files.
# git clone https://github.com/rails/rails.git && cd rails/actioncable
# git archive -v -o actioncable-8.0.3-js.tar.gz v8.0.3 app/javascript package.json rollup.config.js
Source2: %{gem_name}-%{version}%{?prerelease}-js.tar.gz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(puma)
BuildRequires: rubygem(websocket-driver)
BuildRequires: rubygem(zeitwerk)
BuildRequires: %{_bindir}/redis-server
BuildRequires: rubygem(redis)
%{?with_js_recompilation:BuildRequires: %{_bindir}/npm}
BuildArch: noarch

%description
Structure many real-time application concerns into channels over a single
WebSocket connection.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%build
%if %{with js_recompilation}
# Recompile the embedded JS files from sources.
#
# This is practice suggested by packaging guidelines:
# https://fedoraproject.org/wiki/Packaging:Guidelines#Use_of_pregenerated_code

find app/assets/ -type f -exec sha512sum {} \;

rm -rf app/assets

ln -s %{builddir}/app/javascript ./app/javascript
ln -s %{builddir}/package.json .
cp -a %{builddir}/rollup.config.js .

# TODO: This requires network access. Use Fedora rollup.js if it becomes
# available eventually
npm install
npx rollup --config rollup.config.js

# For comparison with the orginal checksum above.
find app/assets/ -type f -exec sha512sum {} \;
%endif

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
touch ../tools/strict_warnings.rb

# We don't have websocket-client-simple in Fedora yet.
mv test/client_test.rb{,.disable}

# TODO: Needs AR together with PostgreSQL.
mv test/subscription_adapter/postgresql_test.rb{,.disable}

# test/javascript_package_test.rb requires rollup.js, which we don't have.
# OTOH, if we had it, we would recomplie the sources and the test would have
# less value.
mv test/javascript_package_test.rb{,.disable}

# Start a testing Redis server instance
REDIS_DIR=$(mktemp -d)
redis-server --dir $REDIS_DIR --pidfile $REDIS_DIR/redis.pid --daemonize yes

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'

# Shutdown Redis.
kill -INT $(cat $REDIS_DIR/redis.pid)

)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
