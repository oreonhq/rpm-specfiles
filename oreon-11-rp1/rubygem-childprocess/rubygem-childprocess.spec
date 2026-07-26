%global source0_hash 3616ce99ccb242361ce7f2b19bf9ff3e6bc1d98b927c7edc29af8ca617ba6cd3

%global gem_name childprocess

Name: rubygem-%{gem_name}
Version: 4.1.0
Release: 13%{?dist}
Summary: A gem for controlling external programs running in the background
License: MIT
URL: http://github.com/enkessler/childprocess
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix `validates cleanly` spec compatibility with RubyGems 3.5+
# https://github.com/enkessler/childprocess/pull/193
Patch0: rubygem-childprocess-4.1.0-Make-validates-cleanly-spec-compatible-with-RubyGems-3-5-.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(ffi)
BuildRequires: rubygem(logger)
BuildRequires: rubygem(rspec) >= 3
BuildArch: noarch
# posix_spaw is not implemented everywhere, use just Intel for build.
ExclusiveArch: %{ix86} x86_64 noarch

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch 0 -p1

# ref: https://github.com/enkessler/childprocess/pull/199/
%gemspec_add_dep -g logger

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# We don't care about code coverage.
sed -i '/[cC]overalls/ s/^/#/' spec/spec_helper.rb

# Disable validity of .gemspec check, since it requires Git and it is not super
# important.
sed -i "/gemspec.validate/ s/^/#/" spec/childprocess_spec.rb

# We need Unicode support to pass "ChildProcess allows unicode characters
# in the environment" test case.
LC_ALL=C.UTF-8 RUBYOPT=-Ilib rspec spec

# Disable test failing for posix-spawn
# https://github.com/enkessler/childprocess/issues/173
sed -i '/^\s*it "can write to stdin interactively if duplex = true" do$/ a \
  skip' spec/io_spec.rb

# Test also posix_spawn, which requires FFI.
CHILDPROCESS_POSIX_SPAWN=true LC_ALL=C.UTF-8 RUBYOPT=-Ilib rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/appveyor.yml
%{gem_instdir}/childprocess.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
