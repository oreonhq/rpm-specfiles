%global source0_hash 7040ed7185417a966920987eaa6eaf1be4ea1fc5b25bb03ff4703f98564a55b0

# Generated from minitest-mock-5.27.0.gem by gem2rpm -*- rpm-spec -*-
%global	gem_name	minitest-mock

Name:		rubygem-%{gem_name}
Version:	5.27.0
Release:	3%{?dist}

Summary:	minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object framework
# From README.rdoc
# SPDX confirmed
License:	MIT
URL:		https://minite.st/

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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

# TODO
# test/minitest/test_minitest_mock.rb:670
# this test needs minitest 6
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
