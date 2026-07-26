%global source0_hash 0ee7c6a4f5388ef98bcc67312456dd774a4ee2720c93c28be893bedec143d1e2

%global gem_name simplecov-html
%global rubyabi 1.9.1

Summary:       Default HTML formatter for SimpleCov
Name:          rubygem-%{gem_name}
Version:       0.10.0
Release:       21%{?dist}
License:       MIT
URL:           https://github.com/colszowka/simplecov-html
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} >= 19 || 0%{?rhel} > 6
Requires:      ruby(release)
%else
Requires:      ruby(abi) >= %{rubyabi}
%endif
Requires:      ruby 
Requires:      rubygems
BuildRequires: ruby 
BuildRequires: rubygems-devel
# For tests
# Cant run tests because they require a circular
#  dependancy that cant be done yet
#BuildRequires: rubygem(test-unit)
#BuildRequires: rubygem(simplecov)
BuildArch:     noarch
Provides:      rubygem(%{gem_name}) = %{version}

%description
Default HTML formatter for SimpleCov code coverage tool for ruby 1.9+

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

#cleanup
rm -f %{buildroot}%{gem_instdir}/.document
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.rubocop.yml
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/.yardopts
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -f %{buildroot}%{gem_instdir}/Gemfile
rm -f %{buildroot}%{gem_instdir}/simplecov-html.gemspec

%check
# Cant run tests because they require a circular
#  dependancy that cant be done yet
#testrb2 -Ilib test

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/assets
%{gem_instdir}/public
%{gem_instdir}/views
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Guardfile
%{gem_instdir}/Rakefile
%{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
%autochangelog
