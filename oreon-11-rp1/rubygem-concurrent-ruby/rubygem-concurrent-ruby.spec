%global source0_hash dddcb536f0088bf47b6cdb475a64ec5105b0f4df060eeac8f4d737dac8980066

# Generated from concurrent-ruby-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name concurrent-ruby

Name: rubygem-%{gem_name}
Version: 1.3.5
Release: 3%{?dist}
Summary: Modern concurrency tools for Ruby
License: MIT
URL: http://www.concurrent-ruby.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ruby-concurrency/concurrent-ruby.git && cd concurrent-ruby
# git archive -v -o concurrent-ruby-1.3.5-specs.tar.gz v1.3.5 spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(timecop)
BuildArch: noarch

%description
Modern concurrency tools including agents, futures, promises, thread pools,
actors, supervisors, and more.

Inspired by Erlang, Clojure, Go, JavaScript, actors, and classic concurrency
patterns.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

# Remove bundled .jar
%gemspec_remove_file 'lib/concurrent-ruby/concurrent/concurrent_ruby.jar'

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
( cd .%{gem_instdir}
ln -s %{builddir}/spec spec

# We don't have the C extension and the condition is broken with 1.3.5
# https://github.com/ruby-concurrency/concurrent-ruby/issues/1080
sed -i 's/allow_c_extensions/c_extensions_loaded/' \
  spec/concurrent/atomic/atomic_{fixnum,reference,boolean}_spec.rb

# Exclude the -edge test cases.
#
# Require path must be exported due to
# spec/concurrent/executor/executor_service_shared.rb spawning new Ruby instance
RUBYOPT=-Ilib/concurrent-ruby rspec -rspec_helper \
  -fd \
  --exclude-pattern 'spec/concurrent/{actor_spec.rb,channel_spec.rb,lazy_register_spec.rb,channel/**/*,edge/**/*,processing_actor_spec.rb,promises_spec.rb,throttle_spec.rb,cancellation_spec.rb,executor/wrapping_executor_spec.rb}' \
  spec

)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
# Containst just some Java sources. Very likely included by mistake.
%exclude %{gem_instdir}/ext
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
%autochangelog
