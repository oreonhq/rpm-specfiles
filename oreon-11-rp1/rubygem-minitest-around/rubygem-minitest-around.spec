%global source0_hash b0348f1c6bfd8d64b0f9423af468f0f717fff4a4afd08cb279fd2b3b5453000d
%global	gem_name	minitest-around
Name:		rubygem-%{gem_name}
Version:	0.6.0
Release:        1%{?dist}
Summary:        Around block for minitest
License:	MIT
URL:		https://github.com/splattael/minitest-around
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
Source2:	%{gem_name}-create-missing-test-files.sh
BuildArch:	noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(cucumber)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Alternative for setup/teardown dance.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n  %{gem_name}-%{version} -b 1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp -a \
	test/ \
	features/ \
	.%{gem_instdir}
export CUCUMBER_PUBLISH_QUIET=true
pushd .%{gem_instdir}
sed -i "/require 'bundler/ s/^/#/" test/test_helper.rb
env RUBYOPT=-Ilib \
	ruby -e 'Dir.glob "./test/*_{test,spec}.rb", &method(:require)'
env RUBYOPT=-Ilib \
	cucumber --tag 'not @todo' --tag 'not @rspec'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-minitest-around-doc -f %{oreon_filedir}/rubygem-minitest-around-doc.list

%changelog

%autochangelog
