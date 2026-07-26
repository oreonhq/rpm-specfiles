%global source0_hash 8daf828cc77bcf7d63b0e3bdb6caa47e2272dcfaf4fbfe46f8c3a9df087a829b

# Generated from tzinfo-0.3.26.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tzinfo

Name: rubygem-%{gem_name}
Version: 2.0.6
Release: 8%{?dist}
Summary: Time Zone Library
License: MIT
URL: https://tzinfo.github.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Gem file does not contain a test suite, you can create it like so:
# git clone https://github.com/tzinfo/tzinfo.git --no-checkout
# cd tzinfo && git archive -v -o tzinfo-2.0.6-tests.txz v2.0.6 test/
Source1: %{gem_name}-%{version}-tests.txz
# Fix compatibility with minitest 6
Patch0:  %{gem_name}-2.0.6-minitest6.patch
# tzdata might not be available on the system, but users still might prefer
# to use tzinfo-data gem (although it is not available in Fedora).
# https://fedoraproject.org/wiki/Changes/AllowRemovalOfTzdata
Recommends: tzdata
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(concurrent-ruby)
BuildArch: noarch

%description
TZInfo provides access to time zone data and allows times to be converted
using time zone rules.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
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

# We don't want to use bundler
sed -i "/raise 'Tests must be run with bundler/ s/^/#/" \
  test/test_utils.rb

export RUBYOPT="-Ilib"

ruby test/ts_all_ruby_format1.rb
ruby test/ts_all_ruby_format2.rb
ruby test/ts_all_zoneinfo.rb

# Test with system tzdata.
sed -i '/zoneinfo_path/ s|= .*|= "%{_datadir}/zoneinfo"|' test/ts_all_zoneinfo.rb

# The test is designed to run with internal zoneinfo fixtures, therefore there
# might be test failures.
# https://github.com/tzinfo/tzinfo/issues/141
ruby test/ts_all_zoneinfo.rb || :
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
