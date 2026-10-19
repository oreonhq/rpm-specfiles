%global source0_hash 2fbbbc82c1ce79c4195b13018a87cbb00d762bda39241bb3cdc32792759dd3f4
%global	gem_name	text
Name:		rubygem-%{gem_name}
Version:	1.3.1
Release:        1%{?dist}
Summary:        Collection of text algorithms
License:	MIT
URL:		http://github.com/threedaymonk/text
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(csv)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A collection of text algorithms: Levenshtein, Soundex, Metaphone, Double
Metaphone, Figlet, Porter Stemming

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

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
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
ruby -Ilib:test:. -e 'gem "minitest" ; Dir.glob("test/*_test.rb").each{|f| require f}'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-text-doc -f %{oreon_filedir}/rubygem-text-doc.list

%changelog

%autochangelog
