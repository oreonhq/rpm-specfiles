%global source0_hash e72e626413ea47099becb7b5683beb1c2ea902c69f5bad55c9258fe2b48314d7

%global	gem_name	contracts

Name:		rubygem-%{gem_name}
Version:	0.17.3
Release:	2%{?dist}

Summary:	Contracts for Ruby
# SPDX confirmed
License:	BSD-2-Clause
URL:		http://egonschiele.github.io/contracts.ruby/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(rspec) >= 3
BuildArch:		noarch

%description
This library provides contracts for Ruby. Contracts let you clearly express
how your code behaves, and free you from writing tons of boilerplate,
defensive code.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

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
	.[^.]* \
	Gemfile \
	Rakefile \
	*gemspec \
	*yml \
	features/ \
	script/ \
	spec/ \
	%{nil}

%check
pushd .%{gem_instdir}
rspec spec/
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE
%doc		%{gem_instdir}/CHANGELOG.markdown
%doc		%{gem_instdir}/README.md
%doc		%{gem_instdir}/TODO.markdown
%doc		%{gem_instdir}/TUTORIAL.md

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
# Keep this
%{gem_instdir}/benchmarks/

%changelog
%autochangelog
