%global source0_hash 403bc5d598353821e94d4c870e7927dbd61731de38bdeb75741cbb4f18c47bf9

# Generated from rack-cache-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rack-cache

Name: rubygem-%{gem_name}
Version: 1.14.0
Release: 7%{?dist}
Summary: HTTP Caching for Rack
License: MIT
URL: https://github.com/rack/rack-cache
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rack/rack-cache.git && cd rack-cache
# git archive -v -o rack-cache-1.14.0-test.tar.gz v1.14.0 test/
Source1: %{gem_name}-%{version}-test.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-global_expectations)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rack)
BuildArch: noarch

%description
Rack::Cache is suitable as a quick drop-in component to enable HTTP caching
for Rack-based applications that produce freshness (expires, cache-control)
and/or validation (last-modified, etag) information.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

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
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# Get rid of Bundler.
sed -i '/bundler/ s/^/#/' test/test_helper.rb

# We don't have maxitest in Fedora, lets try Minitest.
sed -i '/global_must/ s/global_must/global_expectations/' test/test_helper.rb
sed -i 's/maxitest/minitest/' test/test_helper.rb
mv test/meta_store_test.rb{,.disabled}

ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
