%global source0_hash 318b920ccffdc68cc32f82b7b98009332ddfe2d9e278472b1031a45fce806b0d

%global gem_name activesupport

#%%global prerelease 

Name: rubygem-%{gem_name}
Epoch: 1
Version: 8.0.3
Release: 5%{?dist}
Summary: A support libraries and Ruby core extensions extracted from the Rails framework
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone http://github.com/rails/rails.git && cd rails/activesupport
# git archive -v -o activesupport-8.0.3-tests.tar.gz v8.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz
# This is needed due to `force_skip` alias.
# https://github.com/rails/rails/blob/main/tools/test_common.rb
Source2: https://raw.githubusercontent.com/rails/rails/e25d738430bdc6bdd04cd28be705484ea953e74e/tools/test_common.rb
# Fix XmlMiniTest::ParsingTest#test_decimal test failure with BigDecimal 3.2.3+
# https://github.com/rails/rails/pull/55840
Patch1: rubygem-activesupport-8.0.3-Always-pass-default-precision-to-BigDecimal-when-parsing.patch
# Support minitest 6
# https://github.com/rails/rails/pull/56202/
Patch2: rubygem-activesupport-pr56202-minitest6.patch
# We don't always install railties with activesupport, so rescue this
Patch3: rubygem-activesupport-pr56202-minitest6-rescue-loaderror.patch

# Ruby package has just soft dependency on rubygem(json), while
# ActiveSupport always requires it.
Requires: rubygem(json)

# Runtime dependency, lot of build failures in other packages.
# https://fedoraproject.org/wiki/Changes/AllowRemovalOfTzdata
Requires: tzdata

# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(connection_pool)
BuildRequires: rubygem(dalli)
BuildRequires: rubygem(drb)
BuildRequires: rubygem(i18n) >= 0.7
BuildRequires: rubygem(listen)
BuildRequires: rubygem(minitest) >= 5.0.0
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(msgpack)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(redis)
BuildRequires: rubygem(rexml)
BuildRequires: rubygem(tzinfo) >= 2.0
BuildRequires: memcached
%ifnarch %{ix86}
BuildRequires: %{_bindir}/valkey-server
%endif
BuildRequires: tzdata
BuildArch: noarch

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

%check
# Move the tests into place
cp -a test .%{gem_instdir}

cd .%{gem_instdir}

mkdir ../tools
ln -s %{SOURCE2} ../tools/
touch ../tools/strict_warnings.rb

sed -i '/require .bundler./ s/^/#/' test/abstract_unit.rb

# backported from:
# https://github.com/rails/rails/commit/632b2c5128581731c2451459081176a43f474f74
# benchmark 0.5.0 in ruby4_0 defines Benchmark.ms{}, so the following
# test is no longer needed
sed -i test/core_ext/benchmark_test.rb -e '\@test_is_deprecated@s@$@ ; skip ""@'

# Start a testing Valkey (Redis) server instance
%ifnarch %{ix86}
VALKEY_DIR=$(mktemp -d)
valkey-server --dir $VALKEY_DIR --pidfile $VALKEY_DIR/valkey.pid --daemonize yes
%endif

# Start Memcached server
memcached &
mPID=$!
sleep 1

ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)' -- -v

# Shutdown Memcached
kill -15 $mPID

# Shutdown Valkey.
%ifnarch %{ix86}
kill -INT $(cat $VALKEY_DIR/valkey.pid)
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
