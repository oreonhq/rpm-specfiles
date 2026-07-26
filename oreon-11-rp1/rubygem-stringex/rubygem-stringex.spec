%global source0_hash c7b382d2b2a47a1e1646f256df201c48d487d6296fbb289d76802f67f5e929c4

%global gem_name stringex

Name:           rubygem-%{gem_name}
Summary:        Useful extensions to Ruby's String class
Version:        2.8.6
Release:        7%{?dist}
# SPDX confirmed
License:        MIT

URL:            http://github.com/rsl/stringex
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby

BuildRequires:  rubygem(activerecord)
BuildRequires:  rubygem(i18n)
BuildRequires:  rubygem(RedCloth)
BuildRequires:  rubygem(sqlite3)
BuildRequires:  rubygem(test-unit)

%description
Some [hopefully] useful extensions to Ruby's String class. Stringex is made up
of three libraries: ActsAsUrl [permalink solution with better character
translation], Unidecoder [Unicode to ASCII transliteration], and
StringExtensions [miscellaneous helper methods for the String class].

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# Relax unstable time-dependent test strictness
sed -i test/performance/localization_performance_test.rb \
	-e 's|allowed_difference = 25|allowed_difference = 99|'

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	stringex.gemspec \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
ruby -I'lib:test' -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%license %{gem_instdir}/MIT-LICENSE

%dir %{gem_instdir}
%{gem_instdir}/VERSION
%{gem_instdir}/init.rb
%{gem_instdir}/locales

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
