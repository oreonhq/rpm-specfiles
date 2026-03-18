# Generated from abrt-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name abrt

Name: rubygem-%{gem_name}
Version: 0.5.0
Release: 2%{?dist}
Summary: ABRT support for Ruby
License: MIT
URL: http://github.com/voxik/abrt-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/voxik/abrt-ruby.git && cd abrt-ruby
# git archive -v -o abrt-0.5.0-spec.tar.gz v0.5.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
Requires: libreport-filesystem
# `logger` is now used instead of Ruby `Syslog`
# https://github.com/voxik/abrt-ruby/pull/15/commits/ae31cc838a576794309209ec3ea83a18d12eb14e
Requires: %{_bindir}/logger
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Provides ABRT reporting support for libraries/applications written using Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
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

mkdir -p %{buildroot}%{_sysconfdir}/libreport/events.d/
cp -a .%{gem_instdir}/config/ruby_event.conf %{buildroot}%{_sysconfdir}/libreport/events.d/


%check
pushd .%{gem_instdir}
cp -a %{_builddir}/spec spec

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%exclude %{gem_instdir}/config
%config(noreplace) %{_sysconfdir}/libreport/events.d/ruby_event.conf

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.0-2
- Prepare for Oreon 11 (RP1)
