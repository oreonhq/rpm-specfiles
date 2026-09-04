%global source0_hash db6e57956f6ecc6134683b4c87467d6dd792323c7f0eea7b93f66bd284adbc3d

# Generated from minitest-1.4.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name minitest

Name: rubygem-%{gem_name}
Version: 6.0.2
Release: 1%{?dist}
Summary: minitest provides a complete suite of testing facilities
# README.rdoc
# SPDX confirmed
License: MIT
URL: https://github.com/seattlerb/minitest
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(hoe)
BuildArch: noarch

%description
minitest provides a complete suite of testing facilities supporting
TDD, BDD, mocking, and benchmarking.

minitest/unit is a small and incredibly fast unit testing framework.
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
LANG=C.UTF-8
LC_ALL=C.utf8
pushd .%{gem_instdir}

ruby -Ilib:test -e 'Dir.glob "./test/minitest/test_*.rb", &method(:require)'

popd

%files
%license %{gem_instdir}/README.rdoc
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%{gem_instdir}/design_rationale.rb

%changelog
%autochangelog
