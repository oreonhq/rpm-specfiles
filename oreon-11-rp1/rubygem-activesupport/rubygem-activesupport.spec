%global source2_hash 07aaf0a5e9424d6b2bbd9b121da56a2f24d45e86c0b6a09f5aed00b7ac4f12c0
%global source1_hash 0419bf47f7357e6d3da85ff4ad797a3609dcf36ff44be496162ffbc901ff4232
%global source0_hash a711ce5e30660b23232f26a38699469f8d859d47aa1f722e183fda6d7cc17823
%global gem_name activesupport
Name: rubygem-%{gem_name}
Epoch: 1
Version: 8.0.3
Release:        1%{?dist}
Summary:        A support libraries and Ruby core extensions extracted from the Rails framework
License: MIT
URL: https://rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/rails/archive/refs/tags/v8.0.3.tar.gz
Source2: https://raw.githubusercontent.com/rails/rails/e25d738430bdc6bdd04cd28be705484ea953e74e/tools/test_common.rb
Patch1: rubygem-activesupport-8.0.3-Always-pass-default-precision-to-BigDecimal-when-parsing.patch
Patch2: rubygem-activesupport-pr56202-minitest6.patch
Patch3: rubygem-activesupport-pr56202-minitest6-rescue-loaderror.patch
Requires: rubygem(json)
Requires: tzdata
%ifnarch %{ix86}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  //bin/valkey-server
BuildRequires:  memcached
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(builder)
BuildRequires:  rubygem(concurrent-ruby)
BuildRequires:  rubygem(connection_pool)
BuildRequires:  rubygem(dalli)
BuildRequires:  rubygem(drb)
BuildRequires:  rubygem(i18n)
BuildRequires:  rubygem(listen)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(msgpack)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(redis)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(tzinfo)
BuildRequires:  rubygems-devel
BuildRequires:  tzdata
# /oreon:deps
%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization,
time zones, and testing.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -a 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 1 -p2
%patch 2 -p2
%patch 3 -p1

# lib/active_support/testing/method_call_assertions.rb
# always needs minitest/mock
%gemspec_add_dep -g minitest-mock

%build

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp -a test .%{gem_instdir}
cd .%{gem_instdir}
mkdir ../tools
ln -s %{SOURCE2} ../tools/
touch ../tools/strict_warnings.rb
sed -i '/require .bundler./ s/^/#/' test/abstract_unit.rb
sed -i test/core_ext/benchmark_test.rb -e '\@test_is_deprecated@s@$@ ; skip ""@'
%ifnarch %{ix86}
VALKEY_DIR=$(mktemp -d)
valkey-server --dir $VALKEY_DIR --pidfile $VALKEY_DIR/valkey.pid --daemonize yes
%endif
memcached &
mPID=$!
sleep 1
ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)' -- -v
kill -15 $mPID
%ifnarch %{ix86}
kill -INT $(cat $VALKEY_DIR/valkey.pid)
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-activesupport-doc -f %{oreon_filedir}/rubygem-activesupport-doc.list

%changelog

%autochangelog
