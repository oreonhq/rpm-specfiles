%global source0_hash 2d3b17f8a36fe7801c1adcffdbc38233b938eb0b4966e97a6739055a45fa77d5

%global gem_name minitest

Name: rubygem-%{gem_name}5
Version: 5.27.0
Release: 2%{?dist}
Summary: minitest provides a complete suite of testing facilities
# README.rdoc
# SPDX confirmed
License: MIT
URL: https://minite.st/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch

%description
minitest provides a complete suite of testing facilities supporting
TDD, BDD, mocking, and benchmarking.

minitest/test is a small and incredibly fast unit testing framework.
It provides a rich set of assertions to make your tests clean and
readable.

minitest/spec is a functionally complete spec engine. It hooks onto
minitest/unit and seamlessly bridges test assertions over to spec
expectations.

minitest/benchmark is an awesome way to assert the performance of your
algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential
one!

minitest/mock by Steven Baker, is a beautifully tiny mock (and stub)
object framework.

minitest/pride shows pride in testing and adds coloring to your test
output. I guess it is an example of how to write IO pipes too. :P
minitest/unit is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working
test suite. For example, there is no magic involved for test-case
discovery.

minitest doesn't reinvent anything that ruby already provides, like:
classes, modules, inheritance, methods. This means you only have to
learn ruby to use minitest and all of your regular OO practices like
extract-method refactorings still apply.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest \
	Manifest.txt \
	Rakefile \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}

ruby -Ilib:test -e 'Dir.glob "./test/minitest/test_*.rb", &method(:require)'

popd

%files
%license %{gem_instdir}/README.rdoc
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%{gem_instdir}/design_rationale.rb

%changelog
%autochangelog
