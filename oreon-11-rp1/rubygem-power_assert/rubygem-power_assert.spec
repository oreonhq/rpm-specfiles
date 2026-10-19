%global source0_hash 8ce9876716cc74e863fcd4cdcdc52d792bd983598d1af3447083a3a9a4d34103
%global	gem_name	power_assert
Name:		rubygem-%{gem_name}
Version:	3.0.1
Release:        2%{?dist}
Summary:        Power Assert for Ruby
License:	Ruby OR BSD-2-Clause
URL:	https://github.com/ruby/power_assert
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-tests-%{version}.tar.gz
Source2:	create-power_assert-test-files.sh
BuildArch:	noarch
# oreon:deps
BuildRequires:  rubygem(irb)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Power Assert for Ruby. Power Assert shows each value of variables and method
calls in the expression. It is useful for testing, providing which value
wasn't correct when the condition is not satisfied.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
cp -a ./test ./%{gem_instdir}/
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.gitignore .travis.yml \
	.github/ \
	Gemfile \
	Rakefile \
	*gemspec \
	benchmarks \
	bin/ \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
LANG=C.utf8
ruby -Ilib:. \
	-e \
	'Dir.glob("test/**/*_test.rb").each {|f| require f}'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-power_assert-doc -f %{oreon_filedir}/rubygem-power_assert-doc.list

%changelog

%autochangelog
