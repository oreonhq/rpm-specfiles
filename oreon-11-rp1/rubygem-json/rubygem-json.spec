%global source0_hash bc656e361461a3b7038b2b45644f20de10016165c208b7ed5240476522fc505f

%global	gem_name	json

%global	pkg_version_num		2.19.2
%dnl		%global	pkg_version_alpha
%global	gem_version()		%{pkg_version_num}%{?pkg_version_alpha:.%pkg_version_alpha}

Name:           rubygem-%{gem_name}
Version:        %{pkg_version_num}%{?pkg_version_alpha:~%pkg_version_alpha}
Release:        1%{?dist}

Summary:        A JSON implementation in Ruby

# SPDX confirmed
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/flori/json
Source0:        https://rubygems.org/gems/%{gem_name}-%{gem_version}.gem
Source1:        rubygem-%{gem_name}-%{gem_version}-missing-files.tar.gz
# Source1 is created by $ %%SOURCE2 v%%version
Source2:        json-create-tarball-missing-files.sh

BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(test-unit-ruby-core)
BuildRequires:  rubygem(test-unit)

Obsoletes:	rubygem-%{gem_name}-gui < %{version}
Obsoletes:	ruby-%{gem_name}-gui < %{version}
Obsoletes:	ruby-%{gem_name} < %{version}

%description
This is a implementation of the JSON specification according
to RFC 4627 in Ruby.
You can think of it as a low fat alternative to XML,
if you want to store data to disk or transmit it over
a network rather than use a verbose markup language.

%package	doc
Summary:	Documentation for %{name}

Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%global	version	%gem_version

%setup -q -n %{gem_name}-%{gem_version} -a 1
mv ./%{gem_name}-%{version}/test .
mv ../%{gem_name}-%{version}.gemspec .

# Change cflags to honor Fedora compiler flags correctly
find . -name extconf.rb | xargs sed -i -e 's|-O3|-O2|' -e 's|-O0|-O2|'

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

find . -name \*gem -exec chmod 0644 {} \;

# remove pure
rm -fr .%{gem_instdir}/lib/json/pure*

%install
mkdir -p $RPM_BUILD_ROOT%{gem_dir}
mkdir -p $RPM_BUILD_ROOT%{gem_extdir_mri}
 
cp -a .%{gem_dir}/* %{buildroot}/%{gem_dir}
cp -a .%{gem_extdir_mri}/{gem.build_complete,json} %{buildroot}/%{gem_extdir_mri}/

mkdir -p %{buildroot}%{ruby_libdir}
mkdir -p %{buildroot}%{ruby_libarchdir}
ln -s %{gem_libdir}/json.rb %{buildroot}%{ruby_libdir}/json.rb
ln -s %{gem_libdir}/json %{buildroot}%{ruby_libdir}/json
ln -s %{gem_extdir_mri}/json/ %{buildroot}%{ruby_libarchdir}/json

find $RPM_BUILD_ROOT%{gem_instdir} -name \*.rb -print0 | \
	xargs --null chmod 0644

# We don't need those files anymore.
pushd $RPM_BUILD_ROOT%{gem_instdir}
rm -rf \
	%{gem_name}.gemspec \
	Gemfile \
	ext \
	java \
	lib/json/truffle_ruby/ \
	test \
	%{nil}
popd

%check
rm -rf .%{gem_instdir}/test
cp -a ./test .%{gem_instdir}/

pushd .%{gem_instdir}
ruby -Ilib:test:test/json:$RPM_BUILD_ROOT%{gem_extdir_mri}:. \
	-e "gem 'test-unit'; require 'test_helper' ; Dir.glob('test/json/*_test.rb').sort.each {|f| require f}"
popd

%files
%dir %{gem_instdir}
%dir %{gem_libdir}
%dir %{gem_libdir}/%{gem_name}

%license %{gem_instdir}/BSDL
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/LEGAL
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md

%{gem_libdir}/%{gem_name}.rb
%{gem_libdir}/%{gem_name}/add
%{gem_libdir}/%{gem_name}/common.rb
%{gem_libdir}/%{gem_name}/ext.rb
%dir	%{gem_libdir}/%{gem_name}/ext
%dir	%{gem_libdir}/%{gem_name}/ext/generator/
%{gem_libdir}/%{gem_name}/ext/generator/*.rb
%{gem_libdir}/%{gem_name}/version.rb
%{gem_libdir}/%{gem_name}/generic_object.rb

%{ruby_libdir}/json*
%{ruby_libarchdir}/json*
%{gem_extdir_mri}/
%{gem_spec}

%exclude %{gem_cache}

%files      doc
%{gem_docdir}/

%changelog
%autochangelog
