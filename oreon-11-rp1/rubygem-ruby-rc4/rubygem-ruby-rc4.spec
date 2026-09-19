%global source0_hash 00cc40a39d20b53f5459e7ea006a92cf584e9bc275e2a6f7aa1515510e896c03

%global gem_name ruby-rc4

Name: rubygem-%{gem_name}
Version: 0.1.5
Release: 30%{?dist}
Summary: Pure Ruby implementation of the RC4 algorithm
License: MIT
URL: https://github.com/caiges/Ruby-RC4
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
RubyRC4 is a pure Ruby implementation of the RC4 algorithm.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

sed -i 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' %{buildroot}%{gem_instdir}/spec/rc4_spec.rb

rm %{buildroot}%{gem_instdir}/{README.md,LICENSE}

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%license LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
%autochangelog
