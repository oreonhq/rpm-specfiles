%global source0_hash 8569685c902108b1845be4e5794d646f2a8adcb0280d7651b600dab0844fe942
%global gem_name metaclass
Summary:        Adds a metaclass method to all Ruby objects
Name: rubygem-%{gem_name}
Version: 0.0.4
Release:        1%{?dist}
License: MIT
URL: http://github.com/floehopper/metaclass
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-metaclass-0.0.4-Move-to-Minitest-5.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Adds a metaclass method to all Ruby objects

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch 0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/require "bundler\/setup"/ d' test/test_helper.rb
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-metaclass-doc -f %{oreon_filedir}/rubygem-metaclass-doc.list

%changelog

%autochangelog
