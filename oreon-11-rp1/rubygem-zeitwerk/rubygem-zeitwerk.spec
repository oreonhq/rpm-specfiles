%global source0_hash bb397b50c31127f8dab372fa9b21da1e7c453c5b57da172ed858136c6283f826

# Generated from zeitwerk-2.1.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name zeitwerk

Name: rubygem-%{gem_name}
Version: 2.6.6
Release: 10%{?dist}
Summary: Efficient and thread-safe constant autoloader
License: MIT
URL: https://github.com/fxn/zeitwerk
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Test suite is not included in packaged gem
# git clone https://github.com/fxn/zeitwerk.git --no-checkout
# cd zeitwerk && git archive -v -o zeitwerk-2.6.6-tests.txz v2.6.6 test
Source2: %{gem_name}-%{version}-tests.txz
# Fix compatibility with minitest 6
Patch0:  zeitwerk-2.6.6-minitest6.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildArch: noarch

%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem
and application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, preloading,
reloading, and eager loading.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b2
(
cd %{_builddir}
%patch -P0 -p1
)

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# focus gem is not needed for tests
sed -i '/require..minitest.focus./ s/^/#/' test/test_helper.rb
# Remove minitest-reporters. It does not provide any additional value while
# it blows up the dependency chain.
sed -i '/require..minitest.reporters./ s/^/#/' test/test_helper.rb
sed -i '/Minitest::Reporters/ s/^/#/' test/test_helper.rb

# Skip failing test
# https://github.com/fxn/zeitwerk/issues/202
sed -i '/returns true for a file in a descendant of an ignored directory/ a \
  skip' test/lib/zeitwerk/test_ignore.rb

ruby -Itest:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
