%global source0_hash 798f6af3556641a7619bad1dce04cdb6eb44b0216a991b0396ea7339276f2b47
%global gem_name addressable
Name: rubygem-%{gem_name}
Version: 2.8.6
Release:        8%{?dist}
Summary:        URI Implementation
License: Apache-2.0
URL: https://github.com/sporkmonger/addressable
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: addressable-pr557-ruby4_0-Ractor.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(public_suffix)
BuildRequires:  rubygem(rspec-its)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/spec_helper.rb
mv spec/addressable/net_http_compat_spec.rb{,.disabled}
LC_ALL=C.UTF-8 rspec spec/
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-addressable-doc -f %{oreon_filedir}/rubygem-addressable-doc.list

%changelog

%autochangelog
