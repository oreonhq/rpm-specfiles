%global source0_hash ebbcaa2cb4930fa1b83206f432c5cb64746507b2dcf50ea1301569a4d662cda6

%global	gem_name	webrobots

Summary:	Ruby library to help write robots.txt compliant web robots
Name:		rubygem-%{gem_name}
Version:	0.1.2
Release:	23%{?dist}

# SPDX confirmed
License:	BSD-2-Clause
URL:		https://github.com/knu/webrobots
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Replace shoulda with shoulda-context, which is enough to execute the test
# suite.
# https://github.com/knu/webrobots/pull/8
Patch0:	rubygem-webrobots-0.1.2-shoulda-context-is-enough-to-execute-the-test-suite.patch

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel 
# %%check
# F-19: kill check until should is rebuilt
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(base64)
BuildRequires:	rubygem(shoulda-context)
BuildRequires:	rubygem(webmock)
BuildRequires:	rubygem(vcr)
BuildRequires:	rubygem(nokogiri)
BuildRequires:	rubygem(racc)
# Add nokogiri dependency
Requires:	rubygem(nokogiri)
Requires:	rubygem(racc)

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
This library helps write robots.txt compliant web robots in Ruby.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1
%gemspec_remove_dep -s %{gem_name}-%{version}.gemspec -g shoulda -d ">= 0"
%gemspec_add_dep -s %{gem_name}-%{version}.gemspec -g shoulda-context -d

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Clean up
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.document \
	.gitignore \
	.travis.yml \
	Gemfile \
	Rakefile \
	test/ \
	%{gem_name}.gemspec \
	%{nil}
popd

%check
pushd .%{gem_instdir}
sed -i.orig \
	-e '/begin/,/end/d' \
	-e '/bundler/d' \
	test/helper.rb

ruby -Ilib:test test/test_webrobots.rb
popd

%files
%dir	%{gem_instdir}/
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}/

%changelog
%autochangelog
