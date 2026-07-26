%global source0_hash e247133988d38cf4fd1ac6c96d4d6e5c9a9f619fefddb3d2f712063d7c94cbbf

# Generated from web-console-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name web-console

Name: rubygem-%{gem_name}
Version: 4.2.0
Release: 8%{?dist}
Summary: A debugging tool for your Ruby on Rails applications
License: MIT
URL: https://github.com/rails/web-console
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/web-console.git && cd web-console
# git archive -v -o web-console-4.2.0-tests.tar.gz v4.2.0 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(railties)
BuildRequires: rubygem(activemodel)
BuildRequires: rubygem(bindex)
BuildRequires: rubygem(mocha)

BuildArch: noarch

%description
A debugging tool for your Ruby on Rails applications.

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

# Run the test suite
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

# We don't care about code coverage.
sed -i '/[Ss]imple[Cc]ov/ s/^/#/' test/test_helper.rb
# We don't use Bundler.
sed -i '/^Bundler.require/ s/^/#/' test/dummy/config/application.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.markdown
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile

%changelog
%autochangelog
