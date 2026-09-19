%global source0_hash d21131e519c86f1a5bc2b6d2d57d46e6998e47f18ed249b25cad86433dbd695d

%global	gem_name	xml-simple

# 1.1.9 is from ruby 3.0 only
Name:		rubygem-%{gem_name}
Version:	1.1.9
Release:	11%{?dist}

Summary:	A simple API for XML processing
License:	MIT

URL:		https://github.com/maik/xml-simple
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-tests-%{version}.tar.gz
# Source1 is created from $ bash %%SOURCE2 <version> <githash>
Source2:	create-xml-simple-test-suite.sh

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(rexml)
# tests
BuildRequires:	rubygem(test-unit)

BuildArch:	noarch

%description
A simple API for XML processing.

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

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%check
cp -a test .%{gem_instdir}
pushd .%{gem_instdir}

# Sometimes we see:
# Error: test_perl_test_cases(TC_Perl_Mem_Copy): RuntimeError: Time moved backwards!
# Error: test_perl_test_cases(TC_Perl_Mem_Share): RuntimeError: Time moved backwards!
# See: https://apenwarr.ca/log/20181113
grep -l backwards test/tc_*.rb | \
	xargs sed -i '\@backwards@s|raise|#raise|'

# passing nil to xml_in makes it search for the ruby script being run
ruby -Ilib test/tc_perl_in.rb
mv test/tc_perl_in.rb{,.bak}
ruby -Ilib -e 'Dir.glob "./test/*.rb", &method(:require)'
mv test/tc_perl_in.rb{.bak,}
popd

%files
%dir	%{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
