%global source0_hash 0cd7c7f824e010c072e33f68bc02d85a00aeb6fce05bb4819c03dfd3c140c289
%global	gem_name	mini_portile2
Name:		rubygem-%{gem_name}
Version:	2.8.9
Release:        1%{?dist}
Summary:        Simplistic port-like solution for developers
License:	MIT
URL:		http://github.com/flavorjones/mini_portile
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:		noarch
# oreon:deps
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

exit 0
ping -w3 fedoraproject.org || exit 0
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mini_portile2-doc -f %{oreon_filedir}/rubygem-mini_portile2-doc.list

%changelog

%autochangelog
