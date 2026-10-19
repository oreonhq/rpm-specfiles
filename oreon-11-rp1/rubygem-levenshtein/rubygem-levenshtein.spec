%global source0_hash e2088ce4eaf4460e48c1812f43f5d89c50835830e74adcb4317cc477d4f1bf98
%global	gem_name	levenshtein
Summary:        Calculates the Levenshtein distance between two byte strings
Name:		rubygem-%{gem_name}
Version:	0.2.2
Release:        1%{?dist}
License:	GPL-2.0-only
URL:		http://www.erikveen.dds.nl/levenshtein/doc/index.html
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	ruby(rubygems) 
Provides:	rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Calculates the Levenshtein distance between two byte strings.

The Levenshtein distance is a metric for measuring the amount
of difference between two sequences (i.e., the so called edit
distance). The Levenshtein distance between two sequences is
given by the minimum number of operations needed to transform
one sequence into the other, where an operation is an
insertion, deletion, or substitution of a single element.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}%{gem_extdir_mri}
rm -f \
	gem_make.out \
	mkmf.log \
	%{nil}
popd
pushd %{buildroot}%{gem_instdir}
rm -rf \
	ext/ \
	test/ \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
export RUBYLIB=$(pwd)/lib:%{buildroot}%{gem_extdir_mri}
ruby ./test/test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-levenshtein-doc -f %{oreon_filedir}/rubygem-levenshtein-doc.list

%changelog

%autochangelog
