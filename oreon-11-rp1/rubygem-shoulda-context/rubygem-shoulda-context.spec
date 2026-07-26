%global source0_hash 7adf45342cd800f507d2a053658cb1cce2884b616b26004d39684b912ea32c34

%global gem_name shoulda-context

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 8%{?dist}
Summary: Context framework extracted from Shoulda
License: MIT
URL: https://github.com/thoughtbot/shoulda-context
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Use `File.exist?` instead of removed `File.exists` for Ruby 3.2
# compatibility.
# https://github.com/thoughtbot/shoulda-context/pull/70
Patch0: rubygem-shoulda-context-2.0.0-Use-File-exist.patch
# Avoid Bundler re-resolving dependencies test suite issues.
# https://github.com/thoughtbot/shoulda-context/pull/111
Patch1: rubygem-shoulda-context-3.0.0.rc1-Ignore-Resolving-dependencies.-message-by-Bundler.patch
# Support minitest 6
Patch2: rubygem-shoulda-context-2.0.0-minitest6.patch
# Support test-unit 3.7.4 and above
# ref: https://github.com/test-unit/test-unit/pull/341
Patch3: rubygem-shoulda-context-2.0.0-test-unit-374.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
Shoulda Context makes it easy to write understandable and maintainable tests
under Minitest and Test::Unit within Rails projects or plain Ruby projects.
It's fully compatible with your existing tests and requires no retooling to
use.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# Remove /usr/bin/env from shebang so RPM doesn't consider this a dependency
sed -i 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' exe/convert_to_should_syntax

%gemspec_remove_file -t "test/fake_rails_root/vendor/plugins/.keep"
%gemspec_remove_file "test/fake_rails_root/vendor/plugins/.keep"

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1

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

%check
pushd .%{gem_instdir}
# No need to depend on git.
sed -i '/git/ s/^/#/' shoulda-context.gemspec

# Create simple test file which satisfies the test suite.
cat << EOF > gemfiles/test.gemfile
source "https://rubygems.org"

gem "minitest"
gem "mocha"
gem "test-unit"

gemspec path: "../"
EOF
BUNDLE_GEMFILE=gemfiles/test.gemfile bundle install --local

# Don't depend on Appraisal gem.
sed -i '/require "appraisal"/ s/^/#/' test/support/current_bundle.rb
sed -i '/assert_appraisal!/ s/^/#/' test/test_helper.rb

# We don't really need pry-byebug.
sed -i '/require "pry-byebug"/ s/^/#/' test/test_helper.rb

# We don't have warnings_logger gem available.
sed -i '/require "warnings_logger"/ s/^/#/' test/test_helper.rb
sed -i '/WarningsLogger/,/^)/ s/^/#/' test/test_helper.rb

# We don't have available snow globe gem, which is required for Rails related
# test cases.
sed -i '/require_relative "support\/rails_application_with_shoulda_context"/ s/^/#/' test/test_helper.rb
mv test/shoulda/railtie_test.rb{,.disable}
mv test/shoulda/rerun_snippet_test.rb{,.disable}

TEST_FRAMEWORK=minitest BUNDLE_GEMFILE=gemfiles/test.gemfile ruby -Ilib:test -rsingleton -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
TEST_FRAMEWORK=test_unit BUNDLE_GEMFILE=gemfiles/test.gemfile ruby -Ilib:test -rsingleton -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/convert_to_should_syntax
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Appraisals
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/bin
%{gem_instdir}/gemfiles
%{gem_instdir}/Rakefile
%{gem_instdir}/shoulda-context.gemspec
%{gem_instdir}/tasks
%{gem_instdir}/test

%changelog
%autochangelog
