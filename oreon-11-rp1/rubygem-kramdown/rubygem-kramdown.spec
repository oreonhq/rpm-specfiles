# Generated from kramdown-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name kramdown

Name: rubygem-%{gem_name}
Version: 2.5.2
Release: 3%{?dist}
Summary: Fast, pure-Ruby Markdown-superset converter

# SPDX confirmed
License:	MIT
URL:		http://kramdown.gettalong.org
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	rubygem(rexml)
BuildRequires:	rubygem(rouge) >= 3.26.0
BuildRequires:	rubygem(test-unit)
%if ! 0%{?rhel}
BuildRequires:	rubygem(stringex)
# Recommends:	rubygem(stringex)
# Some additional dependency for check
BuildRequires:	tidy
BuildRequires:	tex
BuildRequires:	tex(acronym.sty)
BuildRequires:	tex(amssymb.sty)
BuildRequires:	tex(amsmath.sty)
BuildRequires:	tex(amsthm.sty)
BuildRequires:	tex(amsfonts.sty)
BuildRequires:	tex(listings.sty)
# Ideally scrarctl.cls side should have Requires for xpatch.sty
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

# Move man pages
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/man/man1/kramdown.1 \
	%{buildroot}%{_mandir}/man1

# Cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	test/

%check
LANG=C.UTF-8

pushd .%{gem_instdir}

%if 0%{?rhel}
# Avoid unwanted stringex dependency
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.2-3
- Prepare for Oreon 11 (RP1)
