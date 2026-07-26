%global source0_hash 26ee4fbce33ada25eb117ac71f2c24bf4d8b3414ab6b34f05b4708a3e90f1c6b

# Generated from public_suffix-2.0.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name public_suffix

Name: rubygem-%{gem_name}
Version: 5.0.0
Release: 8%{?dist}
Summary: Domain name parser based on the Public Suffix List
# MPLv2.0: %%{gem_instdir}/data/list.txt
License: MIT AND MPL-2.0
URL: https://simonecarletti.com/code/publicsuffix-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildArch: noarch

%description
PublicSuffix can parse and decompose a domain name into top level domain,
domain and subdomains.

%package doc
Summary: Documentation for %{name}
# CC0-1.0: %%{gem_instdir}/test/tests.txt
License: MIT AND CC0-1.0
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
# We don't have minitest-reporters in Fedora yet, but they are not needed
# very likely.
sed -i '/[Rr]eporters/ s/^/#/' test/test_helper.rb

LANG=C.utf-8 ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
# This is usefull just for development.
%exclude %{gem_instdir}/bin
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_instdir}/public_suffix.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/2.0-Upgrade.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/test
%exclude %{gem_instdir}/test/.empty

%changelog
%autochangelog
