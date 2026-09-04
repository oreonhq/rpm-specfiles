%global source0_hash 798f6af3556641a7619bad1dce04cdb6eb44b0216a991b0396ea7339276f2b47

# Generated from addressable-2.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name addressable

Name: rubygem-%{gem_name}
Version: 2.8.6
Release: 8%{?dist}
Summary: URI Implementation
License: Apache-2.0
URL: https://github.com/sporkmonger/addressable
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/sporkmonger/addressable/pull/557/commits/2d934a90f74fd4598cd05582ee7c5a24b87c76a0
# Fix for ruby4_0 Ractor
Patch0: addressable-pr557-ruby4_0-Ractor.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(public_suffix)
BuildRequires: rubygem(rspec-its)
BuildArch: noarch

%description
Addressable is an alternative implementation to the URI implementation that is
part of Ruby's standard library. It is flexible, offers heuristic parsing, and
additionally provides extensive support for IRIs and URI templates.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Drop Bundler dependency.
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/spec_helper.rb

# Remove tests failing because of missing internet connection.
mv spec/addressable/net_http_compat_spec.rb{,.disabled}

LC_ALL=C.UTF-8 rspec spec/
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/data
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
%autochangelog
