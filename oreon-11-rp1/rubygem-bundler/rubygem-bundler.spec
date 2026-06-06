%global source0_hash a25675ffbd055ae1186766cc1e120b4cf62588e88abb59b99c57e22b1c55c9eb
%global source1_hash none

%global gem_name bundler

# Enable test when building on local.
%bcond_with tests

%global connection_pool_version 2.5.0
%global fileutils_version 1.7.3
%global net_http_persistent_version 4.0.4
%global pub_grub_version 0.5.0
%global securerandom_version 0.4.1
%global thor_version 1.3.2
%global tsort_version 0.2.0
%global uri_version 1.0.3

Name: rubygem-%{gem_name}
Version: 2.6.9
Release: 4%{?dist}
Summary: Library and utilities to manage a Ruby application's gem dependencies
# BSD-2-Clause OR Ruby:
#   lib/bundler/vendor/fileutils
#   lib/bundler/vendor/tsort
#   lib/bundler/vendor/uri
# MIT:
#   lib/bundler/vendor/connection_pool
#   lib/bundler/vendor/net-http-persistent
#   lib/bundler/vendor/pub_brub
#   lib/bundler/vendor/thor
#   lib/rubygems/resolver/molinillo
License: MIT AND (Ruby OR BSD-2-Clause)
URL: https://bundler.io
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rubygems/rubygems/ && cd rubygems
# git archive -v -o bundler-2.6.9-specs.tar.gz bundler-v2.6.9 bundler/spec/ tool/bundler/{rubocop,standard,test}_gems.rb
Source1: %{gem_name}-%{version}-specs.tar.gz
# This revert changes which seems to require some setup prior running specs.
# https://github.com/rubygems/rubygems/issues/8698
Patch0:        rubygem-bundler-2.6.9-Revert-changes-in-spec-sectup.patch
# ruby package has just soft dependency on rubygem(io-console), while
# Bundler always requires it.
Requires: rubygem(io-console)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{with tests}
BuildRequires: ruby-devel
BuildRequires: libyaml-devel
BuildRequires: rubygem(rake)
BuildRequires: rubygem(rspec) >= 3.0
BuildRequires: %{_bindir}/git
BuildRequires: %{_bindir}/man
BuildRequires: %{_bindir}/ps
BuildRequires: gcc
%endif
# https://github.com/bundler/bundler/issues/3647
Provides: bundled(rubygem-connection_pool) = %{connection_pool_version}
Provides: bundled(rubygem-fileutils) = %{fileutils_version}
Provides: bundled(rubygem-net-http-persistent) = %{net_http_persistent_version}
Provides: bundled(rubygem-pub_grub) = %{pub_grub_version}
Provides: bundled(rubygem-securerandom) = %{securerandom_version}
Provides: bundled(rubygem-thor) = %{thor_version}
Provides: bundled(rubygem-tsort) = %{tsort_version}
Provides: bundled(rubygem-uri) = %{uri_version}
BuildArch: noarch

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
_specs="%{gem_name}-%{version}-specs.tar.gz"
if test ! -f "$_specs"; then
  curl -sfL -o _b.tar.gz "https://github.com/rubygems/bundler/archive/v%{version}.tar.gz"
  rm -rf _bdir && mkdir _bdir
  tar xf _b.tar.gz -C _bdir --strip-components=1
  tar czf "$_specs" -C _bdir bundler/spec tool/bundler/rubocop_gems.rb tool/bundler/standard_gems.rb tool/bundler/test_gems.rb
  rm -rf _bdir _b.tar.gz
fi

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
gem unpack ../%{gem_name}-%{version}.gem
tar xf ../%{gem_name}-%{version}-specs.tar.gz -C %{gem_name}-%{version}
cd %{gem_name}-%{version}

