%global source0_hash 124ebbf4558d2e03ddf796118473c991e96ea4c73925682b54de69d0b6d6a6d2

%global	gem_name	rdtool

Name:		rubygem-%{gem_name}
Version:	0.6.39
Release:	2%{?dist}

Summary:	Formatter for RD
# SPDX confirmed
# From README.rd
# GPL-2.0-or-later OR Ruby:	Overall
# GPL-2.0-or-later:	utils/rd-mode.el
# LGPL-2.0:	setup.rb (not included in the binary rpm)
License:	GPL-2.0-or-later OR Ruby
URL:		https://github.com/uwabami/rdtool
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/uwabami/rdtool/pull/20
# Remove warnings for ruby 4.0
Patch0:	rdtool-pr20-remove-ruby40-warnings.patch

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(nkf)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(racc)
Requires:	rubygem(racc)
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
RD is multipurpose documentation format created for documentating Ruby and
output of Ruby world. You can embed RD into Ruby script. And RD have neat
syntax which help you to read document in Ruby script. On the other hand, RD
have a feature for class reference.

%package	doc
Summary:	Documentation for %{name}
# utils/rd-mode.el is under GPLv2+
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

# Cleanup
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

%check
pushd .%{gem_instdir}
ruby -Ilib:test:. -e 'gem "minitest" ; Dir.glob("test/test-*.rb").each {|f| require f}'
popd

%files
%dir %{gem_instdir}

%license	%{gem_instdir}/COPYING.txt
%exclude	%{gem_instdir}/LGPL-2.1
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/[HM-Z]*

%{_bindir}/rd2
%{_bindir}/rdswap.rb

%{gem_instdir}/bin
%{gem_libdir}/

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/doc/
%{gem_instdir}/utils/

%changelog
%autochangelog
