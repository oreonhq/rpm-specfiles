%global source0_hash 26ee4fbce33ada25eb117ac71f2c24bf4d8b3414ab6b34f05b4708a3e90f1c6b
%global gem_name public_suffix
Name: rubygem-%{gem_name}
Version: 5.0.0
Release:        1%{?dist}
Summary:        Domain name parser based on the Public Suffix List
License: MIT AND MPL-2.0
URL: https://simonecarletti.com/code/publicsuffix-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
PublicSuffix can parse and decompose a domain name into top level domain,
domain and subdomains.

%package doc
Summary: Documentation for %{name}
License: MIT AND CC0-1.0
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
sed -i '/[Rr]eporters/ s/^/#/' test/test_helper.rb
LANG=C.utf-8 ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-public_suffix-doc -f %{oreon_filedir}/rubygem-public_suffix-doc.list

%changelog

%autochangelog
