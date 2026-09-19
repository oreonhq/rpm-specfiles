%global source0_hash 3dfb41faf0fca7fc3abce3edfe4679f3566b8e6f891dbe78a314255d2eff2654

# Generated from mixlib-log-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-log

Name: rubygem-%{gem_name}
Version: 3.0.9
Release: 14%{?dist}
Summary: A gem that provides a simple mixin for log functionality
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/chef/mixlib-log
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/chef/mixlib-log && cd mixlib-log
# git checkout v3.0.9
# tar -czf rubygem-mixlib-log-3.0.9-specs.tgz spec/
Source1: rubygem-mixlib-log-%{version}-specs.tar.gz
# https://github.com/chef/mixlib-log/pull/74
Patch0:  mixlib-log-pr74-ruby33-Logger-support.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem-rspec
BuildRequires: rubygem(logger)
BuildArch: noarch

%description
A gem that provides a simple mixin for log functionality.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
%patch -P0 -p1

# from lib/mixlib/log.rb
%gemspec_add_dep -g logger

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
ln -s %{_builddir}/spec .
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
