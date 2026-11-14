# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: (Ruby OR BSDL) AND PSFL AND Public Domain

%global source0_hash 00e401e1c66fd3f968dae3a9c2aa76e009826c4a84299e73b81d8912c3032e09
%global gem_name test-unit

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: rubygem-%{gem_name}
Version: 3.7.8
Release: 1%{?dist}
Summary: An xUnit family unit testing framework for Ruby
License: (Ruby OR BSDL) AND PSFL AND Public Domain
URL: https://test-unit.github.io/
Source0: https://github.com/test-unit/test-unit/archive/refs/tags/%{version}.tar.gz#/test-unit-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: ruby
BuildRequires: rubygems-devel
Requires: ruby(release)
Requires: ruby(rubygems)
Provides: rubygem(%{gem_name}) = %{version}

%description
test-unit is an xUnit family unit testing framework for Ruby.

%prep
%oreon_sha256
%autosetup -n test-unit-%{version}

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
ruby -Ilib -e 'require "test/unit"; puts Test::Unit::VERSION'

%files
%license LICENSE.txt BSDL COPYING PSFL
%doc README.md
%{gem_instdir}
%{gem_cache}
%{gem_spec}
%{gem_docdir}

%changelog
%autochangelog
