# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4eeb0185c0fbfa889efed923b5b50e949cd869e7d82ac74138acd0c9c7165ec0
%global source1_hash 766de812aaa69ca57392eaab3f3b3bd764b4ba71f8f8b229fd9787934563abd6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global gem_name ronn-ng

Name:           rubygem-%{gem_name}
Version:        0.10.1
Release:        1%{?dist}
Summary:        Builds man pages from Markdown
License:        MIT
URL:            https://github.com/apjanke/ronn-ng
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-test.tar.gz
Patch0:         ronn-ng-pr125-ruby34-fileutils-deps.patch
BuildRequires: oreon-rpm-macros
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(kramdown)
BuildRequires:  rubygem(kramdown-parser-gfm)
BuildRequires:  rubygem(mustache)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(test-unit)
BuildArch:      noarch

Requires:       groff-base
Provides:       rubygem-ronn = %{version}-%{release}
Obsoletes:      rubygem-ronn < 0.7.3-20

%description
Ronn-NG builds manuals in HTML and Unix man page format from Markdown.

The source format includes all of Markdown but has a more rigid structure and
syntax extensions for features commonly found in man pages (definition lists,
link notation, etc.). The ronn-format(7) manual page defines the format in
detail.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}/test
%patch -P0 -p2
)

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

install -Dt %{buildroot}/%{_mandir}/man1/ -m 0644 %{buildroot}%{gem_instdir}/man/ronn.1
install -Dt %{buildroot}/%{_mandir}/man7/ -m 0644 %{buildroot}%{gem_instdir}/man/ronn-format.7

install -Dt %{buildroot}/usr/share/bash-completion/completions/ -m 0644 %{buildroot}%{gem_instdir}/completion/bash/ronn
install -Dt %{buildroot}/usr/share/zsh/site-functions/ -m 0644 %{buildroot}%{gem_instdir}/completion/zsh/_ronn

%check
pushd .%{gem_instdir}
cp -a %{_builddir}/test test

ruby -Itest -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/ronn
%{gem_instdir}/INSTALLING.md
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%exclude %{gem_instdir}/completion
%{gem_instdir}/config.ru
%{gem_libdir}
%exclude %{gem_instdir}/man
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/ronn.1*
%{_mandir}/man7/ronn-format.7*
%dir %_datadir/bash-completion//
%_datadir/bash-completion/completions/
%_datadir/zsh/site-functions/

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ronn-ng.gemspec

%changelog
%autochangelog
