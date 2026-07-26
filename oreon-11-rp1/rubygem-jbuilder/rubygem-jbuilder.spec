%global source0_hash 7200a38a1c0081aa81b7a9757e7a299db75bc58cf1fd45ca7919a91627d227d6

# Generated from jbuilder-1.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jbuilder

Name: rubygem-%{gem_name}
Version: 2.13.0
Release: 3%{?dist}
Summary: Create JSON structures via a Builder-style DSL
License: MIT
URL: https://github.com/rails/jbuilder
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activemodel)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(railties)
BuildArch: noarch

%description
Jbuilder gives you a simple DSL for declaring JSON structures that beats
massaging giant hash structures. This is particularly helpful when
the generation process is fraught with conditionals and loops.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

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
# Get rid of Bundler.
sed -i '/bundler\/setup/ s/^/#/' test/test_helper.rb

ruby -Ilib:test -e "Dir.glob './test/*_test.rb', &method(:require)"
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Appraisals
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/bin
%{gem_instdir}/jbuilder.gemspec
%{gem_instdir}/test
%{gem_instdir}/gemfiles

%changelog
%autochangelog
