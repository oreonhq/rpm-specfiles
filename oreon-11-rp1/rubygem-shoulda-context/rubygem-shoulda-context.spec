%global source0_hash 7adf45342cd800f507d2a053658cb1cce2884b616b26004d39684b912ea32c34
%global gem_name shoulda-context
Name: rubygem-%{gem_name}
Version: 2.0.0
Release:        1%{?dist}
Summary:        Context framework extracted from Shoulda
License: MIT
URL: https://github.com/thoughtbot/shoulda-context
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-shoulda-context-2.0.0-Use-File-exist.patch
Patch1: rubygem-shoulda-context-3.0.0.rc1-Ignore-Resolving-dependencies.-message-by-Bundler.patch
Patch2: rubygem-shoulda-context-2.0.0-minitest6.patch
Patch3: rubygem-shoulda-context-2.0.0-test-unit-374.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/git/ s/^/#/' shoulda-context.gemspec
cat << EOF > gemfiles/test.gemfile
source "https://rubygems.org"
gem "minitest"
gem "mocha"
gem "test-unit"
gemspec path: "../"
EOF
BUNDLE_GEMFILE=gemfiles/test.gemfile bundle install --local
sed -i '/require "appraisal"/ s/^/#/' test/support/current_bundle.rb
sed -i '/assert_appraisal!/ s/^/#/' test/test_helper.rb
sed -i '/require "pry-byebug"/ s/^/#/' test/test_helper.rb
sed -i '/require "warnings_logger"/ s/^/#/' test/test_helper.rb
sed -i '/WarningsLogger/,/^)/ s/^/#/' test/test_helper.rb
sed -i '/require_relative "support\/rails_application_with_shoulda_context"/ s/^/#/' test/test_helper.rb
mv test/shoulda/railtie_test.rb{,.disable}
mv test/shoulda/rerun_snippet_test.rb{,.disable}
TEST_FRAMEWORK=minitest BUNDLE_GEMFILE=gemfiles/test.gemfile ruby -Ilib:test -rsingleton -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
TEST_FRAMEWORK=test_unit BUNDLE_GEMFILE=gemfiles/test.gemfile ruby -Ilib:test -rsingleton -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-shoulda-context-doc -f %{oreon_filedir}/rubygem-shoulda-context-doc.list

%changelog

%autochangelog
