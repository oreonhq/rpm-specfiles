%global source0_hash 628949100091fddbdc98cd4d8eb07c83fa3e3ad7d616587398b8363923041f6c
%global gem_name hiera-vault
Name: rubygem-%{gem_name}
Version: 0.2.2
Release:        22%{?dist}
Summary:        Module for using vault as a hiera backend
License: Apache-2.0
URL: http://github.com/jsok/hiera-vault
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: hiera-vault-34.patch
Patch1: hiera-vault-37.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-hiera-vault-doc -f %{oreon_filedir}/rubygem-hiera-vault-doc.list

%changelog

%autochangelog
