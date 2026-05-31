%global source0_hash 13266611fde7dcc5bd63d147e6ae7300a3500cb3d2fa9f9d3c6dfbff73d26fa7

# Generated from bson-1.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bson

Name: rubygem-%{gem_name}
Version: 4.15.0
Release: 14%{?dist}
Summary: Ruby implementation of the BSON specification
License: Apache-2.0
# Keep the URL, while different URL is used in the upstream gemspec file.
# Because there is a basic explanation about the bson
# that is a beneficial for Fedora user.
URL: http://bsonspec.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/mongodb/bson-ruby/blob/e560ee5c65f9f82d8f3430b5a72d8c9a3f1e0fdb/lib/bson/decimal128.rb#L16
# https://github.com/mongodb/bson-ruby/pull/340
Patch0:  bson-pr340-testsuite-explicit-require.patch
Requires: rubygem(bigdecimal)
# https://github.com/mongodb/bson-ruby/blob/e560ee5c65f9f82d8f3430b5a72d8c9a3f1e0fdb/lib/bson/ext_json.rb#L18
Requires: rubygem(json)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby-devel >= 2.3
BuildRequires: gcc
BuildRequires: rubygem(base64)
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(rspec)
# This package contains the binary extension originaly provided by bson_ext
# since F26 timeframe.
Provides: rubygem-bson_ext%{?_isa} = %{version}-%{release}
Provides: rubygem-bson_ext = %{version}-%{release}
Provides: rubygem(bson_ext) = %{version}-%{release}
Obsoletes: rubygem-bson_ext < 4.1.1-1

%description
A fully featured BSON specification implementation in Ruby.


%package doc
Summary: Documentation for %{name}
# MIT: spec/shared
# Git submodule originally living at:
# https://github.com/mongodb-labs/mongo-ruby-spec-shared
License: Apache-2.0 AND MIT
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/NOTICE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.15.0-14
- Prepare for Oreon 11 (RP1)
