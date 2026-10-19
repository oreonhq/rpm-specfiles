%global source0_hash 4c59ae90d5f31d3ff8177eeca15205d4c0d35cefd54389d89d92c06aff66b2fb
%global		gem_name		mkrf
Summary:        Making C extensions for Ruby a bit easier
Name:		rubygem-%{gem_name}
Version:	0.2.3
Release:        1%{?dist}
License:	MIT AND (Ruby OR GPL-2.0-only)
URL:		http://mkrf.rubyforge.org/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:	rubygem-mkrf-0.2.3-Rakefile-newrake.patch
Requires:	ruby(release)
BuildArch:		noarch
Provides:		rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  libxml2-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby(rubygems)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rake)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
mkrf is a library for generating Rakefiles to build Ruby
extension modules written in C. It is intended as a replacement for
mkmf. The major difference between the two is that mkrf
builds you a Rakefile instead of a Makefile.

This proposed replacement to mkmf generates Rakefiles to build C Extensions.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1

grep -rl "Config::CONFIG" . | xargs sed -i -e 's|Config::CONFIG|RbConfig::CONFIG|g'

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rake -P | grep 'rake test:' | grep -v 'sample:all' | while read line
do
	eval $line --trace || true
done
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mkrf-doc -f %{oreon_filedir}/rubygem-mkrf-doc.list

%changelog

%autochangelog
