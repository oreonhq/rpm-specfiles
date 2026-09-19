%global source0_hash 790d924ec13ea376aced58a88c0216e075762166e92080ac8b658859ae4e2945

%global gem_name memoizer

Name: rubygem-%{gem_name}
Version: 1.0.3
Release: 10%{?dist}
Summary: Memoize your methods
License: MIT
URL: https://github.com/wegowise/memoizer
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: ruby(release) >= 1.9.3
BuildRequires: rubygems-devel
BuildRequires: rubygem(timecop) >= 0.8.0
BuildRequires: rubygem(rspec) >= 3.5.0
BuildArch: noarch

%description
Memoizer caches the results of your method calls, works well 
with methods that accept arguments or return nil. It's a 
simpler and more expicit alternative to ActiveSupport::Memoizable

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}
sed -i '/bundler\/setup/d' spec/spec_helper.rb

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
rspec spec

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/memoizer.gemspec
%doc     %{gem_instdir}/README.md
%doc     %{gem_instdir}/CHANGELOG.txt
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}
%exclude %{gem_docdir}/rdoc

%changelog
%autochangelog
