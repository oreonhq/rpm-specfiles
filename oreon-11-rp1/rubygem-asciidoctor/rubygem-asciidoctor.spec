%global source0_hash none

%global gem_name asciidoctor
%global mandir %{_mandir}/man1

%define pre %nil
%global gittag v%{version}%{pre}

Summary: A fast, open source AsciiDoc implementation in Ruby
Name: rubygem-%{gem_name}
Version: 2.0.26
Release: 2%{?dist}
License: MIT
URL: https://asciidoctor.org
Source0:        https://github.com/asciidoctor/asciidoctor/archive/%{gittag}/%{gem_name}-%{version}%{pre}.tar.gz
%if 0%{?el7}
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
BuildRequires: rubygems-devel
BuildRequires: ruby(rubygems)
%if ! 0%{?rhel}
# Dependencies aren't available on EPEL
BuildRequires: rubygem(coderay)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(erubi)
BuildRequires: rubygem(haml)
BuildRequires: rubygem(logger)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rouge)
BuildRequires: rubygem(slim)
BuildRequires: rubygem(tilt)
%endif
BuildArch: noarch
Provides: asciidoctor = %{version}
%if 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%if %{?pre:1}
%global gem_instdir() %{gem_dir}/gems/%{gem_name}-%{version}%{pre}
%global gem_cache   %{gem_dir}/cache/%{gem_name}-%{version}%{pre}.gem
%global gem_spec    %{gem_dir}/specifications/%{gem_name}-%{version}%{pre}.gemspec
%global gem_docdir  %{gem_dir}/doc/%{gem_name}-%{version}%{pre}
%endif

%description
A fast, open source text processor and publishing toolchain, written in Ruby,
for transforming AsciiDoc markup into HTML 5, DocBook 4.5, DocBook 5.0 and
custom output formats. The transformation from AsciiDoc to custom output
formats is performed by running the nodes in the parsed document tree through a
collection of templates written in a template language supported by Tilt.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{gem_name}-%{version}%{pre} -p1

# Include tests in the gem, they're disabled by default
sed -i -e 's/#\(s\.test_files\)/\1/' %{gem_name}.gemspec

# Fix shebang (avoid Requires: /usr/bin/env)
sed -i -e 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' bin/%{gem_name}

# ref: https://github.com/asciidoctor/asciidoctor/issues/4684
# the upstream plans to remove logger dep, but for now
# add logger dep explicitly for ruby3_5
%gemspec_add_dep -g logger -s ./%{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install -n %{gem_name}-%{version}%{pre}.gem

%check
pushd .%{gem_instdir}

%if ! 0%{?rhel}
# Asciidoctor tests require Minitest 5, so we can't run them on EPEL
#
# disable tests which require open-uri-cached gem
sed -Ei "/test 'should cache remote (SVG|image) when allow-uri-read, cache-uri, and (inline option|data-uri) are set' do/a \\
      skip('open-uri-cached gem is not avaiable on Fedora')" test/blocks_test.rb
LANG=C.UTF-8 ruby -I"lib:test" -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
%endif
popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
       %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
       %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{mandir}
cp -a .%{gem_instdir}/man/*.1 \
       %{buildroot}%{mandir}/

%files
%dir %{gem_instdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/asciidoctor.gemspec
%exclude %{gem_instdir}/man
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/features
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/CHANGELOG.adoc
%doc %{gem_instdir}/README.*
%lang(de) %doc %{gem_instdir}/README-de.*
%lang(fr) %doc %{gem_instdir}/README-fr.*
%lang(ja) %doc %{gem_instdir}/README-jp.*
%lang(zh_CN) %doc %{gem_instdir}/README-zh_CN.*
%{gem_instdir}/data
%{_bindir}/*
%{gem_instdir}/bin
%{gem_libdir}
%{mandir}/*
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.26-2
- Prepare for Oreon 11 (RP1)
