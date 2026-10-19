%global source0_hash 81c454aaf1e2bd2c359e42aa9386c51820aadcc862fa9e86f61ff7248858deef
%global gem_name fog-xml
Name: rubygem-%{gem_name}
Version: 0.1.4
Release:        1%{?dist}
Summary:        XML parsing for fog providers
License: MIT
URL: https://github.com/fog/fog-xml
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(fog-core)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Extraction of the XML parsing tools shared between a
number of providers in the 'fog' gem.

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
sed -i '/require.*turn/ s/^/#/' spec/minitest_helper.rb
sed -i '/Turn/,/end/ s/^/#/' spec/minitest_helper.rb
ruby -Ispec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-fog-xml-doc -f %{oreon_filedir}/rubygem-fog-xml-doc.list

%changelog

%autochangelog
