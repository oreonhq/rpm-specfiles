%global source1_hash 942e71d427d575bb2604b7224e89f0d0a61f647df3f0c601c324ae1cc3c34300
%global source0_hash 813b3e37aca6df2a21a3b9f1d497f8cbab24a2b94cab325bffe65ee0f6cbebc6
%global gem_name concurrent-ruby
Name: rubygem-%{gem_name}
Version: 1.3.5
Release:        1%{?dist}
Summary:        Modern concurrency tools for Ruby
License: MIT
URL: http://www.concurrent-ruby.com
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ruby-concurrency/concurrent-ruby/archive/refs/tags/v1.3.5.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(timecop)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

# Remove bundled .jar
%gemspec_remove_file 'lib/concurrent-ruby/concurrent/concurrent_ruby.jar'

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
ln -s %{builddir}/spec spec
sed -i 's/allow_c_extensions/c_extensions_loaded/' \
  spec/concurrent/atomic/atomic_{fixnum,reference,boolean}_spec.rb
RUBYOPT=-Ilib/concurrent-ruby rspec -rspec_helper \
  -fd \
  --exclude-pattern 'spec/concurrent/{actor_spec.rb,channel_spec.rb,lazy_register_spec.rb,channel/**/*,edge/**/*,processing_actor_spec.rb,promises_spec.rb,throttle_spec.rb,cancellation_spec.rb,executor/wrapping_executor_spec.rb}' \
  spec
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-concurrent-ruby-doc -f %{oreon_filedir}/rubygem-concurrent-ruby-doc.list

%changelog

%autochangelog
