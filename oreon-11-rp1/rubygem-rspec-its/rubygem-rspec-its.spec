%global source0_hash c404314f933ffd5ef6e2cfa87167e272477a7007467db5ec59c96ad1679c51f6
%global gem_name rspec-its
Name: rubygem-%{gem_name}
Version: 1.3.1
Release:        1%{?dist}
Summary:        Provides "its" method formerly part of rspec-core
License: MIT
URL: https://github.com/rspec/rspec-its
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-cucumber-1.3.1-Ruby-3-4-replaces-initial-backtick-by-single-quote.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(aruba)
BuildRequires:  rubygem(cucumber)
BuildRequires:  rubygem(matrix)
BuildRequires:  rubygem(rspec-core)
BuildRequires:  rubygem(rspec-expectations)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
RSpec extension gem for attribute matching.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

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
rspec spec
export RUBYOPT="-I${PWD}/lib"
cucumber --tags 'not @pre-3-9'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rspec-its-doc -f %{oreon_filedir}/rubygem-rspec-its-doc.list

%changelog

%autochangelog
