%global source0_hash 77d162e8bcd5d2a1833193c3ad7700b2c6994dad547c8e2341e4598d4bb1730d

%global gem_name sshkey

Name:     rubygem-%{gem_name}
Version:  2.0.0
Release:  15%{?dist}
Summary:  Generate private/public SSH key-pairs using pure Ruby
License:  MIT
URL:      https://github.com/bensie/sshkey
Source0:  http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch: noarch
BuildRequires: ruby(release)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygems
BuildRequires: rubygems-devel
Requires: ruby(release)
Requires: rubygems

Provides: rubygem(%{gem_name}) = %{version}

%description
Generate private and public SSH keys (RSA and DSA supported) using pure Ruby.

%package doc
Summary: Documentation for %{gem_name}
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

#cleanup some files
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/.gitignore

%check
pushd %{buildroot}%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%doc LICENSE 
%dir %{gem_instdir}
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/Gemfile
%doc %{gem_docdir}
%{gem_instdir}/test

%changelog
%autochangelog
