%global source1_hash f9839b916869a9fff187c649a1ddff6070632d2f64b348ca02fa299e22780e64
%global source0_hash 9acc664ef67e819ffa3d95bd7ad4c3623ea799110c5f4dee67fa7e583e74c392
%global gem_name propshaft
Name: rubygem-%{gem_name}
Version: 1.3.1
Release:        3%{?dist}
Summary:        Deliver assets for Rails
License: MIT
URL: https://github.com/rails/propshaft
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/propshaft/archive/refs/tags/v1.3.1.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(actioncable)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Propshaft is an asset pipeline library for Rails. It's built for an era where
bundling assets to save on HTTP connections is no longer urgent, where
JavaScript and CSS are either compiled by dedicated Node.js bundlers or served
directly to the browsers, and where increases in bandwidth have made the need
for minification less pressing. These factors allow for a dramatically simpler
and faster asset pipeline compared to previous options, like Sprockets.

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
sed -i '/Bundler.require/ s/^/#/' test/dummy/config/application.rb
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-propshaft-doc -f %{oreon_filedir}/rubygem-propshaft-doc.list

%changelog

%autochangelog
