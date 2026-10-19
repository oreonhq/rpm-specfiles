%global source0_hash fed7b1ef9dcad9365aceb36dcd66be4700d61c5798c8ad57773563ad39867db2
%global gem_name between_meals
Name: rubygem-%{gem_name}
Version: 0.0.12
Release:        1%{?dist}
Summary:        Between Meals
License: Apache-2.0
URL: https://github.com/facebook/between-meals
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: rubygem-%{gem_name}-%{version}-specs.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem-mixlib-shellout
BuildRequires:  rubygem-rspec
BuildRequires:  rubygem-rugged
BuildRequires:  rubygem-simplecov
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Between Meals is the library for calculating what Chef objects were modified
between two revisions in a version control system. It is also the library that
backs Taste Tester and Grocery Delivery. It currently supports SVN, GIT and
HG, but plugins can easily be written for other source control systems. It
also includes some wrappers around knife execution and a few other utility
functions.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

# From lib/between_meals/cmd.rb
%gemspec_add_dep -g logger

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
ln -s %{_builddir}/spec .
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-between_meals-doc -f %{oreon_filedir}/rubygem-between_meals-doc.list

%changelog

%autochangelog
