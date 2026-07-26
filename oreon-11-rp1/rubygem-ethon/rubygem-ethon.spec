%global source0_hash 4d98dbe05fd53b7d4ce9fa4f5782b035124682ca0fffb52a836353903fc43051

# Generated from ethon-0.5.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ethon

Name: rubygem-%{gem_name}
Version: 0.17.0
Release: 1%{?dist}
Summary: Libcurl wrapper
License: MIT
URL: https://github.com/typhoeus/ethon
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/typhoeus/ethon.git && cd ethon
# git archive -v -o ethon-0.17.0-spec.tar.gz v0.17.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# This prevents test errors in Typhoeus:
# https://github.com/typhoeus/typhoeus/issues/710
# https://github.com/felipedmesquita/ethon/pull/13
Patch0: rubygem-ethon-0.17.0-fix-on-headers-regression.patch
Patch1: rubygem-ethon-0.17.0-fix-on-headers-regression-test.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(ffi) => 1.3.0
# https://github.com/typhoeus/ethon/blob/453c6f0ba37a7d42978c90f2399f5c2cd66b32a6/spec/ethon/easy/queryable_spec.rb#L164
BuildRequires: rubygem(mime-types) => 1.18
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rackup)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(webrick)
BuildArch: noarch

%description
Very lightweight libcurl wrapper.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%patch 0 -p1

( cd %{builddir}
%patch 1 -p1
)

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
ln -s %{builddir}/spec spec

# Don't use Bundler.
sed -i -e "/require 'bundler'/ s/^/#/" \
       -e "/Bundler.setup/ s/^/#/" \
       spec/spec_helper.rb

# `rackup` is preloaded by Bundler in upstream test suite. Load it explicitly
# here.
rspec -r rackup spec
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/ethon.gemspec

%changelog
%autochangelog
