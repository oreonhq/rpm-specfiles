%global source1_hash d76f4292eaee52506c2d9c440965d02f9c3c0425052ff981094d7c92d3f8fb46
%global source0_hash c73eb646d450044241c973a8360f6326e33ec5ad933f7acf503f6f3579873a71
%global gem_name process_executer
Name: rubygem-%{gem_name}
Version: 4.0.2
Release:        1%{?dist}
Summary:        An API for executing commands in a sub process
License: MIT
URL: https://github.com/main-branch/process_executer
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/main-branch/%{gem_name}/archive/v%{version}/%{gem_name}-%{version}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(track_open_instances)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
An API for executing commands in a sub process.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
An API for executing commands in a sub process

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
# From lib/process_executer.rb
%gemspec_add_dep -g logger

# unpack only the spec files from SOURCE1.
tar zxf %{SOURCE1} %{gem_name}-%{version}/spec --strip-components 1

# Skip coverage test formatter, not available and undesirable
sed -i '/# SimpleCov configuration/,/^end/s/.*//'  spec/spec_helper.rb
sed -i '/^SimpleCov::RSpec.start/,/^end/s/.*//' spec/spec_helper.rb

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rspec spec
%files -f %{oreon_filedir}/main.list
%files -n rubygem-process_executer-doc -f %{oreon_filedir}/rubygem-process_executer-doc.list

%changelog

%autochangelog
