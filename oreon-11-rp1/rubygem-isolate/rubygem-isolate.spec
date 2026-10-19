%global source0_hash c5998030cbe6baf07a0434294d5feb62c68f5d9147e3e99c3d02e45b46be813c
%global	gem_name	isolate
Summary:        Very simple RubyGems sandbox
Name:		rubygem-%{gem_name}
Version:	4.1.0
Release:        1%{?dist}
License:	MIT
URL:		http://github.com/jbarnette/isolate
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch:	noarch
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(hoe)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Isolate is a very simple RubyGems sandbox. It provides a way to
express and automatically install your project's Gem dependencies.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Remove strict version requirement for rubygems
sed -i ./%{gem_name}-%{version}.gemspec \
	-e '\@required_rubygems_version@s|~>|>=|'

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest \
	Manifest.txt \
	Rakefile \
	test/ \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

ping -c 3 www.google.co.jp || exit 0
pushd .%{gem_instdir}
sed -i Rakefile -e 's|^ENV\["GEM_PATH"\] +=.*|ENV["GEM_PATH"] += ":"|'
rake test --trace
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-isolate-doc -f %{oreon_filedir}/rubygem-isolate-doc.list

%changelog

%autochangelog
