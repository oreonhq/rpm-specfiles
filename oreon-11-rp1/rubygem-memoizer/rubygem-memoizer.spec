%global source0_hash 790d924ec13ea376aced58a88c0216e075762166e92080ac8b658859ae4e2945
%global gem_name memoizer
Name: rubygem-%{gem_name}
Version: 1.0.3
Release:        1%{?dist}
Summary:        Memoize your methods
License: MIT
URL: https://github.com/wegowise/memoizer
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(timecop)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Memoizer caches the results of your method calls, works well 
with methods that accept arguments or return nil. It's a 
simpler and more expicit alternative to ActiveSupport::Memoizable

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}
sed -i '/bundler\/setup/d' spec/spec_helper.rb

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rspec spec
%files -f %{oreon_filedir}/main.list
%files -n rubygem-memoizer-doc -f %{oreon_filedir}/rubygem-memoizer-doc.list

%changelog

%autochangelog
