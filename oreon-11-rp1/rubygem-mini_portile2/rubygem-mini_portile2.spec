%global source0_hash 0cd7c7f824e010c072e33f68bc02d85a00aeb6fce05bb4819c03dfd3c140c289

%global	gem_name	mini_portile2

Name:		rubygem-%{gem_name}
Version:	2.8.9
Release:	3%{?dist}

Summary:	Simplistic port-like solution for developers
# SPDX confirmed
License:	MIT
URL:		http://github.com/flavorjones/mini_portile
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	rubygems-devel
# BuildRequires:	rubygem(minitest)
# BuildRequires:	rubygem(minitest-hooks)
#BuildRequires:	rubygem(archive-tar-minitar)
BuildArch:		noarch

%description
Simplistic port-like solution for developers. It provides a standard and
simplified way to compile against dependency libraries without messing up your
system.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}
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
	.concourse.yml \
	.github/ \
	.gitignore \
	.travis.yml \
	Gemfile \
	Rakefile \
	appveyor.yml \
	concourse/ \
	*.gemspec \
	test/ \
	%{nil}
popd

%check
# Currently minitest-hooks is not available on Fedora,
# exit
exit 0

# This requires net connection, so give up test suite
# without net
# (also just exit without ping)
ping -w3 fedoraproject.org || exit 0

pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.md
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/SECURITY.md

%{gem_libdir}
%{gem_spec}

%files	doc
%doc	%{gem_docdir}

%changelog
%autochangelog
