%global source1_hash 09f17263eb3ca6a0bdfcb4dfd6d4d68e5370595872f48b0a1d5388b3484d81de
%global source0_hash 7f0e48821e6b4c881daaa40fb1583e308937c22a9c84883c150b399c3b5c3029
%global gem_name track_open_instances
Name: rubygem-%{gem_name}
Version: 0.1.15
Release:        1%{?dist}
Summary:        A mix-in to ensure that all instances of a class are closed
License: MIT
URL: https://github.com/main-branch/track_open_instances
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/main-branch/%{gem_name}/archive/v%{version}/%{gem_name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A mix-in to track instances of Ruby classes that require explicit cleanup,
helping to identify potential resource leaks. It maintains a list of
created instances and allows checking for any that remain open.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# unpack only the spec files from SOURCE1.
tar zxf %{SOURCE1} %{gem_name}-%{version}/spec --strip-components 1

# Skip coverage test formatter, not available and undesirable
sed -i '/# SimpleCov configuration/,/^end/s/.*//'  spec/spec_helper.rb
sed -i '/^SimpleCov::RSpec.start/,/^end/s/.*//' spec/spec_helper.rb

# Not surprising this is needed but odd its not needed when using
# rake.
sed -i '1a require '\''track_open_instances'\''' spec/spec_helper.rb

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
%files -n rubygem-track_open_instances-doc -f %{oreon_filedir}/rubygem-track_open_instances-doc.list

%changelog

%autochangelog
