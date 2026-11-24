# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 90891fdd50b53919ca334c8c1031eada1215e78d226d5795e523d6123a2717d0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global gem_name mustache

Name: rubygem-%{gem_name}
Version: 1.1.1
Release: 1%{?dist}
Summary: Mustache is a framework-agnostic way to render logic-free views
License: MIT
URL: https://github.com/mustache/mustache
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-mustache-1.1.1-Fix-test-race-condition.patch
BuildRequires: oreon-rpm-macros
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(ostruct)
BuildArch: noarch

%description
Inspired by ctemplate, Mustache is a framework-agnostic way to render
logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation:
it is impossible to embed application logic in this template
language.

Think of Mustache as a replacement for your views. Instead of views
consisting of ERB or HAML with random helpers and arbitrary logic,
your views are broken into two parts: a Ruby class and an HTML
template.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%oreon_sha256
%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_mandir}/man5
cp -a .%{gem_instdir}/man/mustache.5 %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man1
cp -a .%{gem_instdir}/man/mustache.1 %{buildroot}%{_mandir}/man1

cp -a .%{gem_instdir}/man/*.html .

%check
pushd .%{gem_instdir}
sed -i '/simplecov/,/^end$/ s/^/#/' test/helper.rb

LANG=C.UTF-8 ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%doc *.html
%{_bindir}/mustache
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/man
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
