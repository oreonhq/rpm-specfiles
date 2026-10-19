%global source0_hash 124ebbf4558d2e03ddf796118473c991e96ea4c73925682b54de69d0b6d6a6d2
%global	gem_name	rdtool
Name:		rubygem-%{gem_name}
Version:	0.6.39
Release:        2%{?dist}
Summary:        Formatter for RD
License:	GPL-2.0-or-later OR Ruby
URL:		https://github.com/uwabami/rdtool
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:	rdtool-pr20-remove-ruby40-warnings.patch
Requires:	rubygem(racc)
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(nkf)
BuildRequires:  rubygem(racc)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
RD is multipurpose documentation format created for documentating Ruby and
output of Ruby world. You can embed RD into Ruby script. And RD have neat
syntax which help you to read document in Ruby script. On the other hand, RD
have a feature for class reference.

%package	doc
Summary:	Documentation for %{name}
License:	(GPL-2.0-or-later OR Ruby) AND GPL-2.0-or-later
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1

# shebang
sed -i \
	-e '\@/usr/bin/env@d' \
	lib/rd/rd2html-ext-opt.rb

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	setup.rb \
	%{gem_name}.gemspec \
	test/ \
	%{nil}
rm -f lib/rd/pre-setup.rb
find lib/rd -type f -print0 | xargs -0 chmod ugo-x
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib:test:. -e 'gem "minitest" ; Dir.glob("test/test-*.rb").each {|f| require f}'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rdtool-doc -f %{oreon_filedir}/rubygem-rdtool-doc.list

%changelog

%autochangelog
