%global source0_hash 4c0e66e84a2f9b2ea4ea4679394c4a950d8473e56a44316081d711f258afbe98

%global	gem_name	parseconfig

Name:			rubygem-%{gem_name}
Version:		1.1.2
Release:		10%{?dist}

Summary:		Config File Parser for Standard Unix/Linux Type Config Files
License:		MIT
URL:			http://github.com/datafolklabs/ruby-parseconfig/
Source0:		https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:		rubygem-parseconfig-%{version}-tests.tar.gz
# Source1 is created by Source2
Source2:		parseconfig-create-test-suite.sh

BuildRequires:	ruby(release)
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygems-devel
BuildArch:		noarch

%description
ParseConfig provides simple parsing of standard configuration files in the
form of 'param = value'.  It also supports nested [group] sections.

%package		doc
Summary:		Documentation for %{name}
Requires:		%{name} = %{version}-%{release}
BuildArch:		noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

# 1.1.2 only
# https://github.com/datafolklabs/ruby-parseconfig/issues/39
sed -i lib/version.rb -e "\@VERSION@s|'.*'|'%{version}'|"

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

cp -a ./tests .%{gem_instdir}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

pushd %{buildroot}
rm -rf  \
	.%{gem_cache} \
	.%{gem_instdir}/tests/ \
	%{nil}

%check
cd tests
ruby ./test_parseconfig.rb
cd ..

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/Changelog
%doc	%{gem_instdir}/README.md
%license	%{gem_instdir}/LICENSE
%{gem_libdir}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
