%global source0_hash adfbe09decee22deea2dc7a6b60698766306d3e74e9af0e03199de80b029a3eb

%global gem_name multi_test

Name: rubygem-%{gem_name}
Version: 0.1.2
Release: 21%{?dist}
Summary: Wafter-thin gem to disable autorun of various testing libraries
License: MIT
URL: http://cukes.info
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# Each unit tests depends on the condition of installed
# of minitest, rspec and test-unit
# Run tests for one condition (minitest only is installed).
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
multi_test gives a uniform interface onto whatever testing library has been
loaded into a running Ruby process. It can be used to clobber autorun behaviour
from older versions of Test::Unit that automatically hook in when the user
requires them.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Disable the test depends on bundler.
mv test/scenarios/bundler_require.rb{,.disabled}
# Disable the test for rspec
mv test/scenarios/rspec_matchers.rb{,.disabled}
mv test/scenarios/spec_matchers.rb{,.disabled}
# Disable the test for test-unit
mv test/scenarios/require_test_unit.rb{,.disabled}
mv test/scenarios/test_unit_assertions.rb{,.disabled}

ruby -Ilib <<EOR
  Dir.glob "./test/scenarios/*.rb" do |filename|
    puts "Testing file: #{filename}"
    require filename
  end
EOR
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Makefile
%{gem_instdir}/Rakefile
# This is not the original file => makes no sense to ship it.
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test

%changelog
%autochangelog
