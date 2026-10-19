%global source0_hash 7040ed7185417a966920987eaa6eaf1be4ea1fc5b25bb03ff4703f98564a55b0
%global	gem_name	minitest-mock
Name:		rubygem-%{gem_name}
Version:	5.27.0
Release:        1%{?dist}
Summary:        minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object framework
License:	MIT
URL:		https://minite.st/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:	noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
export RUBYLIB=$(pwd)/lib:$(pwd)/test
sed -i test/minitest/test_minitest_mock.rb \
	-e '\@assertion_count@s|assert_equal|#assert_equal|'
ruby -e \
	'Dir.glob "./test/minitest/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-minitest-mock-doc -f %{oreon_filedir}/rubygem-minitest-mock-doc.list

%changelog

%autochangelog