( cd %{builddir}
%patch 0 -p1
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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

# Man pages are used by Bundler internally, do not remove them!
for n in 5 1; do
  mkdir -p %{buildroot}%{_mandir}/man${n}
  for file in %{buildroot}%{gem_libdir}/bundler/man/*.${n}; do
    base_name=$(basename "${file}")
    cp -a "${file}" "%{buildroot}%{_mandir}/man${n}/${base_name}"
  done
done

%check
( cd .%{gem_instdir}
# Check bundled libraries.
[ `ls lib/bundler/vendor | wc -l` == 8 ]

# connection_pool.
[ "`ruby -e " \
  module Bundler; end; \
  require './lib/bundler/vendor/connection_pool/lib/connection_pool/version'; \
  puts Bundler::ConnectionPool::VERSION"`" \
  == '%{connection_pool_version}' ]

# FileUtils.
[ "`ruby -e " \
  module Bundler; end; \
  require './lib/bundler/vendor/fileutils/lib/fileutils'; \
  puts Bundler::FileUtils::VERSION"`" \
  == '%{fileutils_version}' ]

# PubGrub
[ `ruby -Ilib -e '
  module Bundler; end;
  require "bundler/vendor/pub_grub/lib/pub_grub/version";
  puts Bundler::PubGrub::VERSION'` == '%{pub_grub_version}' ]

# Net::HTTP::Persistent.
[ `ruby -Ilib -e '
  module Bundler; module Persistent; module Net; module HTTP; end; end; end; end
  require "bundler/vendor/net-http-persistent/lib/net/http/persistent"
  puts Gem::Net::HTTP::Persistent::VERSION'` == '%{net_http_persistent_version}' ]

# SecureRandom.
[ `ruby -Ilib -e '
  module Bundler; module Random; end; end;
  require "bundler/vendor/securerandom/lib/securerandom";
  puts Bundler::SecureRandom::VERSION'` == '%{securerandom_version}' ]

# Thor.
[ `ruby -e '
  module Bundler; end;
  require "./lib/bundler/vendor/thor/lib/thor/version"
  puts Bundler::Thor::VERSION'` == '%{thor_version}' ]

# TSort
[ `ruby -Ilib -e '
  module Bundler; end;
  require "bundler/vendor/tsort/lib/tsort";
  puts Bundler::TSort::VERSION'` == '%{tsort_version}' ]

# URI.
[ "`ruby -e "
  module Bundler; end; \
  require './lib/bundler/vendor/uri/lib/uri/version'; \
  puts Bundler::URI::VERSION"`" \
  == '%{uri_version}' ]

# Test suite has to be disabled for official build, since it downloads various
# gems, which are not in Fedora or they have different version etc.
# Nevertheless, the test suite should run for local builds.
%if %{with tests}

cp -a %{builddir}/bundler/spec .
cp -a %{builddir}/tool ..

# This dependency is relevant just to RubyGems. Removing it we can omit
# `BR: libffi-devel`
sed -i '/"fiddle"/ s/^/#/' ../tool/bundler/test_gems.rb

# This test fails due to rubypick.
sed -i '/^    context "when disable_exec_load is set" do$/,/^    end$/ {
  /it "runs" do/a\        skip
}' spec/commands/exec_spec.rb

# Avoid unexpected influence of Fedora specific configuration. This forces
# Ruby to load this empty operating_system.rb instead of operatin_system.rb
# shipped as part of RubyGems.
mkdir -p %{_builddir}/rubygems/rubygems/defaults/
touch %{_builddir}/rubygems/rubygems/defaults/operating_system.rb

# The sources are not stored in Git repository nor they come from Ruby source
# tarball. However, the test suite makes some assumptions based on that. Lets
# try to tweak them.
# 1. Standard Bundler layout is used:
sed -i '/def ruby_core_tarball\?/,/^    end$/ {
  /^    end$/i\      # Hardcode standar Bundler layout\n      return false
}' spec/support/path.rb
# 2. But without Git repo, we can't get hash:
sed -i '/def git_commit_sha\?/a\      return "unknown"' spec/support/build_metadata.rb
# 3. These are checking the Git repository content and would be disabled for Ruby
# tarball, but we change that condition above for different reasons 🙈
mv spec/quality_spec.rb{,.disable}
# 4. This check manpages conent and does not really influence runtime stability.
mv spec/quality_es_spec.rb{,.disable}
# 5. Convince the test suite, that the Ruby repo layout is used. This seems to be
# more suitable then assuming that the Bundler repo is used. `GEM_COMMAND` env
# variable unfortunately brings in another set of assumptions.
sed -i '/\sruby_repo:\s/ s/ruby_repo: .*/ruby_repo: true/' spec/support/filters.rb
# 6. Use the `ruby_core?` test version, so it matches the expectaion without
# making another assumpitons about directory layout.
sed -i '/if Spec::Path.ruby_core?/ s/$/ || true/' spec/commands/version_spec.rb

# We work with released version => change the condition.
# https://github.com/rubygems/rubygems/issues/5926
sed -i '/release.*be_falsey/I s/be_falsey/be_truthy/' spec/bundler/build_metadata_spec.rb

# This test is very specific to directory layouts and it its usefulness
# is mostly for upstream to point out some changes which needs to be included.
sed -i '/it "stays in sync with the rubygems implementation" do/a\    skip' spec/bundler/ci_detector_spec.rb

# Fix the compilation issues likely caused by:
# 
# https://github.com/rubygems/rubygems/issues/8694
sed -i 's/VALUE foo()/VALUE foo(VALUE _)/' spec/install/gemfile/git_spec.rb

# Please note that spec/install/security_policy_spec.rb fails with DEFAULT
# crypto policy. Use `update-crypto-policies --set LEGACY` to make it pass.
# https://github.com/rubygems/rubygems/issues/8693

# The `BUNDLER_GEM_DEFAULT_DIR` is useful to make pass e.g.:
# rspec ./spec/commands/exec_spec.rb:203 # bundle exec with default gems when not specified in Gemfile uses version provided by ruby
#
# It is necessary to require spec_helper.rb explicitly.
# https://github.com/bundler/bundler/pull/5634
RUBYOPT=-I%{_builddir}/rubygems GEM_PATH=%{gem_dir} BUNDLER_GEM_DEFAULT_DIR=%{gem_dir} rspec -rspec_helper spec -f d

%endif

)

%files
%dir %{gem_instdir}
%{_bindir}/bundle
%{_bindir}/bundler
%license %{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/bundler.gemspec
%{gem_instdir}/exe
%{gem_libdir}
%doc %{gem_libdir}/bundler/man/*
%exclude %{gem_cache}
%{gem_spec}
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.9-4
- Import
