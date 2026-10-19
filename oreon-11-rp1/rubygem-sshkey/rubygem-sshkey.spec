%global source0_hash 77d162e8bcd5d2a1833193c3ad7700b2c6994dad547c8e2341e4598d4bb1730d
%global gem_name sshkey
Name:     rubygem-%{gem_name}
Version:  2.0.0
Release:        1%{?dist}
Summary:        Generate private/public SSH key-pairs using pure Ruby
License:  MIT
URL:      https://github.com/bensie/sshkey
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch: noarch
Requires: ruby(release)
Requires: rubygems
Provides: rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems
BuildRequires:  rubygems-devel
# /oreon:deps
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
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/.gitignore
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd %{buildroot}%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-sshkey-doc -f %{oreon_filedir}/rubygem-sshkey-doc.list

%changelog

%autochangelog
