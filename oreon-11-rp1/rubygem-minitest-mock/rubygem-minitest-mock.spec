# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7040ed7185417a966920987eaa6eaf1be4ea1fc5b25bb03ff4703f98564a55b0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global	gem_name	minitest-mock

Name:		rubygem-%{gem_name}
Version:	5.27.0
Release:	1%{?dist}

Summary:	minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object framework
License:	MIT
URL:		https://minite.st/

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: oreon-rpm-macros
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest)
BuildArch:	noarch

%description
minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub)
object framework.
The minitest-mock gem is an extraction of minitest/mock.rb from
minitest in order to make it easier to maintain independent of
minitest.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}.

%prep
%oreon_sha256
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Manifest.txt \
	Rakefile \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
export RUBYLIB=$(pwd)/lib:$(pwd)/test

sed -i test/minitest/test_minitest_mock.rb \
	-e '\@assertion_count@s|assert_equal|#assert_equal|'
ruby -e \
	'Dir.glob "./test/minitest/test_*.rb", &method(:require)'
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/README.rdoc
%{gem_libdir}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
