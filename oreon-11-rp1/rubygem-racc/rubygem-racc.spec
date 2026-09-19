%global source0_hash 4a7f6929691dbec8b5209a0b373bc2614882b55fc5d2e447a21aaa691303d62f

%global	gem_name	racc

Name:		rubygem-%{gem_name}
Version:	1.8.1
Release:	105%{?dist}

Summary:	LALR(1) parser generator
# SPDX confirmed
License:	BSD-2-Clause
URL:		https://github.com/tenderlove/racc

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source10:	rubygem-%{gem_name}-%{version}-missing-files.tar.gz
# Source10 is created by %%{SOURCE11} %%version
Source11:	racc-create-tarball-missing-files.sh

BuildRequires:	gcc
BuildRequires:	rubygems-devel
BuildRequires:	ruby-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-ruby-core)

%description
Racc is a LALR(1) parser generator.
It is written in Ruby itself, and generates Ruby program.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 10

mv ../%{gem_name}-%{version}.gemspec .

# Fix shebang
grep -rl /usr/local . | xargs -r sed -i -e 's|/usr/local|/usr|'

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{_prefix}
cp -a .%{_prefix}/* \
	%{buildroot}%{_prefix}/

cp -a ./%{gem_name}-%{version}/sample \
	%{buildroot}%{gem_instdir}

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* \
	%{buildroot}%{gem_extdir_mri}/
rm -f %{buildroot}%{gem_extdir_mri}/{gem_make.out,mkmf.log}

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	ext/ \
	fastcache/ \
	misc/ \
	tasks/ \
	test/ \
	DEPENDS \
	Manifest.txt \
	Rakefile \
	setup.rb \
	%{nil}

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
cp -a %{gem_name}-%{version}/* .%{gem_instdir}
pushd .%{gem_instdir}

LANG=C.utf8
export RUBYLIB=$(pwd)/lib:$(pwd)/test:$(pwd)/test/lib
ruby -Ilib:test:test/lib:. -e \
	"gem 'test-unit' ; require 'helper' ; Dir.glob('test/test_*.rb').each {|f| require f}"
popd

%files
%dir	%{gem_instdir}

%license	%{gem_instdir}/BSDL
%license	%{gem_instdir}/COPYING
%doc	%lang(ja)	%{gem_instdir}/README.ja.rdoc
%doc	%{gem_instdir}/README.rdoc
%doc	%{gem_instdir}/ChangeLog

%{_bindir}/racc

%{gem_extdir_mri}
%{gem_instdir}/bin
%{gem_libdir}

%{gem_spec}

%files	doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/TODO
%doc	%{gem_instdir}/doc
%doc	%{gem_instdir}/sample

%changelog
%autochangelog
