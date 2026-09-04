%global source0_hash 4c5846c27c8250bfb2b924375d5ba1a48359d4d8ddd92db3faba3ea2ad7430ce

%global	gem_name	isolate
Summary:	Very simple RubyGems sandbox

Name:		rubygem-%{gem_name}
Version:	4.1.1
Release:	1%{?dist}
# SPDX confirmed
License:	MIT
URL:		http://github.com/jbarnette/isolate
Source0:	https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch:	noarch

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(hoe)
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(rake)
#BuildRequires:	iputils

Requires:	rubygems

Provides:	rubygem(%{gem_name}) = %{version}

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

# cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest \
	Manifest.txt \
	Rakefile \
	test/ \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}

%check
ping -c 3 www.google.co.jp || exit 0

pushd .%{gem_instdir}
# FIXME I actually don't know why the following work...
sed -i Rakefile -e 's|^ENV\["GEM_PATH"\] +=.*|ENV["GEM_PATH"] += ":"|'
rake test --trace
popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/CHANGELOG.rdoc
%license	%{gem_instdir}/README.rdoc
%{gem_instdir}/lib/
%{gem_spec}

%files doc
%{gem_docdir}

%changelog
%autochangelog
