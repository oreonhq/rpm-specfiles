%global source0_hash 1ba542204c66b6f9111ff00dcc26075b95b220b07f2905d8261740c82f7f02fa
%global gem_name kramdown
Name: rubygem-%{gem_name}
Version: 2.5.2
Release:        1%{?dist}
Summary:        Fast, pure-Ruby Markdown-superset converter
License:	MIT
URL:		http://kramdown.gettalong.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch: noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(rouge)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LANG=C.UTF-8
pushd .%{gem_instdir}
sed -i.skip test/test_files.rb \
	-e "\@EXCLUDE_LATEX_FILES =@s|^\(.*\)$|\1 'test/testcases/block/04_header/with_auto_ids.text', #texlive 2022|"
export RUBYLIB=$(pwd)/lib
ruby -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-kramdown-doc -f %{oreon_filedir}/rubygem-kramdown-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.2-3
- Prepare for Oreon 11 (RP1)
