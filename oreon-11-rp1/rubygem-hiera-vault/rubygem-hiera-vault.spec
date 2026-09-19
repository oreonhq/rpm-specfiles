%global source0_hash 628949100091fddbdc98cd4d8eb07c83fa3e3ad7d616587398b8363923041f6c

# Generated from hiera-vault-0.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hiera-vault

Name: rubygem-%{gem_name}
Version: 0.2.2
Release: 22%{?dist}
Summary: Module for using vault as a hiera backend
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: http://github.com/jsok/hiera-vault
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Fix translation isue with version 5 hiera.yaml
# https://github.com/jsok/hiera-vault/pull/34
Patch0: hiera-vault-34.patch

# Vault kv2 - based on upstream PR, with default field fixes
# https://github.com/jsok/hiera-vault/pull/37
Patch1: hiera-vault-37.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
Hiera backend for looking up secrets stored in Vault.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch -P0 -p1
%patch -P1 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
