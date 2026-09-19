%global source0_hash 29346c2d8364c19effb548b7a8952bf187545b99b70d1ddde76bd6c69046d27c

# Generated from vault-0.12.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name vault

Name: rubygem-%{gem_name}
Version: 0.18.2
Release: 7%{?dist}
Summary: A Ruby API client for interacting with a Vault server
License: MPL-2.0
URL: https://github.com/hashicorp/vault-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(pry) >= 0.13.1
# BuildRequires: rubygem(pry) < 0.14
# BuildRequires: rubygem(rspec) >= 3.5
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(yard) >= 0.9.24
# BuildRequires: rubygem(yard) < 0.10
# BuildRequires: rubygem(webmock) >= 3.8.3
# BuildRequires: rubygem(webmock) < 3.9
BuildArch: noarch

%description
%{summary}

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
# rspec spec
popd

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

%changelog
%autochangelog
