%global source1_hash 3e5b873f4531e872910a5c708c909a4e881724b40466a4eb58466cbfbc350e5f
%global source0_hash a9e88e6ce9f8c912d349aa5401509165ec42326baf9e942a85de4b76dbc4119e
%global gem_name sprockets-rails
Name: rubygem-%{gem_name}
Version: 3.5.2
Release:        1%{?dist}
Summary:        Sprockets Rails integration
License: MIT
URL: https://github.com/rails/sprockets-rails
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/sprockets-rails/archive/refs/tags/v3.5.2.tar.gz
Patch0:  sprockets-rails-3.5.2-minitest6.patch
%dnl BuildRequires: rubygem(rake)
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygem(sprockets)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
(
cd %{_builddir}
%patch -P0 -p1
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
ln -s %{builddir}/test .
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-sprockets-rails-doc -f %{oreon_filedir}/rubygem-sprockets-rails-doc.list

%changelog

%autochangelog
