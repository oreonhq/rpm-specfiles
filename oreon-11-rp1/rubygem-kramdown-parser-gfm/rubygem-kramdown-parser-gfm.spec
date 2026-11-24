# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fb39745516427d2988543bf01fc4cf0ab1149476382393e0e9c48592f6581729
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global gem_name kramdown-parser-gfm

Name:           rubygem-%{gem_name}
Summary:        Kramdown parser for GitHub-flavored markdown
Version:        1.1.0
Release:        1%{?dist}

License:        MIT

URL:            https://github.com/kramdown/parser-gfm
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

Patch0:         %{url}/commit/ad48572.patch

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.3

BuildRequires:  rubygem(kramdown) >= 2.0.0
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rouge)

%description
kramdown-parser-gfm provides a kramdown parser for the GFM dialect of
Markdown.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

BuildArch: noarch

%description    doc
Documentation for %{name}.

%prep
%oreon_sha256
%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
mv test/testcases/codeblock_fenced.text test/testcases/codeblock_fenced.disabled

ruby -I'lib' -e 'Dir.glob "./test/**test_*.rb", &method(:require)'

mv test/testcases/codeblock_fenced.disabled test/testcases/codeblock_fenced.text
popd

%files
%license %{gem_instdir}/COPYING

%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%exclude %{gem_instdir}/VERSION

%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}

%doc %{gem_instdir}/CONTRIBUTERS

%{gem_instdir}/test

%changelog
%autochangelog
