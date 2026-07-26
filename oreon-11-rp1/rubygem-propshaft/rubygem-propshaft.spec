%global source0_hash 9acc664ef67e819ffa3d95bd7ad4c3623ea799110c5f4dee67fa7e583e74c392

# Generated from propshaft-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name propshaft

Name: rubygem-%{gem_name}
Version: 1.3.1
Release: 3%{?dist}
Summary: Deliver assets for Rails
License: MIT
URL: https://github.com/rails/propshaft
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone http://github.com/rails/propshaft.git && cd propshaft
# git archive -v -o propshaft-1.3.1-tests.tar.gz v1.3.1 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.7.0
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(actioncable)
BuildRequires: rubygem(railties)
BuildArch: noarch

%description
Propshaft is an asset pipeline library for Rails. It's built for an era where
bundling assets to save on HTTP connections is no longer urgent, where
JavaScript and CSS are either compiled by dedicated Node.js bundlers or served
directly to the browsers, and where increases in bandwidth have made the need
for minification less pressing. These factors allow for a dramatically simpler
and faster asset pipeline compared to previous options, like Sprockets.

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
( cd .%{gem_instdir}
ln -s %{builddir}/test .

# Remove Bundler usage.
sed -i '/Bundler.require/ s/^/#/' test/dummy/config/application.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
%autochangelog
