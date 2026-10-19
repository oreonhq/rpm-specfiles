%global source0_hash 29346c2d8364c19effb548b7a8952bf187545b99b70d1ddde76bd6c69046d27c
%global gem_name vault
Name: rubygem-%{gem_name}
Version: 0.18.2
Release:        1%{?dist}
Summary:        A Ruby API client for interacting with a Vault server
License: MPL-2.0
URL: https://github.com/hashicorp/vault-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
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
%files -n rubygem-vault-doc -f %{oreon_filedir}/rubygem-vault-doc.list

%changelog

%autochangelog
