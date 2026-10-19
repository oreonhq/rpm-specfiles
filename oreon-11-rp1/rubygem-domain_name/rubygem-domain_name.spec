%global source0_hash 5f693b2215708476517479bf2b3802e49068ad82167bcd2286f899536a17d933
%global	gem_name	domain_name
Summary:        Domain Name manipulation library for Ruby
Name:		rubygem-%{gem_name}
Version:	0.6.20240107
Release:        7%{?dist}
License:	BSD-2-Clause AND BSD-3-Clause AND MPL-2.0
URL:		https://github.com/knu/ruby-domain_name
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	ruby(rubygems) 
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This is a Domain Name manipulation library for Ruby.
It can also be used for cookie domain validation based on the Public
Suffix List.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version}
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
	.document \
	.github/ \
	.gitignore \
	.travis.yml \
	Gemfile \
	Rakefile \
	%{gem_name}.gemspec \
	data/ \
	test/ \
	tool/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i.orig \
	-e '/begin/,/end/d' \
	-e '/bundler/d' \
	test/helper.rb
for f in test/test_*.rb
do
	ruby -Ilib:test:. $f
done
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-domain_name-doc -f %{oreon_filedir}/rubygem-domain_name-doc.list

%changelog

%autochangelog
