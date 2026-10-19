%global source1_hash 4bd9f4f15a1c18f6f396477c78ff35edad8d1813acfb5d27be51c8d543c164a1
%global source0_hash 5e8200521400d6695e6c0e20e0741a0a8e43a18e2fed2188ee12d958ad06d243
%global gem_name git
Name: rubygem-%{gem_name}
Version: 4.3.0
Release:        1%{?dist}
Summary:        Ruby/Git is a Ruby library that can be used to create, read and manipulate Git repositories by wrapping system calls to the git binary
License: MIT
URL: http://github.com/schacon/ruby-git
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ruby-git/ruby-git/archive/v%{version}/ruby-git-%{version}.tar.gz
BuildArch: noarch
Requires:  git-core
# oreon:deps
BuildRequires:  git-core
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(addressable)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(process_executer)
BuildRequires:  rubygem(rchardet)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/Git is a Ruby library that can be used to create, read and manipulate Git
repositories by wrapping system calls to the git binary.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# unpack only the test files from SOURCE1.
tar zxf %{SOURCE1} ruby-git-%{version}/tests --strip-components 1
tar zxf %{SOURCE1} ruby-git-%{version}/bin --strip-components 1

# Some tests require rubygem-minitar - skip them.
# https://bugzilla.redhat.com/show_bug.cgi?id=2181580
rm -f tests/units/test_archive.rb
sed -i 's/^.*minitar.*//' tests/test_helper.rb
# Requires writing to home directory with a generated gpg key ignore
rm -f tests/units/test_signed_commits.rb

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

git config --global init.defaultBranch main
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
ruby  -Ilib -I. -Itests -e 'Dir.glob "tests/**/*.rb", &method(:require)'
%files -f %{oreon_filedir}/main.list
%files -n rubygem-git-doc -f %{oreon_filedir}/rubygem-git-doc.list

%changelog

%autochangelog
