%global source0_hash e515712e48df1f687a1d7c380fd7b07b8558faa26464474da64183a7426fa93b
%global gem_name rails-dom-testing
Name: rubygem-%{gem_name}
Version: 2.2.0
Release:        1%{?dist}
Summary:        Dom and Selector assertions for Rails applications
License: MIT
URL: https://github.com/rails/rails-dom-testing
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  rails-dom-testing-2.2.0-minitest6.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This gem can compare doms and assert certain elements exists in doms using
Nokogiri.

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
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rails-dom-testing-doc -f %{oreon_filedir}/rubygem-rails-dom-testing-doc.list

%changelog

%autochangelog
