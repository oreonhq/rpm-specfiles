# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fbef3479b69c875aacb118dde77a40d6cc3a91e2c1d505a4c3f3f9e92d142641
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global gem_name kramdown

Name: rubygem-%{gem_name}
Version: 2.6.1
Release: 1%{?dist}
Summary: Fast, pure-Ruby Markdown-superset converter

License:	MIT
URL:		http://kramdown.gettalong.org
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: oreon-rpm-macros
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	rubygem(rexml)
BuildRequires:	rubygem(rouge) >= 3.26.0
BuildRequires:	rubygem(test-unit)
%if ! 0%{?rhel} && ! 0%{?oreon}
BuildRequires:	rubygem(stringex)
BuildRequires:	tidy
BuildRequires:	tex
BuildRequires:	tex(acronym.sty)
BuildRequires:	tex(amssymb.sty)
BuildRequires:	tex(amsmath.sty)
BuildRequires:	tex(amsthm.sty)
BuildRequires:	tex(amsfonts.sty)
BuildRequires:	tex(listings.sty)
BuildRequires:	tex(xpatch.sty)
BuildRequires:	tex(utf8x.def)
%if 0%{?fedora} >= 44
BuildRequires:	texlive-koma-script
BuildRequires:	texlive-ec
%else
BuildRequires:	tex(scrartcl.cls)
BuildRequires:	tex-ec
%endif
%endif
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch: noarch

Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
kramdown is yet-another-markdown-parser but fast, pure Ruby,
using a strict syntax definition and supporting several common extensions.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%oreon_sha256
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/man/man1/kramdown.1 \
	%{buildroot}%{_mandir}/man1

pushd %{buildroot}%{gem_instdir}
rm -rf \
	test/

%check
LANG=C.UTF-8

pushd .%{gem_instdir}

%if 0%{?rhel} || 0%{?oreon}
sed -i test/testcases/block/04_header/with_auto_ids.options \
       -e '\@transliterated_header_ids@s|true|false|'
sed -i \
       test/testcases/block/04_header/with_auto_ids.* \
       -e '\@[Tr]ransliterated@d'
%endif

sed -i.skip test/test_files.rb \
	-e "\@EXCLUDE_LATEX_FILES =@s|^\(.*\)$|\1 'test/testcases/block/04_header/with_auto_ids.text', #texlive 2022|"

export RUBYLIB=$(pwd)/lib
ruby -e 'Dir.glob "./test/test_*.rb", &method(:require)'

popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/COPYING
%doc	%{gem_instdir}/AUTHORS
%doc	%{gem_instdir}/CONTRIBUTERS
%doc	%{gem_instdir}/README.md
%doc	%{gem_instdir}/VERSION

%{_bindir}/kramdown
%{gem_instdir}/bin
%{_mandir}/man1/kramdown.1*

%{gem_libdir}/
%{gem_instdir}/data/

%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
