%global source0_hash 346af09fe4c4d793a9107b978d9a62e3274972e5c17b8d4c0a8f348c77e78250

%global	gem_name	test-unit-rr

Summary:	Test::Unit::RR - RR adapter for Test::Unit
Name:		rubygem-%{gem_name}
Version:	1.0.5
Release:	22%{?dist}
# SPDX confirmed
License:	LGPL-2.1-or-later
URL:		http://rubyforge.org/projects/test-unit/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel 
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(rr)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Test::Unit::RR - RR adapter for Test::Unit.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version} -p1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

# Permission
find . -type f -print0 | xargs --null chmod go-w

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Manifest.txt \
	Rakefile \
	*.gemspec \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
ruby -Ilib test/run-test.rb
popd

%files
%dir	%{gem_instdir}
%{gem_libdir}/
%{gem_spec}

%doc	%{gem_instdir}/[A-Z]*
%dir	%{gem_instdir}/doc/
%dir	%{gem_instdir}/doc/text/
%license	%{gem_instdir}/doc/text/lgpl-2.1.txt
%doc	%{gem_instdir}/doc/text/news.md

%files doc
%doc	%{gem_docdir}/

%changelog
%autochangelog
