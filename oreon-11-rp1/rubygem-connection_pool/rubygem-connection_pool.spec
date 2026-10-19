%global source0_hash 13a8fc3921ce4df8e04fb65f1037251decb08d74757b41163688bd1c1feccd39
%global gem_name connection_pool
Name: rubygem-%{gem_name}
Version: 2.2.5
Release:        1%{?dist}
Summary:        Generic connection pool for Ruby
License: MIT
URL: https://github.com/mperham/connection_pool
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  %{gem_name}-2.2.5-minitest6.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Generic connection pool for Ruby.

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
  ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-connection_pool-doc -f %{oreon_filedir}/rubygem-connection_pool-doc.list

%changelog

%autochangelog
