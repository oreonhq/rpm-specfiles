%global source0_hash c412c2b6ddd4734bb688d8e40a16cf1b036f3f0d1e06e2230f884fc46fefaf3b

%global	gem_name	power_assert

# Note: 1.1.7 -> 1.2.0: just the upstream URL changed
Name:		rubygem-%{gem_name}
Version:	3.0.1
Release:	2%{?dist}

Summary:	Power Assert for Ruby
# SPDX confirmed
License:	Ruby OR BSD-2-Clause
URL:	https://github.com/ruby/power_assert
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-tests-%{version}.tar.gz
# Source1 is created by bash %%{SOURCE2} %%{version}
Source2:	create-power_assert-test-files.sh

BuildRequires:	rubygems-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(irb) >= 1.3.1

BuildArch:	noarch

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

# cleanup
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

%check
pushd .%{gem_instdir}
# test-1.1.3/block_test.rb 1.1.3
LANG=C.utf8
ruby -Ilib:. \
	-e \
	'Dir.glob("test/**/*_test.rb").each {|f| require f}'
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/BSDL
%license	%{gem_instdir}/COPYING
%license	%{gem_instdir}/LEGAL
%doc	%{gem_instdir}/README.md
%{gem_libdir}
%{gem_spec}

%files	doc
%doc	%{gem_docdir}

%changelog
%autochangelog
