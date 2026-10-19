%global source0_hash 7200a38a1c0081aa81b7a9757e7a299db75bc58cf1fd45ca7919a91627d227d6
%global gem_name jbuilder
Name: rubygem-%{gem_name}
Version: 2.13.0
Release:        1%{?dist}
Summary:        Create JSON structures via a Builder-style DSL
License: MIT
URL: https://github.com/rails/jbuilder
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activemodel)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Jbuilder gives you a simple DSL for declaring JSON structures that beats
massaging giant hash structures. This is particularly helpful when
the generation process is fraught with conditionals and loops.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

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
sed -i '/bundler\/setup/ s/^/#/' test/test_helper.rb
ruby -Ilib:test -e "Dir.glob './test/*_test.rb', &method(:require)"
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-jbuilder-doc -f %{oreon_filedir}/rubygem-jbuilder-doc.list

%changelog

%autochangelog
