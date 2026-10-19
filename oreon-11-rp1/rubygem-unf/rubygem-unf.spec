%global source0_hash e6bcc2e101d80e3f9459753db747d5926aada1aaaf61e629e93359da9a5b04ab
%global	gem_name	unf
%undefine __brp_mangle_shebangs
Summary:        Wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
Name:		rubygem-%{gem_name}
Version:	0.2.0
Release:        4%{?dist}
License:	BSD-2-Clause
URL:		https://github.com/knu/ruby-unf
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	unf-%{version}-test-missing-files.tar.gz
Source2:	unf-create-missing-test-files.sh
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(unf_ext)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This is a wrapper library to bring Unicode Normalization Form support
to Ruby/JRuby.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

%build

sed -i ./%{gem_name}-%{version}.gemspec \
	-e '\@s.extensions@d' \
	-e '\@s.files@s|"ext/[^ \t][^ \t]*||' \
	%{nil}
gem build ./%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	*.gemspec \
	.github/ \
	.gitignore \
	.travis.yml \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -rf .%{gem_instdir}/test/
cp -a ./test/ .%{gem_instdir}
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
%files -n rubygem-unf-doc -f %{oreon_filedir}/rubygem-unf-doc.list

%changelog

%autochangelog
